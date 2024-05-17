class Bicicleta:
  def __init__ (self, cor, modelo, ano , valor):
        self.cor = cor
        self.modelo = modelo
        self.ano = ano
        self.valor = valor
  
  def buzinar(self):
      print("Plim Plim ...")
  
  def parar(self):
      print("Parando bicicleta...")
      print("Bicicleta parada!")
  
  def correr(self):
      print("Vrummmmmm...")
  
  def __str__(self):
      return f"{self.__class__.__name__}: {', '.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}"

b1 = Bicicleta("vermelho", "caloi", 2022, 600);
b1.buzinar();
b1.correr();
b1.parar();

print(b1);

b2 = Bicicleta("verde", "monark", 2000, 200);
Bicicleta.buzinar(b2); # e equivalente a b2.buzinar()
print(b2)