Cenario-1:class Evento:
    def init(self, nome, descricao, data, hora_inicio):
        self.nome = nome
        self.descricao = descricao
        self.data = data
        self.hora_inicio = hora_inicio
        self.participantes = []

    def adicionar_participante(self, participante):
        self.participantes.append(participante)

    def str(self):
        return f"{self.nome} - {self.data} às {self.hora_inicio}"


class SistemaGerenciamentoEventos:
    def init(self):
        self.eventos = []

    def adicionar_evento(self, evento):
        self.eventos.append(evento)

    def listar_eventos(self):
        for evento in self.eventos:
            print(evento)


//Função para receber entrada do usuário e criar um evento:

def criar_evento():
    nome = input("Digite o nome do evento: ")
    descricao = input("Digite a descrição do evento: ")
    data = input("Digite a data do evento (no formato AAAA-MM-DD): ")
    hora_inicio = input("Digite a hora de início do evento (no formato HH:MM): ")

    return Evento(nome, descricao, data, hora_inicio)


//Exemplo de uso:
sistema = SistemaGerenciamentoEventos()

//Adicionar eventos usando a entrada do usuário:
while True:
    criar_novo = input("Deseja criar um novo evento? (s/n): ")
    if criar_novo.lower() != 's':
        break
    evento = criar_evento()
    sistema.adicionar_evento(evento)

//Listar todos os eventos cadastrados:
print("\nEventos cadastrados:")
sistema.listar_eventos()
