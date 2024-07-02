import textwrap

# Criei funçoes verificadoras para validar a entrada do usuário para cada situaçao

#  Verifica se o email do usuario contem @ e .
def validar_email():
  email = input("Informe o e-mail: ")
  while True:
    if '@' in email and '.' in email:
      return email  
    else: 
      email = input('Digite um email válido: ')

def validar_salario():
  while True:
        salario = input("Informe o salário (Ex.: 1000.00): ")
        try:
            salario_float = float(salario)
            # Verifica se o número tem duas casas decimais
            if '.' in salario and len(salario.split('.')[-1]) == 2:
                return round(salario_float, 2)
            else:
                print('Digite um salário válido com duas casas decimais.')
        except ValueError:
            print('Digite um salário válido.')

#  Verfica se o nome digitado contem apenas letras e substitui os espacos em branco
def validar_nome():
    nome = input("Informe o nome completo: ")
    while True:  
      if nome.replace(' ', '').isalpha():
         return nome.title()
      else:
       nome = input('Digite um nome válido: ')  

#  Verfica se o valor digitado contem apenas letras e substitui os espacos em branco
def validar_cidade():
   cidade = input("Informe a cidade: ").title()
   while True:
      if cidade.replace(' ', '').isalpha():
        return cidade
      else:
        cidade = input('Digite uma cidade válida: ') 

#  Verifica se o valor digita e igual a 2 e maior que zero
def validar_estado():
   estado = input("Informe o UF: ").upper()  
   while True:
    if (len(estado) == 2 and len(estado) > 0) and estado.isalpha():
      return estado 
    else:
       estado = input('Digite uma UF válido (Ex. MG, SP): ')

# Verificar se na idade tem apenas numeros
def validar_idade():
   idade = input("Informe a idade: ")
   while True:
      if idade.isdigit():
        return int(idade)
      else:
        idade = input('Digite uma idade válida: ')

#  Verfica se o valor digitado contem apenas letras e substitui os espacos em branco
def validar_escolaridade():
   escolaridade = input("Informe a escolaridade: ").capitalize()
   while True:
      if escolaridade.replace(' ', '').isalpha():
        return escolaridade
      else:
       escolaridade =  input('Digite uma escolaridade válido: ')

#  Verfica se o valor digitado contem apenas letras e substitui os espacos em branco
def validar_cargo():
   cargo = input("Informe o cargo: ").title()
   while True:
       if cargo.replace(' ', '').isalpha():
        return cargo
       else:
        cargo = input('Digite um cargo válido: ')
   

# Criei uma funçao menu para gerar as opçoes para o usuário

def menu():
    menu = """\n
    ================ MENU ================
    [n]\tNovo funcionário
    [a]\tAtualizar informações
    [l]\tListar funcionário
    [d]\tDeletar funcionário
    [q]\tSair
    => """
    return input(textwrap.dedent(menu))

# Fiz uma função para filtrar apenas os numeros do CPF, ignorando pontos e traços

def somente_numeros(string):
    return ''.join(filter(str.isdigit, string))

#  Para a funçao criar funcionarios, utilizei try except para caso uma informaçao 
#  tenha sido digitada errada parar a execuçao do programa.

def criar_funcionario(usuarios):
    #  Utilizei o CPF como identificador unico
      cpf = input("Informe o CPF (somente número): ")
      cpf_tratado = somente_numeros(cpf)
    # Verifico se o CPF digitado existe na minha base de dados
      usuario = filtrar_usuario(cpf_tratado, usuarios)

      if usuario:
          print("\n@@@ Já existe funcioário com esse CPF! @@@")
          return

      if len(cpf_tratado) <= 11:
            nome = validar_nome()
            cidade= validar_cidade()
            estado = validar_estado()
            idade = validar_idade()
            escolaridade = validar_escolaridade()
            cargo = validar_cargo()
            salario = validar_salario()
            email = validar_email()

            usuarios.append({"cpf": cpf, "nome": nome, "cidade": cidade, "estado": estado, "idade": idade,
              'escolaridade': escolaridade, "cargo": cargo, "salario": salario,
              "email": email })
            
            print("=== Usuário criado com sucesso! ===")
      else:
          print('CPF digitado incorretamente, deve conter 11 numeros.')       

def listar_funcionario(usuarios):
  if len(usuarios) > 0:
    for usuario in usuarios:
        linha = f"""\
            CPF:\t{usuario['cpf']}
            Nome:\t{usuario['nome']}
            Cidade:\t{usuario['cidade']}
            Estado:\t{usuario['estado']}
            Idade:\t{usuario['idade']}
            Escolaridade: {usuario['escolaridade']}
            Cargo:\t{usuario['cargo']}
            Salário: {usuario['salario']}
            E-mail:\t{usuario['email']}
        """

        print(textwrap.dedent(linha))
  else:
    print("Não há funcionários cadastrados.")

def atualizar_funcionario(usuarios):
   print('============Obrigatorio preencher todas as informações============\n')

   cpf = input("Informe o CPF (somente número): ")
   cpf_tratado = somente_numeros(cpf)
   usuario = filtrar_usuario(cpf_tratado, usuarios)

   if usuario:
     try:
        usuario['nome'] = validar_nome()
        usuario['cidade'] = validar_cidade()
        usuario['estado'] = validar_estado()
        usuario['idade'] = validar_idade()
        usuario['escolaridade'] = validar_escolaridade()
        usuario['cargo'] = validar_cargo()
        usuario['salario'] = validar_salario()
        usuario['email'] = validar_email()

        print("Informações atualizadas com sucesso!")
     except ValueError as v:
         print(f"Erro ao atualizar informações: {v}")
     except Exception as e:
         print(f"Ocorreu um erro inesperado: {e}")    
   else:
       print('Usuário não encontrado')

def remover_funcionario(usuarios):
    cpf = input("Informe o CPF (somente número) do funcionário a ser removido: ")
    cpf_tratado = somente_numeros(cpf) 

    funcionario_remover = [u for u in usuarios if u["cpf"] == cpf_tratado ]

    if funcionario_remover:
        usuarios.remove(funcionario_remover[0])
        print("Funcionário removido com sucesso.")
    else:
        print("Funcionário não encontrado.")


def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None


def main():

  usuarios = []

  while True:
    opcao = menu()

    if opcao == 'n':
        criar_funcionario(usuarios)
    elif opcao == 'a':
        atualizar_funcionario(usuarios)
    elif opcao ==  'l':
        listar_funcionario(usuarios)
    elif opcao == 'd':
        remover_funcionario(usuarios)
    elif opcao == "q":
       break
    else:
       print("Opção inválida, por favor selecione novamente a opção desejada.")

main()