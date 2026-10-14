print("Mensagens Secretas")

numero = 0
while numero != 3:
    print("\n[1] Criptografia [2] Descriptografar [3] Sair")
    opcao = int(input("Escolha sua opção: "))
    
    if opcao == 1:
        mensagem = input("Digite sua mensagem: ")
        chave = int(input("Digite o número da chave: "))
        resultado = ""
        
        for letra in mensagem:
            resultado = resultado + chr(ord(letra) + chave)
            
        print("Mensagem criptografada:", resultado)

    elif opcao == 2:
        mensagem = input("Digite a mensagem criptografada: ")
        
        for chave in range(1, 26):
            resultado = ""
            for letra in mensagem:
                resultado = resultado + chr(ord(letra) - chave)
            print(f"Chave {chave}: {resultado}")

    elif opcao == 3:
        print("Encerrando o programa. Até mais!")
        break
    else:
        print("Opção inválida! Escolha 1, 2 ou 3.")