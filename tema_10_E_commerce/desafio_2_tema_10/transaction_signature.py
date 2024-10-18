import hashlib

import ecdsa


def create_transaction(sender, recipient, amount):
    transaction = f"Sender: {sender}, Recipient: {recipient}, Amount: {amount}"
    return transaction


def sign_transaction(private_key, transaction):
    # Cria o objeto de chave privada
    signing_key = ecdsa.SigningKey.from_string(
        private_key, curve=ecdsa.SECP256k1)

    # Cria um hash da transação
    transaction_hash = hashlib.sha256(transaction.encode()).digest()

    # Assina o hash da transação
    signature = signing_key.sign(transaction_hash)

    return signature


def verify_signature(public_key, transaction, signature):
    # Cria o objeto de chave pública
    verifying_key = ecdsa.VerifyingKey.from_string(
        public_key, curve=ecdsa.SECP256k1)

    # Cria um hash da transação
    transaction_hash = hashlib.sha256(transaction.encode()).digest()

    # Verifica a assinatura
    try:
        verifying_key.verify(signature, transaction_hash)
        return True
    except ecdsa.BadSignatureError:
        return False


if __name__ == "__main__":
    sender = input("Digite o endereço do remetente: ")
    recipient = input("Digite o endereço do destinatário: ")
    amount = input("Digite o valor da transação: ")

    # Gerar chave privada e pública para demonstração
    signing_key = ecdsa.SigningKey.generate(curve=ecdsa.SECP256k1)
    private_key = signing_key.to_string()
    public_key = signing_key.get_verifying_key().to_string()

    transaction = create_transaction(sender, recipient, amount)
    signature = sign_transaction(private_key, transaction)

    print("Transação:", transaction)
    print("Assinatura:", signature.hex())

    # Verificação
    is_valid = verify_signature(public_key, transaction, signature)
    print("A assinatura é válida?", is_valid)
