import string
import secrets

def main():
    while True:
        print("\n[1] Generar Password (Default)")
        print("[2] Generar Password (Personalizada)")
        print("[0] Salir")
        opcion = int(input("-> "))
        if opcion == 1:
            n = int(input("Indica la longitud de la password: "))
            r = generar_password(n)
            print(f"password -> {r}")
        elif opcion == 2:
            r  = password_personalizada()
            print(f"password -> {r}")
        elif opcion == 0:
            break
        else:
            pass


def generar_password(longitud):
    formato = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(secrets.choice(formato) for _ in range(longitud))
    return password

def password_personalizada():
    num_symbols = int(input("num_special characters: "))
    num_digits = int(input("num _digits: "))
    num_letters = int(input("num_letters: "))

    symbols = ''.join(secrets.choice(string.punctuation) for _ in range(num_symbols))
    digits = ''.join(secrets.choice(string.digits) for _ in range(num_digits))
    letters = ''.join(secrets.choice(string.ascii_letters) for _ in range(num_letters))

    formato = symbols + digits + letters
    longitud = num_symbols + num_digits + num_letters
    
    password = ''.join(secrets.choice(formato) for _ in range(longitud))
    return password


if __name__ == "__main__":
    main()

'# Author: rootvan'