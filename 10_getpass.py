import getpass as gtp

usuario = input("Nome de usuário: ")
senha = gtp.getpass("Digite sua senha: ")

if len(senha) >= 6:
    print("Usuário cadastrado com sucesso")
else: 
    print("Atenção, a senha deve ter no mínimo 6 digitos!")