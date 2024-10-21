# URL: https://medium.com/@adilmarcoelhodantas/introdu%C3%A7%C3%A3o-%C3%A0s-%C3%A1rvores-de-decis%C3%A3o-aplica%C3%A7%C3%B5es-e-exemplo-pr%C3%A1tico-com-python-13dccdfb1030


from flask import Flask, request, render_template
app = Flask(__name__)

@app.route("/")
def home():
   print('Log: Show the home.html')
   return render_template('home.html')

@app.route("/knn")
def knn():
   
    # Get the variables from query parameters
    # Ex. url/knn?var1=10&var2=100&var3=1000
    print('Log: Receive var from GET')
    print('Log: Value of K = ', request.args.get('k'))

    # Here put the knn code basead on the vars received
    #



    # Bellow return the resul of the knn code
    return 'Deu certo'

if __name__ == "__main__":
    app.run()

