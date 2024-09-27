from flask import Flask, request

from src.calculator import Calculator

app = Flask(__name__)

@app.route("/")
def index():
    return "Bienvenido! Esta aplicación ayuda a elevar números a sus potencias."

@app.route("/hola")
def hola():
    nombre = request.args.get("nombre", "Mundo")
    return f"Hola {nombre}!"

@app.route("/cuadrado")
def cuadrado():
    numero = float(request.args.get("numero", 0))
    calculadora = Calculator()
    return f"El cuadrado de {numero} es {calculadora.cuadrado(numero)}"

@app.route("/cubo")
def cubo():
    numero = float(request.args.get("numero", 0))
    calculadora = Calculator()
    return f"El cubo de {numero} es {calculadora.cubo(numero)}"

if __name__ == "__main__":
    app.run(debug=True)