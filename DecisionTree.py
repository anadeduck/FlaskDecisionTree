import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.preprocessing import LabelEncoder
import matplotlib.pyplot as plt
import pydotplus
from IPython.display import Image
from sklearn.tree import export_graphviz

# Carregar os dados do CSV
data = pd.read_csv('tennis.csv')

# Inicializar os codificadores de rótulos para variáveis categóricas
outlook_encoder = LabelEncoder()
wind_encoder = LabelEncoder()
play_encoder = LabelEncoder()

# Codificar as variáveis categóricas
data['outlook'] = outlook_encoder.fit_transform(data['outlook'])
data['wind'] = wind_encoder.fit_transform(data['wind'])
data['play'] = play_encoder.fit_transform(data['play'])

# Exibir os mapeamentos de valores codificados
print("Mapeamento de 'outlook':",
      dict(zip(outlook_encoder.classes_, outlook_encoder.transform(outlook_encoder.classes_))))
print("Mapeamento de 'wind':", dict(zip(wind_encoder.classes_, wind_encoder.transform(wind_encoder.classes_))))
print("Mapeamento de 'play':", dict(zip(play_encoder.classes_, play_encoder.transform(play_encoder.classes_))))

# Separar as características (features) e o rótulo (label)
X = data[['outlook', 'temperature', 'humidity', 'wind']]
y = data['play']

# Dividir os dados em conjunto de treinamento e teste
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Criar o modelo de árvore de decisão
clf = DecisionTreeClassifier()

# Treinar o modelo
clf.fit(X_train, y_train)


# Função para fazer a previsão com novos dados e salvar a árvore de decisão como imagem
def answerDecisionTree():
    # Exemplo de uso da função com novos dados
    new_data = {'outlook': 'sunny', 'temperature': 85, 'humidity': 85, 'wind': 'false'}
    # Converter os novos dados usando os mesmos label encoders treinados
    new_data['outlook'] = outlook_encoder.transform([new_data['outlook']])[0]
    new_data['wind'] = wind_encoder.transform([new_data['wind']])[0]

    # Exibir os valores codificados dos novos dados
    print("Novos dados codificados:", new_data)

    # Converter para DataFrame
    new_data_df = pd.DataFrame([new_data])

    # Fazer a previsão
    prediction = clf.predict(new_data_df)

    # Converter a previsão de volta para o valor original
    play_prediction = play_encoder.inverse_transform(prediction)

    # Exibir o resultado da previsão
    result = f"Vai jogar tênis? {'Sim' if play_prediction[0] == 'yes' else 'Não'}"
    #print(result)

    # Visualizar a árvore de decisão
    #plt.figure(figsize=(20, 10))
    #plot_tree(clf, feature_names=['outlook', 'temperature', 'humidity', 'wind'], class_names=['no', 'yes'], filled=True)
    #plt.show()

    # Exportar a árvore para um arquivo Graphviz e salvar como uma imagem PNG
    #dot_data = export_graphviz(clf, out_file=None,
    #                         feature_names=['outlook', 'temperature', 'humidity', 'wind'],
    #                           class_names=['no', 'yes'],
    #                          filled=True, rounded=True,
    #                           special_characters=True)
    #graph = pydotplus.graph_from_dot_data(dot_data)

    # Salvar a imagem como arquivo PNG
    #graph.write_png("DecisionTreeResult.png")
    #print("A árvore de decisão foi salva como 'DecisionTreeResult.png'.")

    # Exibir a imagem na tela (opcional)
    #display(Image(graph.create_png()))
    #
    return result



answerDecisionTree()
