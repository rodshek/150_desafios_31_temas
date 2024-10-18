from bitcoin import *


def verify_transaction(tx_id):
    try:
        # Obtém os detalhes da transação usando o ID
        transaction = history(tx_id)
        if transaction:
            return True
        else:
            return False
    except Exception as e:
        print("Erro ao verificar a transação:", e)
        return False


if __name__ == "__main__":
    # Substitua 'your_tx_id_here' pelo ID da transação que você deseja verificar
    tx_id = 'your_tx_id_here'
    is_valid = verify_transaction(tx_id)

    if is_valid:
        print(f"A transação com ID {tx_id} é válida.")
    else:
        print(
            f"A transação com ID {tx_id} não é válida ou não foi encontrada.")
