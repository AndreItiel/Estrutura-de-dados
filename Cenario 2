cenario-2:class Reserva:
    def init(self, nome_cliente, num_pessoas, data, hora):
        self.nome_cliente = nome_cliente
        self.num_pessoas = num_pessoas
        self.data = data
        self.hora = hora

    def str(self):
        return f"Reserva para {self.num_pessoas} pessoa(s) em nome de {self.nome_cliente} para o dia {self.data} às {self.hora}"


class SistemaReservas:
    def init(self):
        self.reservas = []

    def fazer_reserva(self, reserva):
        self.reservas.append(reserva)

    def listar_reservas(self):
        for reserva in self.reservas:
            print(reserva)


//Função para criar uma reserva:
def criar_reserva():
    nome_cliente = input("Digite o nome do cliente: ")
    num_pessoas = int(input("Digite o número de pessoas: "))
    data = input("Digite a data da reserva (no formato AAAA-MM-DD): ")
    hora = input("Digite a hora da reserva (no formato HH:MM): ")

    return Reserva(nome_cliente, num_pessoas, data, hora)


//Exemplo de uso:
sistema_reservas = SistemaReservas()

//Adicionar reservas usando a entrada do usuário:
while True:
    criar_nova_reserva = input("Deseja fazer uma nova reserva? (s/n): ")
    if criar_nova_reserva.lower() != 's':
        break
    reserva = criar_reserva()
    sistema_reservas.fazer_reserva(reserva)

//Listar todas as reservas feitas:
print("\nReservas feitas:")
sistema_reservas.listar_reservas()
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
