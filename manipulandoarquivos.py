def jogar():
    modo = int(input("Digite o modo de entrada [1] Entrada [2] leitura..."))
    while (modo != 0):
        if modo == 3:
            modo = int(input("Digite o modo de entrada [1] Entrada [2] leitura..."))
        if (modo == 1):
            elemento = input("Digite um endereco...")
            with open('palavras.txt', 'a') as arquivo:
                arquivo.write(elemento + '\n')
            arquivo.close()
            teste = input("Deseja continuar? (Y/N) [3] para retornar ao menu")
            teste = teste.upper()
            if (teste == "Y"):
                continue
            elif (teste == "N"):
                modo = 0
            elif (teste.isdigit() and int(teste) == 3):
                modo = 3
                continue
            else:
                input("Erro [02] nao foi declarado o valor {} ...".format(teste))
        elif (modo == 2):
            arquivo = open('palavras.txt', 'r')
            linhas = arquivo.read().splitlines()
            for linha in linhas:
                print(linha)
            teste = input("Deseja continuar? (Y/N) [3] para retornar ao menu")
            teste = teste.upper()
            if (teste == "Y"):
                continue
            elif (teste == "N"):
                modo = 0
            elif (teste.isdigit() and int(teste) == 3):
                modo = 3
                continue
            else:
                input("Erro [03] nao foi declarado o valor {} ...".format(teste))
        elif (modo == 3):
            continue
        else:
            input("Erro [01] Nao foi possivel encontrar o modo de inicializacao, tecle qualquer *caractere* para sair...")

if (__name__ == "__main__"):
    jogar()