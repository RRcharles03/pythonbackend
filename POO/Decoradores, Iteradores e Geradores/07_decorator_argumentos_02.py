def meu_decorador(funcao):
    def envelope(*args, **kwargs):
      print('Faz algo antes de executar')
      resultado = funcao(*args, **kwargs)
      print('Faz algo depois de executar')
      return resultado
  
    return envelope

@meu_decorador
def ola_mundo(nome):
    print(f'Olá {nome}!!')
    return nome.upper()

resultado = ola_mundo("Rodrigo")
print(resultado)