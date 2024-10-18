from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer


def create_and_train_chatbot():
    # Cria um chatbot
    chatbot = ChatBot('SimpleBot')

    # Cria um treinador para o chatbot
    trainer = ChatterBotCorpusTrainer(chatbot)

    # Treina o chatbot com o corpus em inglês
    trainer.train('chatterbot.corpus.english')

    return chatbot


def chat_with_bot(chatbot):
    print("Olá! Eu sou o SimpleBot. Pergunte-me algo.")
    while True:
        try:
            user_input = input("Você: ")
            if user_input.lower() in ['exit', 'quit']:
                print("Adeus!")
                break

            response = chatbot.get_response(user_input)
            print(f"Bot: {response}")

        except (KeyboardInterrupt, EOFError, SystemExit):
            break


if __name__ == "__main__":
    chatbot = create_and_train_chatbot()
    chat_with_bot(chatbot)
