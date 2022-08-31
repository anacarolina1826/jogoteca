from flask import Flask, render_template, request

class jogo:

    def __init__ (self,nome,categoria,console):
        self.nome =nome
        self.categoria=categoria
        self.console= console

jogo1= jogo('God of War','ação','playstation')
jogo2=jogo('CS:GO','Tiro','PC')
jogo3=jogo('Minecraft', 'construção','PC')


app = Flask(__name__)

lista = [jogo1, jogo2, jogo3]

@app.route('/')
def ola():
    return render_template('lista.html',titulo='Meus Jogos', jogos=lista)
  
@app.route('/novo')
def novo():
  return render_template('novo.html')

@app.route('/criar', methods=['POST',])
def criar():
  nome = request.form['nome']
  categoria = request.form['categoria']
  console = request.form['console']
  
  novo_jogo = jogo(nome, categoria, console)
  lista.append(novo_jogo)
  
  return render_template('lista.html',titulo='Meus Jogos', jogos=lista)


app.run(host='0.0.0.0', port=81, debug=True)

