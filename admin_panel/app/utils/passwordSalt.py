import hashlib
import os
"""
Rejestracja:

Użytkownik podaje hasło.
Generowana jest unikalna sól.
Sól jest łączona z podanym przez użytkownika hasłem, a wynik jest haszowany.
Haszowane hasło i sól są zapisywane w bazie danych.
Logowanie:

Użytkownik podaje hasło podczas próby logowania.
Z bazy danych pobierane są zapisane haszowane hasło i sól dla danego użytkownika.
Pobrane hasło podane przez użytkownika jest łączone z pobraną solą, a wynik jest ponownie haszowany.
Haszowane hasło uzyskane od użytkownika jest porównywane z zapisanym w bazie danych hasłem.
Jeżeli hasła są identyczne, logowanie jest uznawane za udane.

Ważne jest, aby używać unikalnej soli dla każdego użytkownika, co zwiększa bezpieczeństwo systemu. Ponadto, 
zalecane jest stosowanie bardziej zaawansowanych funkcji haszujących, takich jak bcrypt, zamiast prostych 
funkcji, na przykład SHA-256, ze względu na dodatkowe zabezpieczenia przed atakami bruteforce 
i atakami na tzw. "rainbow tables".
"""
def generate_salt():
    # Generowanie unikalnej soli
    return os.urandom(16).hex()

def hash_password(password, salt):
    # Łączenie hasła z solą i hashowanie
    hashed_password = hashlib.sha256((password + salt).encode()).hexdigest()
    return hashed_password

if __name__ == "__main__":
    # Przykładowe dane z formularza
    login = "example_user"
    password_from_user = "123"

    # Generowanie soli
    salt = generate_salt()

    # Haszowanie hasła z użyciem soli
    hashed_password = hash_password(password_from_user, salt)

    # Symulacja zapisu do bazy danych
    # W rzeczywistym przypadku zamiast print użyj odpowiednich instrukcji SQL
    print(f"Login: {login}")
    print(f"Hashed Password: {hashed_password}")
    print(f"Salt: {salt}")

    # Symulacja odczytu z bazy danych
    # Zakładając, że masz dostęp do bazy danych i otrzymujesz dane z bazy
    # Tutaj również zamiast print użyj odpowiednich instrukcji SQL
    # W rzeczywistym przypadku odczytaj 'hashed_password' i 'salt' dla danego użytkownika
    # Następnie porównaj hasło wprowadzone przez użytkownika z zapisanym 'hashed_password'
    # przy użyciu tej samej soli, aby zweryfikować hasło
