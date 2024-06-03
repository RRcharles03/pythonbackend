import csv
from pathlib import Path

ROOT_PATH = Path(__file__).parent

#  Para criar arquivo
# try:
#     with open(ROOT_PATH / 'titanic.csv', 'w', encoding='utf-8') as arquivo:
#        escritor = csv.writer(arquivo)
#        escritor.writerow(["PassengerId", "Survived","Pclass","Name","Sex","Age","SibSp","Parch","Ticket","Fare","Cabin","Embarked"])
#        escritor.writerow(["1", "0","3","Maria","Female","A35ge","22S","7.25","","","",""])
# except IOError as exc:
#   print("Erro ao criar o arquivo")

#  Leitura de arquivo
try:
    with open(ROOT_PATH / 'titanic.csv', newline="") as csvfile:
       reader = csv.DictReader(csvfile)
       for row in reader:
          print(f'Passanger Id: {row['PassengerId']}')
          print(f'Sobreviveu: {row['Survived']}')
          print(f'Classe: {row['Pclass']}')
          print(f'Nome: {row['Name']}')
except IOError as exc:
  print(f"Erro ao criar o arquivo. {exc}")