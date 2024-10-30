# URL: https://medium.com/@adilmarcoelhodantas/introdu%C3%A7%C3%A3o-%C3%A0s-%C3%A1rvores-de-decis%C3%A3o-aplica%C3%A7%C3%B5es-e-exemplo-pr%C3%A1tico-com-python-13dccdfb1030
import DecisionTree
from flask import Flask, request, render_template, jsonify

from DecisionTree import answerDecisionTree

app = Flask(__name__)

@app.route("/")
def home():
    print('Log: Show the home.html')
    return render_template('home.html')

@app.route("/Jogartenis", methods=["POST"])
def Jogartenis():
    # Captura os parâmetros enviados pelo formulário (método POST)
    # 'outlook': o, 'temperature': t, 'humidity': h, 'wind', w
    print('Log: Receive var from POST')
    print('Log: Value of o = ', request.form.get("o"))
    o = request.form.get("o")
   
    print('Log: Value of t = ', request.form.get("t"))
    t = request.form.get("t")

    print('Log: Value of h = ', request.form.get("h"))
    h = request.form.get("h")
   
    print('Log: Value of w = ', request.form.get("w"))
    w = request.form.get("w")

    result = answerDecisionTree(o,t,h,w)


    # Aqui você pode inserir o código da árvore de decisão baseado nas variáveis recebidas
    # Exemplo de processamento

    # Abaixo retorna o resultado da execução da árvore de decisão
    return jsonify({"result": result})

if __name__ == "__main__":
    app.run()

