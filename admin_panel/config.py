import subprocess
from packaging import version

def update_libraries():
    try:
        subprocess.check_call(["pip", "install", "--upgrade", "-r", "requirements.txt"])
        print("Aktualizacja bibliotek zakończona pomyślnie.")
    except subprocess.CalledProcessError as e:
        print("Błąd podczas aktualizacji bibliotek:", e)

def install_missing_libraries():
    try:
        with open("requirements.txt", "r") as f:
            required_libraries = f.read().splitlines()
        installed_libraries = subprocess.check_output(["pip", "freeze"]).decode("utf-8").split("\n")
        for lib in required_libraries:
            lib_name, lib_version = lib.split("==")
            is_installed = any(lib_name in line for line in installed_libraries)
            if is_installed:
                for line in installed_libraries:
                    if lib_name in line:
                        installed_version = line.split('==')[1]
                        break
                if version.parse(installed_version) >= version.parse(lib_version):
                    print(f"{lib_name} jest już zainstalowane w nowszej wersji.")
                    continue
            subprocess.check_call(["pip", "install", lib])
            print(f"Zainstalowano brakującą bibliotekę: {lib}")
    except Exception as e:
        print("Błąd podczas instalacji brakujących bibliotek:", e)

if __name__ == "__main__":
    print("Wybierz działanie:")
    print("1. Instalacja i aktualizacja")
    print("2. Tylko aktualizacja")
    print("3. Tylko instalacja")

    choice = input("Podaj numer działania: ")

    if choice == "1":
        install_missing_libraries()
        update_libraries()
    elif choice == "2":
        update_libraries()
    elif choice == "3":
        install_missing_libraries()
    else:
        print("Nieprawidłowy wybór.")
