print("--- Operações Básicas em Python ---")
n1 = int(input("\nDigite seu primeiro número: "))
n2 = int(input("\nDigite seu segundo número: "))
opcao = int (input("\nEscolha qual operação deseja:\n1- Soma\n2- Subtração\n3- Multiplicação\n4- Divisão\nDigite o número da operação que desja realizar: "))

if (opcao == 1):
    print(f"{n1} + {n2} = {n1+n2}")
elif (opcao == 2):
    print(f"{n1} - {n2} = {n1-n2}")
elif (opcao == 3):
    print(f"{n1} x {n2} = {n1*n2}")
elif (opcao == 4):
    print(f"{n1} / {n2} = {n1/n2}")
else:
    print("Opção inválida !")
