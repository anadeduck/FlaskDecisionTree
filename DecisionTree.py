import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.preprocessing import LabelEncoder
import matplotlib.pyplot as plt
import pydotplus
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
def answerDecisionTree(o,t,h,w):
    # Exemplo de uso da função com novos dados simulando um 'NO'
    #new_data = {'outlook': 'sunny', 'temperature': 72, 'humidity': 95, 'wind': 'FALSE'}

    # Exemplo de uso da função com novos dados simulando um 'YES'
    #new_data = {'outlook': 'sunny', 'temperature': 85, 'humidity': 85, 'wind': 'FALSE'}
    new_data = {'outlook': o, 'temperature': t, 'humidity': h, 'wind': w}

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
    print(play_prediction[0])
    result = f"Vai jogar tenis? {'YES' if play_prediction[0] == 'yes' else 'NO'}"

    return result



answerDecisionTree(o='sunny',t='85',h='85',w='FALSE')
