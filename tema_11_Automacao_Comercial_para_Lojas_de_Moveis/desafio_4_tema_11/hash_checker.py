import hashlib


def hash_file(file_path, algorithm='md5'):
    """Gera o hash de um arquivo usando o algoritmo especificado (md5 ou sha256)."""
    hash_algo = hashlib.md5() if algorithm == 'md5' else hashlib.sha256()
    try:
        with open(file_path, 'rb') as file:
            while chunk := file.read(8192):
                hash_algo.update(chunk)
        return hash_algo.hexdigest()
    except FileNotFoundError:
        print(f"Arquivo não encontrado: {file_path}")
        return None


def main():
    file_path = 'example.txt'  # Altere para o caminho do seu arquivo

    # Calculando o hash MD5
    md5_hash = hash_file(file_path, 'md5')
    if md5_hash:
        print(f"MD5 Hash: {md5_hash}")

    # Calculando o hash SHA-256
    sha256_hash = hash_file(file_path, 'sha256')
    if sha256_hash:
        print(f"SHA-256 Hash: {sha256_hash}")


if __name__ == "__main__":
    main()
