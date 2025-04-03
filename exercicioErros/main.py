class Partida:
    def __init__(self, time1, time2, golsTime1, golsTime2):
        self.time1 = time1
        self.time2 = time2
        self.golsTime1 = golsTime1
        self.golsTime2 = golsTime2

    def get_resultado(self):
        return f'{self.time1} {self.golsTime1} x {self.golsTime2} {self.time2}'


class Torneio:
    def __init__(self):
        self.times = set()
        self.partidas = []

    def adicionar_time(self, nome):
        try:
            if not nome or nome.strip() == "":
                raise ValueError("Nome inválido")
            if nome in self.times:
                raise ValueError("Time já registrado")
            self.times.add(nome)
            print(f'✅ Time "{nome}" adicionado com sucesso!')
        except ValueError as e:
            print(f'❌ Erro: {e}')

    def criar_partida(self, time1, time2, golsTime1, golsTime2):
        try:
            if time1 not in self.times or time2 not in self.times:
                raise ValueError("Time não existe")
            if golsTime1 < 0 or golsTime2 < 0:
                raise ValueError("Número inválido de gols")
            partida = Partida(time1, time2, golsTime1, golsTime2)
            self.partidas.append(partida)
            print(f'✅ Partida entre "{time1}" e "{time2}" criada com sucesso!')
        except ValueError as e:
            print(f'❌ Erro: {e}')

    def jogar(self):
        pontos = {time: 0 for time in self.times}
        
        for partida in self.partidas:
            time1, time2, golsTime1, golsTime2 = partida.time1, partida.time2, partida.golsTime1, partida.golsTime2

            if golsTime1 > golsTime2:
                pontos[time1] += 3
            elif golsTime1 < golsTime2:
                pontos[time2] += 3
            else:
                pontos[time1] += 1
                pontos[time2] += 1
        
        return ResultadoTorneio(pontos, self.partidas)


class ResultadoTorneio:
    def __init__(self, pontos, partidas):
        self.pontos = pontos
        self.partidas = partidas

    def imprimir_classificacao(self):
        print("\nClassificação Final:")
        classificados = sorted(self.pontos.items(), key=lambda x: x[1], reverse=True)
        for time, pontos in classificados:
            print(f'{time} ({pontos} pontos)')

    def imprimir_resultados(self):
        print("\nResultados:")
        for partida in self.partidas:
            print(partida.get_resultado())


# Código principal
torneio = Torneio()

# Adicionando times
torneio.adicionar_time("Brasil")
torneio.adicionar_time("")  # ❌ Erro: Nome inválido
torneio.adicionar_time("Canadá")
torneio.adicionar_time("Argentina")
torneio.adicionar_time("Angola")

# Criando partidas
torneio.criar_partida("Brasil", "Canadá", 1, 0)
torneio.criar_partida("Argentina", "Angola", 2, 0)
torneio.criar_partida("Brasil", "Argentina", -10, -2)  # ❌ Erro: Número inválido de gols
torneio.criar_partida("Brasil", "Argentina", 0, 2)
torneio.criar_partida("Angola", "Canadá", 1, 1)
torneio.criar_partida("Brasil", "Angola", 3, 2)
torneio.criar_partida("Argentina", "Nigéria", 3, 3)  # ❌ Erro: Time não existe
torneio.criar_partida("Argentina", "Canadá", 2, 4)

# Exibe a classificação final e o resultado de cada partida
resultados = torneio.jogar()
resultados.imprimir_classificacao()
resultados.imprimir_resultados()
