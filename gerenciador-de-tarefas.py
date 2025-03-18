lista = []

def adicionarTarefa():
    tarefa = {}
    tarefa['Título'] = input('Digite o título da tarefa: ')
    tarefa['Prioridade'] = int(input('Digite o nível de prioridade: '))
    tarefa['Concluída'] = False
    lista.append(tarefa)

def listarTarefa():
    if not lista:
        print('A lista está vazia.')
        return

    print('Lista de tarefas: \n')
    for i, tarefa in enumerate(lista):
        status = 'Concluído' if tarefa['Concluída'] else 'Pendente'
        print(f'{i + 1} - Título: {tarefa["Título"]} | Prioridade: {tarefa["Prioridade"]} | Status: {status}')

def marcarConcluido():
    listarTarefa()
    if not lista:
        print('A lista está vazia.')
        return

    tarefa_index = int(input('Digite a tarefa que queira marcar como concluída: '))

    if tarefa_index < 1 or tarefa_index > len(lista):
        print('Número inválido. Digite um número válido da lista de tarefas.')
        return

    lista[tarefa_index - 1]['Concluída'] = True
    print(f'Tarefa {lista[tarefa_index - 1]["Título"]} marcada como concluída!')

def exibirPrioridade():
    if not lista:
        print('A lista está vazia')
        return

    for prioridade in range(1, 4):
        tarefas_ordenadas = filter(lambda x: x['Prioridade'] == prioridade, lista)
        for tarefa in tarefas_ordenadas:
            status = 'Concluído' if tarefa['Concluída'] else 'Pendente'
            print(f'Prioridade: {tarefa["Prioridade"]} | Título: {tarefa["Título"]} | Status: {status}')

def editarTarefa():
    listarTarefa()
    if not lista:
        print("Não há tarefas para editar.")
        return

    editar_index = int(input('Digite a tarefa que queira editar: ')) - 1

    if 0 <= editar_index < len(lista):
        print(f'Você está editando a tarefa: {lista[editar_index]["Título"]}')
        lista[editar_index]['Título'] = input('Insira novo título: ')
        lista[editar_index]['Prioridade'] = int(input('Digite a nova prioridade: ')) 
    else:
        print("Número de tarefa inválido.")

while True:
    opcao = input('''
(1) - Adicionar tarefa
(2) - Listar tarefas
(3) - Marcar tarefa como concluída
(4) - Exibir lista por prioridade
(5) - Editar tarefa
(6) - Sair

''')

    match opcao:
        case '1':
            adicionarTarefa()
        case '2':
            listarTarefa()
        case '3':
            marcarConcluido()
        case '4':
            exibirPrioridade()
        case '5':
            editarTarefa()
        case '6':
            print('Saindo do programa...')
            break
        case _:
            print('Digite um número válido!')
