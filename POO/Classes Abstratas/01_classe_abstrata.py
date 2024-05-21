from abc import ABC, abstractmethod

class RemoteControl(ABC):
  @abstractmethod
  def ligar(self):
    pass

  @abstractmethod
  def desligar(self):
    pass

  @property
  def marca(self):
    pass
  

class TVControl(RemoteControl):  
  def ligar(self):
    print("Ligando a TV...")
    print("TV ligada")

  def desligar(self):
    print("Desligando a TV...")
    print("TV Desligada")

  @property
  def marca(self):
    return "Marca do Controle: LG"


class ControleArCondicionado(RemoteControl):
    def ligar(self):
      print("Ligando o ar condicionado...")
      print("Ligado!!!")

    def desligar(self):
      print("Desligando o ar condicionado ...")
      print("Desligado!!!")

    @property
    def marca(self):
      return "Marca do Controle: LG"

controle = TVControl()
controle.ligar()
controle.desligar()
print(controle.marca)

controle_ar = ControleArCondicionado()
controle_ar.ligar()
controle_ar.desligar()
print(controle_ar.marca)