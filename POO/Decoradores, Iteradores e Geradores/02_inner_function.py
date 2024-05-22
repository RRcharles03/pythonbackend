def principal():
  print("Executando a funçao principal")

  def funcao_interna():
    print("Executando a funcao interna")

  def funcao_2():
    print('Executando a funcao 2')
  
  funcao_interna()
  funcao_2()

principal()