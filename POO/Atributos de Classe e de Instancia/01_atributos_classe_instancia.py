#  Todos os objetos nascem com o mesmo número de atributos de classe e de instância. Atributos de instância são diferentes para cada objeto (cada objeto tem uma cópia), 
#  já os atributos de classe são compartilhados entre os objetos.

class Estudante :
  escola = "Nuclio Digital School"

  def __init__(self, nome, matricula):
    self.nome = nome
    self.matricula = matricula
  
  def __str__(self):
    return f"{self.nome} - {self.matricula} - {self.escola}"
  
def exibir_dados_aluno(*objs):
  for obj in objs:
    print(obj)

aluno_1 = Estudante("Rodrigo",  112233)
aluno_2 = Estudante("Fernanda", 223344)
exibir_dados_aluno(aluno_1, aluno_2)

# Atributos de classe infere em todos os objetos criados
Estudante.escola = "Dio"
aluno_3 = Estudante("Sofia", 334455)
exibir_dados_aluno(aluno_1, aluno_2, aluno_3)
