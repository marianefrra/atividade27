# Você está organizando um churrasco e precisa gerenciar a lista de convidados. Crie um programa em Python que:

    # Solicite ao usuário que insira o nome de até 7 convidados.
    # Armazene os nomes em uma lista.
    # Permita ao usuário remover um convidado da lista, caso necessário.
    # Exiba a lista final de convidados.

    # Digite o nome do convidado 1: João
    # Digite o nome do convidado 2: Maria
    # ...
    # Digite o nome do convidado 7: Pedro
    # Deseja remover algum convidado da lista? (sim/não): sim
    # Digite o nome do convidado a ser removido: Maria

usuarios = []

for i in range(1,8):
    usuarios.append(str(input("Digite seus convidados: ")))
remover = str(input("Deseja remover algum convidado da lista? (sim/não):"))

if remover == "sim":
       removernome = str(input("Digite o nome de quem deseja remover: "))
       usuarios.remove(removernome)
       print(f"LISTA DE USUÁRIOS ATUALIZADA: {usuarios}")
       
elif remover == "não":
     print(f"LISTA DE CONVIDADOS: {usuarios}")

