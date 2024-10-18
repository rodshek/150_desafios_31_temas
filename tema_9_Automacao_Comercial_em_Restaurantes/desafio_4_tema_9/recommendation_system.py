from surprise import SVD, Dataset, Reader, accuracy
from surprise.model_selection import train_test_split


def create_recommendation_system():
    # Carrega o dataset de filmes
    data = Dataset.load_builtin('ml-100k')

    # Define o formato do dataset
    reader = Reader(line_format='user item rating timestamp', sep='\t')

    # Carrega os dados
    data = Dataset.load_from_file('ml-100k/u.data', reader=reader)

    # Divida os dados em conjunto de treinamento e teste
    trainset, testset = train_test_split(data, test_size=0.25)

    # Usa o algoritmo SVD para recomendação
    algo = SVD()
    algo.fit(trainset)

    # Faz previsões sobre o conjunto de teste
    predictions = algo.test(testset)

    # Avalia a precisão das previsões
    accuracy.rmse(predictions)

    return algo


def recommend_movie(algo, user_id, movie_id):
    # Faz uma recomendação para um usuário específico
    prediction = algo.predict(user_id, movie_id)
    print(
        f"Predicted rating for user {user_id} on movie {movie_id}: {prediction.est}")


if __name__ == "__main__":
    algo = create_recommendation_system()

    # Exemplo de recomendação: usuário 196, filme 302
    recommend_movie(algo, '196', '302')
