arquivo = open('D:\Cursos de Programaçao\dio\pythonbackend\pythonbackend\POO\Manipulando Arquivos\pixar.txt', 'r')

#  utilizando o readlines com for.

# for linha in arquivo.readlines():
#   print(linha)

print(arquivo.read())
print(arquivo.readline())
print(arquivo.readlines())

# # tip
# while len(linha := arquivo.readline()):
#   print(linha)
  
arquivo.close()