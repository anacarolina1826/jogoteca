from flask import Flask, render_template

class jogo:

    def __init__ (self,nome,categoria,console):
        self.nome =nome
        self.categoria=categoria
        self.console= console

jogo1= jogo('God of War','ação','playstation')
jogo2=jogo('CS:GO','Tiro','PC')
jogo3=jogo('Minecraft', 'construção','PC')
jogo4=jogo('Chatlinx','RPG','Android')


app = Flask(__name__)

lista = [jogo1, jogo2, jogo3]

@app.route('/inicio')
def ola():
    return render_template('lista.html',titulo='Meus Jogos', jogos=lista)

app.run()
