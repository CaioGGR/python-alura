import os

def exibir_nome():
  print("""

█▀ ▄▀█ █▄▄ █▀█ █▀█   █▀▀ ▀▄▀ █▀█ █▀█ █▀▀ █▀ █▀
▄█ █▀█ █▄█ █▄█ █▀▄   ██▄ █░█ █▀▀ █▀▄ ██▄ ▄█ ▄█
      
""")

def exibir_opcoes():
  print('1. Cadastrar restaurante')
  print('2. Listar restaurante')
  print('3. Ativar restaurante')
  print('4. Sair\n')

def finalizar_app():
  os.system('cls')
  print('Finalizando o app\n')

def escolher_opcao():
  opcao = int(input('Escolha uma opcao: '))

  if opcao == 1:
    print('Cadastrar restaurante')
  elif opcao == 2:
    print('Listar restaurante')
  elif opcao == 3:
    print('Ativar restaurante')
  else:
    finalizar_app()

def main():
    exibir_nome()
    exibir_opcoes()
    escolher_opcao()
    
if __name__ == '__main__': # primeira execucao do codigo
    main()