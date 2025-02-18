import json
import os

'''
resultado = contatos.pop("guilherme@gmail.com")  # {'nome': 'Guilherme', 'telefone': '3333-2221'}
print(resultado)

resultado = contatos.pop("guilherme@gmail.com", {})  # {}
print(resultado)

for chave, valor in contatos.items():
    print(chave, valor)



contatos = adicioanr_contato(contatos, "ronald@gmail.com", "Ronald", "3333-2221")
'''






def adicionar_contato(contatos, email, nome, telefone):
    contatos[email] = {"nome": nome, "telefone": telefone}

    return contatos

def remover_contato(contatos, email):
    contatos.pop(email, None)

    return contatos

def salvar_contatos_json(contatos):
    with open("contatos.json", "a") as file:
        file.write(json.dumps(contatos) + "\n")
def criar_diretorio():
    if not os.path.exists("contatos"):
        os.mkdir("contatos")
def main():

    try:
        contatos = {}
        diretorio  = criar_diretorio()
        while True:
            print("1 - Adicionar contato")
            print("2 - Remover contato")
            print("3 - Salvar contatso em JSON")
            print("4 - Sair")

            opcao = input("Escolha uma opção: ")

            if opcao == "1":
                email = input("Digite o email: ")
                nome = input("Digite o nome: ")
                telefone = input("Digite o telefone: ")

                contatos = adicionar_contato(contatos, email, nome, telefone)
            elif opcao == "2":
                email = input("Digite o email: ")

                contatos = remover_contato(contatos, email)

            elif opcao == "3":
                os.chdir(diretorio)
                salvar_contatos_json(contatos)    
            elif opcao == "4":
                break
            else:
                print("Opção inválida")

            print(contatos)     
    except Exception as e:
        print("Ocorreu um erro: ", e)    


if __name__ == "__main__":
    main()