class Pessoa:
  def __init__(self, nome, idade):
    self.nome = nome 
    self.idade = idade
  
  @classmethod
  def calculo_idade(cls, ano, mes, dia, nome):
    idade = 2024 - ano
    return cls(nome, idade)
  
  @staticmethod
  def maior_idade(idade):
    return idade >= 18
  
p = Pessoa.calculo_idade(1985, 11, 3, "Rodrigo")
print(p.nome, p.idade)

print(Pessoa.maior_idade(p.idade))