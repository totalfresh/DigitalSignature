from Crypto.Signature import pkcs1_15
from Crypto.Hash import SHA256
from Crypto.PublicKey import RSA

def weryfikuj_podpis(file_path, signature_path, public_key_path, hash_file_path):
    try:
        # Load the public key
        with open(public_key_path, 'rb') as f:
            klucz_publiczny = RSA.import_key(f.read())

        # Load the signature
        with open(signature_path, 'rb') as f:
            podpis = f.read()

        # Load the file and its hash
        with open(file_path, 'rb') as f:
            dane_pliku = f.read()
        with open(hash_file_path, 'r') as f:
            hasz = f.read()

        # Calculate the hash of the file
        obliczony_hasz = SHA256.new(dane_pliku).hexdigest()

        if hasz != obliczony_hasz:
            return "The file hash does not match the provided hash."

        # Verify the signature
        try:
            pkcs1_15.new(klucz_publiczny).verify(SHA256.new(dane_pliku), podpis)
            return "The signature is valid."
        except (ValueError, TypeError):
            return "The signature is invalid."
    except Exception as e:
        return f"An error occurred during verification: {e}"
