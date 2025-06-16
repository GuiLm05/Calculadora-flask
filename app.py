from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)
app.secret_key ='12345'

def conectar_db():
    conectar = sqlite3.connect('calculos.db')
    return conectar 


def criar_tabela():
    conectar = conectar_db()
    cursor = conectar.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS historico (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            operacao TEXT NOT NULL
        )
    ''')
    conectar.commit()
    conectar.close()

def buscar_historico():
    conectar = conectar_db()
    cursor = conectar.cursor()
    cursor.execute('SELECT operacao FROM historico ORDER BY id DESC')
    historico = cursor.fetchall()
    conectar.close()
    return historico

@app.route('/apagar', methods=['POST'])
def apagar_historico():
    conectar = conectar_db()
    cursor = conectar.cursor()
    cursor.execute('DELETE FROM historico')
    conectar.commit()
    conectar.close()
    return render_template('index.html', resultado=None, historico=buscar_historico())


@app.route('/')
def index():
    return render_template('index.html', resultado=None, historico=buscar_historico())


@app.route('/calcular', methods=['POST'])
def calcular():
    num1 = request.form.get('num1', type=int)
    num2 = request.form.get('num2', type=int)
    operacao = request.form.get('operacao')

    if operacao == 'soma':
        resultado = num1 + num2
    elif operacao == 'subtracao':
        resultado = num1 - num2
    elif operacao == 'multiplicacao':
        resultado = num1 * num2
    elif operacao == 'divisao':
        resultado = num1 / num2
    elif operacao == 'potencia':
        resultado = num1 ** num2
    else:
        resultado = None

    simbolos = {
        'soma': '+',
        'subtracao': '-',
        'multiplicacao': '*',
        'divisao': '/',
        'potencia': '**'
    }
    texto = f"{num1} {simbolos.get(operacao, '?')} {num2} = {resultado}"

    conectar = conectar_db()
    cursor = conectar.cursor()
    cursor.execute('INSERT INTO historico (operacao) VALUES (?)', (texto,))
    conectar.commit()
    conectar.close()

    return render_template('index.html', resultado=resultado, historico=buscar_historico())

if __name__ == '__main__':
    criar_tabela()
    app.run(debug=True)
