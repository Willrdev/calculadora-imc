from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calcular_imc', methods=['POST'])
def calcular_imc():
    nome = request.form['nome']
    peso = float(request.form['peso'])
    altura = float(request.form['altura'])

    imc = peso / (altura * altura) 

    if imc < 18.5:
        mensagem = 'Você está abaixo do peso'
        classe_mensagem = 'mensagem-alerta'
    elif imc < 25:
        mensagem = 'Você está com peso normal'
        classe_mensagem = 'mensagem-normal'
    elif imc < 30:
        mensagem = 'Você está com sobrepeso'
        classe_mensagem = 'mensagem-alerta'
    else:
        mensagem = 'Você está com obesidade'
        classe_mensagem = 'mensagem-risco'

    return render_template(
        'index.html',
        nome=nome,
        imc=imc,
        mensagem=mensagem,
        classe_mensagem=classe_mensagem
    )

if __name__ == '__main__':
    app.run(debug=True)
