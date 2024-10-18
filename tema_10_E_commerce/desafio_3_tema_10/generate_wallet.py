from bitcoin import *


def generate_wallet():
    # Gera uma nova chave privada
    private_key = random_key()

    # Deriva a chave pública da chave privada
    public_key = privkey_to_pubkey(private_key)

    # Gera o endereço Bitcoin a partir da chave pública
    address = pubkey_to_address(public_key)

    return private_key, public_key, address


if __name__ == "__main__":
    private_key, public_key, address = generate_wallet()

    print("Chave Privada:", private_key)
    print("Chave Pública:", public_key)
    print("Endereço Bitcoin:", address)
