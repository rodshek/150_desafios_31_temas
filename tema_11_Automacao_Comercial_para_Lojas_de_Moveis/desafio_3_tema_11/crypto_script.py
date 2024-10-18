from cryptography.fernet import Fernet


# Geração da chave
def generate_key():
    key = Fernet.generate_key()
    with open("secret.key", "wb") as key_file:
        key_file.write(key)
    print("Chave gerada e salva como 'secret.key'.")

# Carregamento da chave


def load_key():
    return open("secret.key", "rb").read()

# Criptografar uma mensagem


def encrypt_message(message):
    key = load_key()
    f = Fernet(key)
    encrypted_message = f.encrypt(message.encode())
    return encrypted_message

# Descriptografar uma mensagem


def decrypt_message(encrypted_message):
    key = load_key()
    f = Fernet(key)
    decrypted_message = f.decrypt(encrypted_message).decode()
    return decrypted_message


def main():
    generate_key()  # Execute uma vez para gerar a chave
    original_message = "Este é um segredo muito importante!"
    print(f"Mensagem original: {original_message}")

    encrypted_message = encrypt_message(original_message)
    print(f"Mensagem criptografada: {encrypted_message}")

    decrypted_message = decrypt_message(encrypted_message)
    print(f"Mensagem descriptografada: {decrypted_message}")


if __name__ == "__main__":
    main()
