from scapy.all import IP, TCP, UDP, sniff


def packet_callback(packet):
    """Função callback para processar pacotes capturados."""
    if IP in packet:
        ip_src = packet[IP].src
        ip_dst = packet[IP].dst
        print(f"Pacote capturado: {ip_src} -> {ip_dst}")

        # Verificar se é um pacote TCP ou UDP e considerar como suspeito se for
        if TCP in packet or UDP in packet:
            print(f"Pacote TCP/UDP detectado: {ip_src} -> {ip_dst}")


def main():
    print("Iniciando a captura de pacotes. Pressione Ctrl+C para parar.")
    # Captura pacotes na interface padrão
    sniff(prn=packet_callback, filter="ip", store=0)


if __name__ == "__main__":
    main()
