from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Lista para armazenar informações dos veículos no estacionamento
veiculos = []

@app.route('/')
def index():
    return render_template('index.html', veiculos=veiculos)

@app.route('/cadastrar', methods=['POST'])
def cadastrar():
    cor = request.form['cor']
    placa = request.form['placa']
    motorista = request.form['motorista']
    horas_estacionado = int(request.form['horas'])

    # Calculando o preço (R$ 5 por hora)
    preco = horas_estacionado * 5

    # Adicionando o veículo à lista
    veiculo = (cor, placa, motorista, horas_estacionado, preco)
    veiculos.append(veiculo)
    
    return redirect(url_for('index'))

@app.route('/total')
def total():
    total_arrecadado = sum(veiculo[4] for veiculo in veiculos)
    return render_template('index.html', veiculos=veiculos, total=total_arrecadado)

if __name__ == '__main__':
    app.run(debug=True)
