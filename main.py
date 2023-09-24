estações = {89.5: 'Cocais', 91.5: 'Mix', 94.1: 'Boa', 99.1: 'Clube'}


class RadioFM:
    indice_estação = 0

    def __init__(self, vol_max, estações) -> None:
        self.volume_min = 0
        self.volume_max = vol_max
        self.freq_min = 88
        self.freq_max = 108
        self.estações = estações
        self.volume = None
        self.ligado = False
        self.estação_atual = None
        self.frequencia_atual = None
        self.antena_habilitada = False

    def ligar(self):
        self.ligado = True
        self.volume = self.volume_min
        # Só sintonisa na rádio se estiver ligado
        if self.antena_habilitada:
            self.frequencia_atual = list(self.estações.keys())[
                self.indice_estação]
            self.estação_atual = self.estações.get(self.frequencia_atual)

    def desligar(self):
        self.ligado = False
        self.volume = None
        self.frequencia_atual = None
        self.estação_atual = None

    def aumentar_volume(self, up_vol=1):
        # Se volume for None o volume é filtrado pelo operador ternário
        if self.volume is None:
            self.volume = up_vol if up_vol <= self.volume_max else self.volume_max
        # Se volume não for none, checa se é menor que o volume máximo
        elif self.volume <= self.volume_max:
            self.volume += up_vol
        elif self.volume_max < up_vol >= self.volume:
            self.volume = self.volume_max
            print("Volume atingio o máximo")
        else:
            print("Volume no máximo!", flush=False)

    def diminuir_volume(self, down_vol=1):
        if self.volume is None:
            self.volume = down_vol if down_vol >= self.volume_min else 0
        elif self.volume >= self.volume_min:
            self.volume -= down_vol
        else:
            print("Volume muito baixo!", flush=False)

    def mudar_frequencia(self, freq=0.0):
        if freq:
            if freq in self.estações:
                self.estação_atual = self.estações.get(freq, freq)
            else:
                print("Estação inexistente!")
        else:
            # se tentar mudar frequencia atual e ela for o último item do dicionario, retorna para o primeiro item
            # list converte o dict_keys para lista e então pode ser percorrido pelos indices numéricos
            if self.frequencia_atual == list(self.estações.keys())[len(self.estações) - 1]:
                self.indice_estação = 0  # Zerando o contador
                self.frequencia_atual = list(self.estações.keys())[
                    self.indice_estação]
                self.estação_atual = self.estações.get(self.frequencia_atual)
            else:
                self.indice_estação += 1  # incrementando o contador
                self.frequencia_atual = list(self.estações.keys())[
                    self.indice_estação]
                self.estação_atual = self.estações.get(self.frequencia_atual)


radio1 = RadioFM(10, estações)
# Para que funcione corretamente é nescessário alterar o estado da antena para True
radio1.antena_habilitada = True
radio1.ligar()
print(radio1.estação_atual)
print(radio1.volume)
radio1.aumentar_volume()
radio1.aumentar_volume(5)
print(radio1.volume)
radio1.mudar_frequencia()
print(radio1.estação_atual)
radio1.mudar_frequencia(93.8)
print(radio1.estação_atual)
radio1.mudar_frequencia()
print(radio1.estação_atual)


estações.update({100.2: 'Atena 10'})
caixola = RadioFM(100, estações)
caixola.antena_habilitada = True
caixola.mudar_frequencia()
print(caixola.estação_atual)
caixola.mudar_frequencia()
print(caixola.estação_atual)
caixola.mudar_frequencia()
print(caixola.estação_atual)
caixola.mudar_frequencia()
print(caixola.estação_atual)

radiola = RadioFM(50, estações)
radiola.antena_habilitada = True
radiola.mudar_frequencia(102.5)
radiola.estações.update({102.5: 'Guarani'})
radiola.mudar_frequencia(102.5)
print(radiola.estação_atual)
radiola.aumentar_volume(49)
radiola.aumentar_volume(100)
