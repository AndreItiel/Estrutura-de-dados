import heapq

class Task:
    def init(self, title, description, priority):
        self.title = title
        self.description = description
        self.priority = priority

class PriorityQueue:
    def init(self):
        self.tasks = []

    def addtask(self, task):
        heapq.heappush(self.tasks, (task.priority, task))

    def complete_task(self):
        if self.tasks:
            priority, task = heapq.heappop(self.tasks)
            return task
        else:
            return None

    def search_task_by_title(self, title):
        for , task in self.tasks:
            if task.title == title:
                return task
        return None

    def filtertasks_by_priority(self, priority):
        return [task for , task in self.tasks if task.priority == priority]

//Função para adicionar tarefas com entrada de usuário:
def addtaskfrominput():
    title = input("Digite o título da tarefa: ")
    description = input("Digite a descrição da tarefa: ")
    priority = int(input("Digite a prioridade da tarefa (1-Crítica, 2-Alta, 3-Média, 4-Baixa): "))
    return Task(title, description, priority)

//Exemplo de uso com entrada de usuário:
if _name == "__main":
    priority_queue = PriorityQueue()

    while True:
        print("\n### MENU ###")
        print("1. Adicionar tarefa")
        print("2. Concluir tarefa de maior prioridade")
        print("3. Pesquisar tarefa por título")
        print("4. Filtrar tarefas por prioridade")
        print("5. Sair")

        choice = input("Escolha uma opção: ")

        if choice == "1":
            task = add_task_from_input()
            priority_queue.add_task(task)
            print("Tarefa adicionada com sucesso!")

        elif choice == "2":
            completed_task = priority_queue.complete_task()
            if completed_task:
                print(f"Tarefa concluída: {completed_task.title}")
            else:
print("Não há tarefas para concluir.")

        elif choice == "3":
            title = input("Digite o título da tarefa a ser pesquisada: ")
            task = priority_queue.search_task_by_title(title)
            if task:
                print(f"Tarefa encontrada: {task.title}")
            else:
                print("Tarefa não encontrada.")

        elif choice == "4":
            priority = int(input("Digite a prioridade para filtrar as tarefas (1-Crítica, 2-Alta, 3-Média, 4-Baixa): "))
            filtered_tasks = priority_queue.filter_tasks_by_priority(priority)
            if filtered_tasks:
                print(f"Tarefas de prioridade {priority}:")
                for task in filtered_tasks:
                    print(f"- {task.title}")
            else:
                print("Não há tarefas com essa prioridade.")

        elif choice == "5":
            print("Saindo...")
            break

        else:
            print("Opção inválida. Por favor, escolha uma opção válida.")
