# Digital Signature

**Polska wersja znajduje się poniżej wersji angielskiej.**

The "Digital Signature" project is a web application that allows generating RSA keys, signing files, generating random data, and verifying digital signatures. The application is written in Python and uses the Flask library for the user interface.

## Requirements

- Python 3.x
- Flask
- PyCryptodome
- NumPy

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/totalfresh/DigitalSignature
    cd Digital-Signature
    ```

2. Install the required libraries:
    ```bash
    pip install -r requirements.txt
    ```

3. Create the `static` directory if it does not exist:
    ```bash
    mkdir static
    ```

## Running the Application

To run the application, follow these steps:

1. Ensure you are in the project's root directory.

2. Start the Flask application:
    ```bash
    python app.py
    ```

3. Open a web browser and go to `http://127.0.0.1:5000/`.

## Features

### Generate Random Data

To generate random data, go to the "Generate Random Data" section and click the "Generate Random Data" button. The random data will be saved in the `static` directory.

### Generate Keys

To generate a pair of RSA keys (private and public), go to the "Generate Key" section and click the "Generate Key" button. The keys will be saved in the `static` directory.

### Sign Files

To sign a file, go to the "Sign File" section, select the file to be signed and the private key, and then click the "Sign" button. The signature file will be saved in the `static` directory.

### Verify Signatures

To verify a file's signature, go to the "Verify Signature" section, select the file, the signature, the public key, and the hash file, and then click the "Verify" button. The verification result will be displayed on the screen.

## Project Structure

- `app.py`: Main Flask application file.
- `sign_file.py`: Script for signing files and generating hashes.
- `verify_signature.py`: Script for verifying signatures.
- `generate_random_data.py`: Script for generating random data.
- `templates/`: Directory containing HTML templates.
- `static/`: Directory for storing generated files (keys, signatures, random data).

## License

This project is licensed under the MIT License. Details can be found in the `LICENSE` file.

## Authors

This project was created by [Your Name]. If you have any questions or comments, please contact me at [Your Email].

---

# Podpis Cyfrowy

Projekt "Podpis Cyfrowy" to aplikacja internetowa umożliwiająca generowanie kluczy RSA, podpisywanie plików, generowanie danych losowych oraz weryfikację podpisów cyfrowych. Aplikacja została napisana w Pythonie i wykorzystuje bibliotekę Flask do obsługi interfejsu użytkownika.

## Wymagania

- Python 3.x
- Flask
- PyCryptodome
- NumPy

## Instalacja

1. Sklonuj repozytorium:
    ```bash
    git clone https://github.com/totalfresh/DigitalSignature
    cd Digital-Signature
    ```

2. Zainstaluj wymagane biblioteki:
    ```bash
    pip install -r requirements.txt
    ```

3. Utwórz katalog `static`, jeśli nie istnieje:
    ```bash
    mkdir static
    ```

## Uruchomienie

Aby uruchomić aplikację, wykonaj następujące kroki:

1. Upewnij się, że znajdujesz się w katalogu głównym projektu.

2. Uruchom aplikację Flask:
    ```bash
    python app.py
    ```

3. Otwórz przeglądarkę internetową i przejdź do adresu `http://127.0.0.1:5000/`.

## Funkcje

### Generowanie danych losowych

Aby wygenerować dane losowe, przejdź do sekcji "Generate Random Data" i kliknij przycisk "Generate Random Data". Dane losowe zostaną zapisane w katalogu `static`.

### Generowanie kluczy

Aby wygenerować parę kluczy RSA (prywatny i publiczny), przejdź do sekcji "Generate Key" i kliknij przycisk "Generate Key". Klucze zostaną zapisane w katalogu `static`.

### Podpisywanie plików

Aby podpisać plik, przejdź do sekcji "Sign File", wybierz plik do podpisania oraz klucz prywatny, a następnie kliknij przycisk "Sign". Plik podpisu zostanie zapisany w katalogu `static`.

### Weryfikacja podpisów

Aby zweryfikować podpis pliku, przejdź do sekcji "Verify Signature", wybierz plik, podpis, klucz publiczny oraz plik z hashem, a następnie kliknij przycisk "Verify". Wynik weryfikacji zostanie wyświetlony na ekranie.

## Struktura projektu

- `app.py`: Główny plik aplikacji Flask.
- `sign_file.py`: Skrypt do podpisywania plików i generowania hashy.
- `verify_signature.py`: Skrypt do weryfikacji podpisów.
- `generate_random_data.py`: Skrypt do generowania danych losowych.
- `templates/`: Katalog z szablonami HTML.
- `static/`: Katalog do przechowywania wygenerowanych plików (klucze, podpisy, dane losowe).

## Licencja

Projekt jest dostępny na licencji MIT. Szczegóły znajdują się w pliku `LICENSE`.

## Autorzy

Projekt został stworzony przez [Twoje Imię]. Jeśli masz pytania lub uwagi, skontaktuj się ze mną poprzez [Twój e-mail].
