"""
🎮 Exercício 1 — Gerenciador de Tarefas no Terminal
Crie um programa que funcione como um gerenciador de tarefas simples. O programa
 deve:
Ter um menu em loop com as opções: adicionar tarefa, listar tarefas, marcar como
 concluída, sair
Guardar as tarefas em uma lista de dicionários, cada tarefa com id, nome e status
(pendente ou concluída)
Usar funções separadas pra cada ação (adicionar, listar, concluir)
Salvar as tarefas em um arquivo .txt ou .json sempre que uma tarefa for adicionada/atualizada
Carregar as tarefas do arquivo quando o programa iniciar (pra não perder os dados)
Usar tupla pra guardar as opções válidas do menu e validar a escolha do usuário
"""
def valida_entrada():
   
    texto = """
    Bem-vindo ao seu task manager.

    1. Adicionar tarefa.
    2. Listar tarefas.
    3. Marcar como concluída. 
    4. Sair.
    """
    while True:
        try:
            opcao = int(input(texto)) 
        except ValueError as err:
            print("\nVocê precisa digitar um número.")
            continue
        
        if opcao < 1 or opcao >4:
            print("Você precisa digitar uma opção válida.")
            continue
        elif 1 <= opcao <=3:
            return opcao
        else:
            break


def criar_tarefa(lista_de_tarefas, nome):
    tarefa = {
        "id": len(lista_de_tarefas) + 1, 
        "nome": nome,
        "status": "pendente"
    }

    lista_de_tarefas.append(tarefa)

def listar_tarefas(lista_de_tarefas):
    for i in lista_de_tarefas:
        print(i)    

def mudar_status(lista_de_tarefas, id_tarefa):
    for tarefa in lista_de_tarefas:
        if tarefa["id"] == id_tarefa:
            tarefa["status"] = "concluída"
            return
    print("Tarefa não encontrada.")

def mudar_status_v02(lista_de_tarefas, lista_de_tarefas_concluidas, id_tarefa):
    for tarefa in lista_de_tarefas:
        if tarefa["id"] == id_tarefa:
            tarefa["status"] = "concluída"
            lista_de_tarefas_concluidas.append(tarefa)
            return
    print("Tarefa não encontrada.")

def deletar_tarefa(lista_de_tarefas, id_tarefa):
    for tarefa in lista_de_tarefas:
        if tarefa["id"] == id_tarefa:
            lista_de_tarefas.remove(tarefa)
            print("Tarefa deletada. ")
            return
    print("Tarefa não encontrada")
tarefas = []
tarefas_concluida = []
while True:
    opcao = valida_entrada() 

    if opcao == 1:
        nome_tarefa = input("tarefa: ")
        criar_tarefa(tarefas, nome= nome_tarefa)
    elif opcao == 2:
        listar_tarefas(tarefas)
    elif opcao == 3:
        id = int(input("id: "))
        mudar_status(tarefas, id)
    else:
        break
