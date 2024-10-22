# URL: https://medium.com/@adilmarcoelhodantas/introdu%C3%A7%C3%A3o-%C3%A0s-%C3%A1rvores-de-decis%C3%A3o-aplica%C3%A7%C3%B5es-e-exemplo-pr%C3%A1tico-com-python-13dccdfb1030
from flask import Flask, request, render_template
app = Flask(__name__)

@app.route("/")
def home():
    print('Log: Show the home.html')
    return render_template('home.html')

@app.route("/decisionTree", methods=["POST"])
def decisionTree():
    # Captura os parâmetros enviados pelo formulário (método POST)
    print('Log: Receive var from POST')
    print('Log: Value of K = ', request.form.get("k"))

    # Aqui você pode inserir o código da árvore de decisão baseado nas variáveis recebidas
    # Exemplo de processamento

    # Abaixo retorna o resultado da execução da árvore de decisão
    return 'Deu certo'

if __name__ == "__main__":
    app.run()

