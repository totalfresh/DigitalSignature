from flask import Flask, request, render_template, redirect, url_for, send_from_directory
from sign_file import podpisz_plik, zhaszuj_plik
from verify_signature import weryfikuj_podpis
from generate_random_data import generate_random_data
import os
from Crypto.PublicKey import RSA

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = os.path.join(os.getcwd(), 'static')

def generate_unique_filename(directory, filename):
    base, extension = os.path.splitext(filename)
    counter = 1
    new_filename = filename
    while os.path.exists(os.path.join(directory, new_filename)):
        new_filename = f"{base}_{counter}{extension}"
        counter += 1
    return new_filename

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/sign', methods=['POST'])
def sign_file():
    file = request.files['file']
    private_key = request.files['private_key']

    if file and private_key:
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        private_key_path = os.path.join(app.config['UPLOAD_FOLDER'], private_key.filename)

        file.save(file_path)
        private_key.save(private_key_path)

        podpisz_plik(file_path, private_key_path)
        zhaszuj_plik(file_path)
        return redirect(url_for('index'))

@app.route('/hash', methods=['POST'])
def hash_file():
    file = request.files['file']

    if file:
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(file_path)

        zhaszuj_plik(file_path)

        return redirect(url_for('index'))

@app.route('/verify', methods=['POST'])
def verify_file():
    file = request.files['file']
    signature = request.files['signature']
    public_key = request.files['public_key']
    hash_file = request.files['hash']

    if file and signature and public_key and hash_file:
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        signature_path = os.path.join(app.config['UPLOAD_FOLDER'], signature.filename)
        public_key_path = os.path.join(app.config['UPLOAD_FOLDER'], public_key.filename)
        hash_file_path = os.path.join(app.config['UPLOAD_FOLDER'], hash_file.filename)

        file.save(file_path)
        signature.save(signature_path)
        public_key.save(public_key_path)
        hash_file.save(hash_file_path)

        message = weryfikuj_podpis(file_path, signature_path, public_key_path, hash_file_path)

        return render_template('result.html', message=message)
    else:
        return "Brakujące pliki", 400

@app.route('/generate_key', methods=['POST'])
def generate_key():
    try:
        key = RSA.generate(2048)
        private_key = key.export_key()
        public_key = key.publickey().export_key()
        
        private_key_filename = generate_unique_filename(app.config['UPLOAD_FOLDER'], 'private_key.pem')
        public_key_filename = generate_unique_filename(app.config['UPLOAD_FOLDER'], 'public_key.pem')
        
        with open(os.path.join(app.config['UPLOAD_FOLDER'], private_key_filename), 'wb') as priv_file:
            priv_file.write(private_key)
        with open(os.path.join(app.config['UPLOAD_FOLDER'], public_key_filename), 'wb') as pub_file:
            pub_file.write(public_key)

        return redirect(url_for('index'))
    except Exception as e:
        return str(e)

@app.route('/generate_random_data', methods=['POST'])
def generate_random():
    try:
        generate_random_data()
        return redirect(url_for('index'))
    except Exception as e:
        return str(e)

@app.route('/static/<path:filename>', methods=['GET'])
def download(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

if __name__ == '__main__':
    app.run(debug=True)
