class Usuario:
  Def _init_(self, nome, email, senha)
    self.nome = Nome
    self.email = email
    self.senha = senha
lista_usuarios = [
  Usuario('Daniel', 'daniel@gmail.com', '123'),
  Usuario('Natasha', 'natasha@gmail.com', 'abc')
]

dict_usuarios = {
  usuario.email: usuario for usuario in lista_usuarios
}

def buscar(email, senha):
  usuario = dict_usuarios.get(email)
  if usuario != None and usuario.senha == senha:
    return usuario
  else:
    return None