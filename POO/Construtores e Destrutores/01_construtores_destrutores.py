class Cachorro:
    def __init__(self, nome, cor, acordado=True):
        print("Inicializando a classe")
        self.nome = nome
        self.cor = cor
        self.acordado = acordado
    
    def __del__(self):
        print("Removendo a instancia da classe...")

    def falar(self):
        print("Auau")

def criar_chachorro():
    c = Cachorro("Zeus", "Branco e Preto", False)
    print(c.nome)
      
c = Cachorro("Chappie", "Amarelo")
c.falar()

# a palavra reservada del força o destrutor

del c 