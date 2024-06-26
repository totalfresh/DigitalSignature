from Crypto.Signature import pkcs1_15
from Crypto.Hash import SHA256
from Crypto.PublicKey import RSA
import os

# Function to generate unique filenames
def generate_unique_filename(directory, filename):
    base, extension = os.path.splitext(filename)
    counter = 1
    new_filename = filename
    while os.path.exists(os.path.join(directory, new_filename)):
        new_filename = f"{base}_{counter}{extension}"
        counter += 1
    return new_filename

def podpisz_plik(nazwa_pliku, sciezka_klucza_prywatnego):
    # Load the private key
    with open(sciezka_klucza_prywatnego, 'rb') as f:
        klucz_prywatny = RSA.import_key(f.read())

    # Load data from the file
    with open(nazwa_pliku, 'rb') as f:
        dane_pliku = f.read()

    # Hash the file data
    hasz = SHA256.new(dane_pliku)

    # Sign the hash
    podpis = pkcs1_15.new(klucz_prywatny).sign(hasz)

    # Generate a unique filename for the signature
    podpis_filename = generate_unique_filename('static', 'signature.sig')
    podpis_file_path = os.path.join('static', podpis_filename)

    # Save the signature to a file
    with open(podpis_file_path, 'wb') as f:
        f.write(podpis)

    print(f"File '{nazwa_pliku}' was successfully signed as '{podpis_file_path}'.")
    return podpis

def zhaszuj_plik(nazwa_pliku):
    # Load data from the file
    with open(nazwa_pliku, 'rb') as f:
        dane_pliku = f.read()

    # Hash the file data
    hasz = SHA256.new(dane_pliku)

    # Generate a unique filename for the hash
    hash_filename = 'Hash.txt'
    hash_file_path = os.path.join('static', hash_filename)

    # Save the hash to a file
    with open(hash_file_path, 'w') as f:
        f.write(hasz.hexdigest())

    print(f"Hash of file '{nazwa_pliku}' was saved as '{hash_file_path}'.")
    return hasz.hexdigest()