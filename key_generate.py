from Crypto.PublicKey import RSA
import os

# Function to read data from a binary file
def wczytaj_dane_losowe_z_pliku(nazwa_pliku):
    with open(nazwa_pliku, 'rb') as f:
        dane_binarne = f.read()
    return dane_binarne

# Read random data from file
dane_losowe = wczytaj_dane_losowe_z_pliku('random_data_for_key.bin')
data_index = 0

def funkcja_losowa(n):
    global data_index, dane_losowe
    if data_index + n > len(dane_losowe):
        data_index = 0
        dodatkowe_dane = os.urandom(len(dane_losowe))
        dane_losowe = dane_losowe + dodatkowe_dane
    wynik = dane_losowe[data_index:data_index + n]
    data_index += n
    return wynik

# Function to generate unique filenames
def generate_unique_filename(directory, filename):
    base, extension = os.path.splitext(filename)
    counter = 1
    new_filename = filename
    while os.path.exists(os.path.join(directory, new_filename)):
        new_filename = f"{base}_{counter}{extension}"
        counter += 1
    return new_filename

# Generate RSA keys
try:
    klucz = RSA.generate(2048, e=65537, randfunc=funkcja_losowa)
    klucz_prywatny = klucz.export_key()
    klucz_publiczny = klucz.publickey().export_key()
    
    private_key_filename = generate_unique_filename('static', 'private_key.pem')
    public_key_filename = generate_unique_filename('static', 'public_key.pem')
    
    with open(os.path.join('static', private_key_filename), 'wb') as priv_file:
        priv_file.write(klucz_prywatny)
    with open(os.path.join('static', public_key_filename), 'wb') as pub_file:
        pub_file.write(klucz_publiczny)

    print(f"Keys were generated and saved to '{private_key_filename}' and '{public_key_filename}'.")

except Exception as e:
    print(f"An error occurred while generating the key: {e}")