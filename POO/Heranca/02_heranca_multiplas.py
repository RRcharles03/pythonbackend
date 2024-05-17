class Animal:
  def __init__(self, nro_patas):
    self.nro_patas = nro_patas

  def __str__(self):
      return f"{self.__class__.__name__}: {', '.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}"


class Ave(Animal):
    def __init__(self, cor_bico, **kw):
      self.cor_bico = cor_bico
      super().__init__(**kw)

class Mamifero(Animal):
    def __init__(self, cor_pelo, **kw):
      self.cor_pelo = cor_pelo
      super().__init__(**kw)


class Chachorro(Mamifero):
   pass

class Gato(Mamifero):
   pass

class Leao(Mamifero):
  pass

class Ornitorrinco(Mamifero, Ave):
  pass

gato = Gato(nro_patas=4, cor_pelo='Azul Russo')
print(gato)

ornitorrinco = Ornitorrinco(nro_patas=2, cor_pelo='Marron', cor_bico='Castanho')
print(ornitorrinco)

# class Foo:
#     def hello(self):
#         print(self.__class__.__name__.lower())


# class Bar(Foo):
#     def hello(self):
#         return super().hello()


# bar = Bar()
# bar.hello()