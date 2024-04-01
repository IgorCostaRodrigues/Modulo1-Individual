# Imprime o cabeçalho do programa
print("\n╭─────────────────────────────────────────PROJETO INDIVIDUAL──────────────────────────────────────────╮")
print("│                                                                                                     │")
print("│                   ╭──────────────── D  E  U    M  A  T  C  H ! ! ! ───────────────╮                 │")
print("│                   │                                                               │                 │")
print("│                   │            Programa de Compatibilidade de Candidatos          │                 │")
print("│                   │                                                               │                 │")
print("│                   ╰───────────────────────────────────────────────────────────────╯                 │")
print("╰─────────────────────────────────────────────────────────────────────────────────────────────────────╯")



# Lista de candidatos cadastrados
candidatos = []

# Loop principal do programa
while True:
    # Mostra o menu principal e solicita a opção do usuário
    opcao = input(
       """
╭───────────────────────────────────────────MENU PRINCIPAL────────────────────────────────────────────╮
│                                                                                                     │
│    [1] Área de candidatos                                                                           │
│    [2] Sair do programa                                                                             │
│                                                                                                     │
╰─────────────────────────────────────────────────────────────────────────────────────────────────────╯
""")

    # Se o usuário escolher a opção "Área de candidatos"
    if opcao == "1":
        # Loop para a área de candidatos
        while True:
            # Mostra o menu da área de candidatos e solicita a opção do usuário
            opcao_cadastro_candidatos = input("""
╭───────────────────────────────────────ÁREA DE CANDIDATOS────────────────────────────────────────────╮
│                                                                                                     │
│    [1] Cadastrar candidato                                                                          │
│    [2] Remover candidato                                                                            │
│    [3] Verificar compatibilidade de candidatos                                                      │
│    [4] Ver candidatos cadastrados                                                                   │
│    [5] Voltar ao menu anterior                                                                      │
│                                                                                                     │
╰─────────────────────────────────────────────────────────────────────────────────────────────────────╯
""")

            # Se o usuário escolher a opção "Cadastrar candidato"
            if opcao_cadastro_candidatos == "1":
                print("\n╭──────────────────────────────────CADASTRO DE CANDIDATO──────────────────────────────────────────────╮")
                # Solicita informações do candidato
                nome = input("\nNome do candidato(a): ").title()
                nota_entrevista = float(input("Nota da entrevista: "))
                nota_teorico = float(input("Nota do teste teórico: "))
                nota_pratico = float(input("Nota do teste prático: "))
                nota_soft = float(input("Nota da avaliação de Soft Skills: "))

                # Formata as notas em um formato específico e armazen1a os dados do candidato em um dicionário
                resultado = f"e{nota_entrevista}_t{nota_teorico}_p{nota_pratico}_s{nota_soft}"
                candidato = {'nome': nome, 'resultado': resultado}
                # Adiciona o candidato à lista de candidatos
                candidatos.append(candidato)
                print("╭──────────────────────────────────────────────────────────────────────────────╮")
                print(f"│ Candidato {nome} cadastrado com sucesso!")                                          
                print("╰──────────────────────────────────────────────────────────────────────────────╯")
            # Se o usuário escolher a opção "Verificar compatibilidade de candidatos"
            elif opcao_cadastro_candidatos == "2":
                   print("\n╭──────────────────────────────────REMOVER CANDIDATO──────────────────────────────────────────────────╮")
                   nome_remover = input("Insira o nome do candidato que deseja remover: ").title()
                # Variável para verificar se o candidato foi encontrado na lista
                   encontrado = False
                # Loop para percorrer a lista de candidatos e remover o candidato com o nome fornecido
                   for candidato in candidatos:
                    if candidato['nome'] == nome_remover:
                     candidatos.remove(candidato)
                     print("╭─────────────────────────────────────────────────────────────────────────────╮")
                     print(f"│ {nome_remover} removido da lista de candidatos!")
                     print("╰─────────────────────────────────────────────────────────────────────────────╯")
                     encontrado = True
                     break
                # Se o candidato não for encontrado na lista, informa ao usuário
                   else:
                    print("╭─────────────────────────────────────────────────────────────────────────────╮")
                    print(f"│ {nome_remover} não encontrado na lista de candidatos.")
                    print("╰─────────────────────────────────────────────────────────────────────────────╯")

            elif opcao_cadastro_candidatos == "3":
                # Solicita as notas para verificar a compatibilidade
                print("\n╭──────────────────────────────VERIFICAR COMPATIBILIDADE──────────────────────────────────────────╮")
                nota_entrevista = float(input("Nota da entrevista: "))
                nota_teorico = float(input("Nota do teste teórico: "))
                nota_pratico = float(input("Nota do teste prático: "))
                nota_soft = float(input("Nota da avaliação de Soft Skills: "))

                # Cria um dicionário com os critérios de compatibilidade
                criterios = {
                    'e': nota_entrevista,
                    't': nota_teorico,
                    'p': nota_pratico,
                    's': nota_soft
                }

                # Lista para armazenar os candidatos compatíveis
                candidatos_compativeis = []

                # Itera sobre a lista de candidatos para verificar compatibilidade
                for candidato in candidatos:
                    resultado_candidato = candidato['resultado']

                    # Verifica se o candidato atende aos critérios de compatibilidade
                    if all(criterios[etapa] <= float(resultado_candidato.split('_')[indice][1:])
                           for indice, etapa in enumerate(['e', 't', 'p', 's'])):
                        candidatos_compativeis.append(candidato)

                # Se houver candidatos compatíveis, os imprime na tela
                if candidatos_compativeis:
                    print("╭─────────────────────────────────────────────────────────────────────────────╮")
                    print(f"│ Candidatos compatíveis encontrados:                                         │")
                    for candidato in candidatos_compativeis:
                       print(f"│ Nome: {candidato['nome']}, Resultado: {candidato['resultado']}")
     
                        
                else:
                    print("╭─────────────────────────────────────────────────────────────────────────────╮")
                    print("│ Não há candidatos compatíveis..                                             │")
                    print("╰─────────────────────────────────────────────────────────────────────────────╯")

            # Se o usuário escolher a opção "Ver candidatos cadastrados"
            elif opcao_cadastro_candidatos == "4":
                # Verifica se há candidatos cadastrados e os imprime na tela
                if candidatos:
                    print("\nCandidatos cadastrados:")
                    for candidato in candidatos:
                        print(f"Nome: {candidato['nome']}, Resultado: {candidato['resultado']}")
  
                else:
                    print("╭─────────────────────────────────────────────────────────────────────────────╮")
                    print("│ Não há candidatos cadastrados.                                              │ ")
                    print("╰─────────────────────────────────────────────────────────────────────────────╯")
            # Se o usuário escolher a opção "Voltar ao menu anterior"
            elif opcao_cadastro_candidatos == "5":
                break

            # Se o usuário inserir uma opção inválida
            else:
                print("\nPor favor, insira uma opção válida.")

    # Se o usuário escolher a opção "Sair do programa"
    elif opcao == "2":
        print('''   ____  _          _                 _              __  
  / __ \| |        (_)               | |        _____\ \ 
 | |  | | |__  _ __ _  __ _  __ _  __| | ___   |______| |
 | |  | | '_ \| '__| |/ _` |/ _` |/ _` |/ _ \   ______| |
 | |__| | |_) | |  | | (_| | (_| | (_| | (_) | |______| |
  \____/|_.__/|_|  |_|\__, |\__,_|\__,_|\___/         | |
                       __/ |                         /_/ 
                      |___/                              ''')
        break

    # Se o usuário inserir uma opção inválida
    else:
        print("\nPor favor, insira uma opção válida.")