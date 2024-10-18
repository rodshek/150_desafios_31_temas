from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer


def create_chatbot():
    # Cria uma instância do chatbot
    chatbot = ChatBot('SimpleBot')

    # Configura o treinamento usando o corpus padrão
    trainer = ChatterBotCorpusTrainer(chatbot)
    trainer.train('chatterbot.corpus.english')

    return chatbot


def chat_with_bot(chatbot):
    print("Olá! Eu sou o SimpleBot. Pergunte-me qualquer coisa!")
    while True:
        try:
            # Recebe a entrada do usuário
            user_input = input("Você: ")
            if user_input.lower() == 'sair':
                print("Adeus!")
                break

            # Obtém a resposta do chatbot
            response = chatbot.get_response(user_input)
            print("Bot:", response)
        except (KeyboardInterrupt, EOFError, SystemExit):
            break


if __name__ == "__main__":
    bot = create_chatbot()
    chat_with_bot(bot)
