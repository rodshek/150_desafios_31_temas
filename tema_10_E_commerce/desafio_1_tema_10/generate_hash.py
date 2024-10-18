import hashlib


def generate_hash(data, hash_algorithm='sha256'):
    # Cria um objeto hash com o algoritmo especificado
    hash_object = hashlib.new(hash_algorithm)

    # Atualiza o objeto hash com os dados
    hash_object.update(data.encode())

    # Retorna o hash em formato hexadecimal
    return hash_object.hexdigest()


if __name__ == "__main__":
    data = input("Digite os dados para gerar o hash: ")
    hash_algorithm = input(
        "Digite o algoritmo de hash (por exemplo, 'sha256', 'md5'): ").strip().lower()

    try:
        hash_value = generate_hash(data, hash_algorithm)
        print(f"Hash ({hash_algorithm}): {hash_value}")
    except ValueError as e:
        print(f"Erro: {e}")
