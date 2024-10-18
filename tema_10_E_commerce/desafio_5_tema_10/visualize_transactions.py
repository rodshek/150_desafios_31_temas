import matplotlib.pyplot as plt
from blockchain import Blockchain


def fetch_transactions(address):
    blockchain = Blockchain()
    transactions = blockchain.address(address).transactions
    return transactions


def visualize_transactions(transactions):
    dates = []
    values = []

    for tx in transactions:
        # Convertendo a data da transação para um formato legível
        dates.append(tx.time.strftime("%Y-%m-%d %H:%M:%S"))
        values.append(tx.value / 10**8)  # Convertendo satoshis para BTC

    plt.figure(figsize=(10, 5))
    plt.plot(dates, values, marker='o', linestyle='-')
    plt.xlabel('Data')
    plt.ylabel('Valor (BTC)')
    plt.title('Histórico de Transações')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    # Substitua 'your_bitcoin_address_here' pelo endereço Bitcoin que você deseja analisar
    address = 'your_bitcoin_address_here'
    transactions = fetch_transactions(address)
    visualize_transactions(transactions)
