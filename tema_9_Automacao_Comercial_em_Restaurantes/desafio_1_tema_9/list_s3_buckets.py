import boto3
from botocore.exceptions import NoCredentialsError, PartialCredentialsError


def list_s3_buckets():
    try:
        # Cria uma sessão com a AWS
        s3 = boto3.client('s3')

        # Obtém a lista de buckets
        response = s3.list_buckets()

        # Exibe o nome dos buckets
        print("Buckets:")
        for bucket in response['Buckets']:
            print(f"- {bucket['Name']}")

    except NoCredentialsError:
        print("Erro: Credenciais não encontradas. Verifique se você configurou suas credenciais AWS.")
    except PartialCredentialsError:
        print("Erro: Credenciais incompletas. Verifique suas credenciais AWS.")
    except Exception as e:
        print(f"Erro: {e}")


if __name__ == "__main__":
    list_s3_buckets()
