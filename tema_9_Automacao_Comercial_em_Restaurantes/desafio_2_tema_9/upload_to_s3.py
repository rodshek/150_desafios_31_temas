import os

import boto3
from botocore.exceptions import NoCredentialsError, PartialCredentialsError


def upload_file_to_s3(file_name, bucket_name, object_name=None):
    if object_name is None:
        object_name = os.path.basename(file_name)

    s3 = boto3.client('s3')

    try:
        s3.upload_file(file_name, bucket_name, object_name)
        print(
            f"Arquivo '{file_name}' carregado com sucesso para o bucket '{bucket_name}' com o nome '{object_name}'.")
    except FileNotFoundError:
        print(f"Erro: O arquivo '{file_name}' não foi encontrado.")
    except NoCredentialsError:
        print("Erro: Credenciais não encontradas. Verifique se você configurou suas credenciais AWS.")
    except PartialCredentialsError:
        print("Erro: Credenciais incompletas. Verifique suas credenciais AWS.")
    except Exception as e:
        print(f"Erro: {e}")


if __name__ == "__main__":
    # Substitua os valores abaixo pelos seus próprios
    file_name = 'caminho/para/seu/arquivo.txt'
    bucket_name = 'seu-bucket'
    object_name = 'backup/arquivo.txt'  # Opcional: nome do arquivo no S3

    upload_file_to_s3(file_name, bucket_name, object_name)
