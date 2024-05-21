class Pessoa:
  def __init__(self, nome, ano_nascimento):
    self.nome = nome
    self._ano_nascimento = ano_nascimento

  
  @property
  def idade(self):
    _ano_atual = 2024
    return _ano_atual - self._ano_nascimento

pessoa = Pessoa('Rodrigo', 1985)
print(f"Nome: {pessoa.nome} \tIdade: {pessoa.idade}")

# num1 = int(input());
# num2 = int(input());
# op=str(input());

# def calculadora(op,num1,num2):
#   if op=="sub":
#     resultado= num1 - num2
#   elif op=="ad":
#     resultado = num1 + num2
#   else: 
#     resultado = "Operaçao nao encontrada"
#   return resultado

# print(calculadora(op, num1,num2))
