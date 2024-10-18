import requests
from bs4 import BeautifulSoup


# Função para fazer scraping e analisar o conteúdo
def scrape_website(url):
    # Fazer uma requisição para a URL
    response = requests.get(url)

    # Verificar se a requisição foi bem-sucedida
    if response.status_code == 200:
        # Criar um objeto BeautifulSoup
        soup = BeautifulSoup(response.text, 'html.parser')

        # Extrair o título da página
        title = soup.title.string

        # Extrair todos os parágrafos
        paragraphs = soup.find_all('p')
        paragraphs_text = [p.get_text() for p in paragraphs]

        print("Título da Página:")
        print(title)
        print("\nParágrafos da Página:")
        for p in paragraphs_text:
            print(p)
    else:
        print(
            f"Falha ao acessar a página. Código de status: {response.status_code}")


if __name__ == '__main__':
    url = 'https://example.com'  # Substitua com a URL que deseja analisar
    scrape_website(url)
