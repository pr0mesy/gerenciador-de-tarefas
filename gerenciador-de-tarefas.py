import os 

def limpar_tela():
    sistema = os.name
    if sistema == 'nt':
        _ = os.system('cls')  
    else:
        _ = os.system('clear')  

lista = []

def adicionarTarefa():
    limpar_tela()  
    tarefa = {}
    tarefa['Título'] = input('Digite o título da tarefa: ')
    prioridade = int(input('Digite o nível de prioridade (1-3): '))
    while prioridade not in [1, 2, 3]:
        print('Digite um número entre 1-3.')
        prioridade = int(input('Digite o nível de prioridade (1-3): '))
    tarefa['Prioridade'] = prioridade
    tarefa['Concluída'] = False
    lista.append(tarefa)

def excluirTarefa():
    limpar_tela() 
    if not lista:
        print('A lista está vazia.')
        return
    
    listarTarefa()
    
    excluir_index = int(input('Digite a tarefa que deseja remover: ')) - 1
    if 0 <= excluir_index < len(lista):
        tarefa_removida = lista.pop(excluir_index)
        print(f'Tarefa "{tarefa_removida['Título']}" excluída com sucesso!')
    else:
        print(f'Digite um número entre 1 e {len(lista)}.')

def listarTarefa():
    limpar_tela()  
    if not lista:
        print('A lista está vazia.')
    else:
        print('Lista de tarefas:\n')
        for i, tarefa in enumerate(lista):
            status = 'Concluída' if tarefa['Concluída'] else 'Pendente'
            print(f'{i + 1} - Título: {tarefa["Título"]} | Prioridade: {tarefa["Prioridade"]} | Status: {status}')
    
    input("Pressione Enter para continuar...")

def marcarConcluido():
    limpar_tela()  
    listarTarefa()
    if not lista:
        print('A lista está vazia.')
        return

    tarefa_index = int(input('Digite a tarefa que deseja marcar como concluída: ')) - 1
    if 0 <= tarefa_index < len(lista):
        lista[tarefa_index]['Concluída'] = True
        print(f'Tarefa "{lista[tarefa_index]["Título"]}" marcada como concluída!')
    else:
        print(f'Digite um número entre 1 e {len(lista)}.')

def exibirPrioridade():
    limpar_tela()  
    if not lista:
        print('A lista está vazia.')
    else:
        for prioridade in range(1, 4):
            tarefas_ordenadas = list(filter(lambda x: x['Prioridade'] == prioridade, lista))
            for tarefa in tarefas_ordenadas:
                status = 'Concluída' if tarefa['Concluída'] else 'Pendente'
                print(f'Prioridade {tarefa["Prioridade"]} | Título: {tarefa["Título"]} | Status: {status}')
    
    input("Pressione Enter para continuar...")

def editarTarefa():
    limpar_tela()  
    listarTarefa()
    if not lista:
        print('A lista está vazia.')
        return

    editar_index = int(input('Digite a tarefa que deseja editar: ')) - 1
    if 0 <= editar_index < len(lista):
        print(f'Você está editando a tarefa: {lista[editar_index]["Título"]}')
        lista[editar_index]['Título'] = input('Insira novo título: ')
        prioridade = int(input('Digite o nível de prioridade (1-3): '))
        while prioridade not in [1, 2, 3]:
            print('Digite um número entre 1-3.')
            prioridade = int(input('Digite o nível de prioridade (1-3): '))
        lista[editar_index]['Prioridade'] = prioridade
        lista[editar_index]['Concluída'] = False
    else:
        print(f'Digite um número entre 1 e {len(lista)}.')

while True:
    limpar_tela()  
    opcao = input('''
==== Gerenciador de Tarefas ====
  (1) - Adicionar tarefa
  (2) - Excluir tarefas
  (3) - Listar tarefas
  (4) - Marcar tarefa como concluída
  (5) - Exibir lista por prioridade
  (6) - Editar tarefa
  (7) - Sair
================================
''')

    match opcao:
        case '1':
            adicionarTarefa()
        case '2':
            excluirTarefa()
        case '3':
            listarTarefa()
        case '4':
            marcarConcluido()
        case '5':
            exibirPrioridade()
        case '6':
            editarTarefa()
        case '7':
            print('Saindo do programa...')
            break
        case _:
            print('Digite um número válido.')
