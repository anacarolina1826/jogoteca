from flask import Flask, render_template, request, redirect,session,flash,url_for,abort
import usuarios

class jogo:

    def __init__ (self,nome,categoria,console):
        self.nome =nome
        self.categoria=categoria
        self.console= console

jogo1= jogo('God of War','ação','playstation')
jogo2=jogo('CS:GO','Tiro','PC')
jogo3=jogo('Minecraft', 'construção','PC')


app = Flask(__name__)
app.secrety_key='ifmg'

lista = [jogo1, jogo2, jogo3]
#exibir a tabela com meus jogos
@app.route('/')
def ola():
    return render_template('lista.html',titulo='Meus Jogos', jogos=lista)

  
  #rota: Exibir o formulario para cadstro de novo jogo
@app.route('/novo')
def novo():
  if not usuario_logado():
    return 'usuario_nome' in session
  
  return render_template('novo.html')

  

@app.route('/criar', methods=['POST',])
def criar():
  if not usuario_logado():
    abort(403)
  
  nome = request.form['nome']
  categoria = request.form['categoria']
  console = request.form['console']
  
  novo_jogo = jogo(nome, categoria, console)
  lista.append(novo_jogo)
  
  return render_template('lista.html',titulo='Meus Jogos', jogos=lista)

  
# fazer verivicação dos usuarios e senha e ver se o usuario está cadastrado na sessão ou não  
@app.route('/login', methods=['GET', 'POST'])
def login():
  if request.method == 'POST':
    email = request.form['email']
    senha = request.form['senha']
    usuario = usuarios.buscar(email, senha)
    if usuario is None:
      flash('Usuário/senha inválidos.')
    else:
      session['usuario_email'] = usuario.email
      session['usuario_nome'] = usuario.nome
      return redirect(url_for('index'))
      
  return render_template('login.html')

@app.route('/logout', methods=['POST'])
def logout():
  session.pop('usuario_email', None) #sension.pop ele retira as informações que está na sensão fazendo o logout 
  session.pop('usuario_nome', None)
  return redirect(url_for('index')) 

def usuario_logado():
    return 'usuario_email' in session

@app.errorhandler(403)
def acesso_negado(erro):
  return render_template('acesso_negado.html', titulo='Ops!'), 403



#app.run coloca o sistema no ar, sendo a ultima linha do c
app.run(host='0.0.0.0', port=81, debug=True)