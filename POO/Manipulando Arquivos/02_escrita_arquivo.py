arquivo = open("D:\Cursos de Programaçao\dio\pythonbackend\pythonbackend\POO\Manipulando Arquivos\manipulando_arquivo.txt", 'w')

arquivo.write('Escrevendo dados em um novo arquivo.')
arquivo.writelines([' Escrevendo ', 'um ', 'novo ', 'texto '])
arquivo.close()