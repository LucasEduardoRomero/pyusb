import keyboard
import threading

class LeitorCodigoBarras(threading.Thread):
    def __init__(self, nome_leitor):
        super().__init__()
        self.nome_leitor = nome_leitor
        self.codigo_de_barras = ""
        self.sair = threading.Event()
    
    def run(self):
        print(f"Iniciando leitor {self.nome_leitor}...")
        
        # Aguarda a entrada de teclado até que o código de barras seja lido ou sair seja sinalizado
        while not self.sair.is_set():
            try:
                # Captura a próxima tecla pressionada
                tecla = keyboard.read_event()
                
                # Verifica se é uma tecla de caractere (não é um modificador de teclado)
                if hasattr(tecla, 'char'):
                    # Concatena o caractere ao código de barras
                    self.codigo_de_barras += tecla.char
                    
                # Verifica se a tecla Enter foi pressionada para encerrar a leitura do código de barras
                if tecla.name == "enter":
                    print(f"Leitor {self.nome_leitor} - Código de Barras: {self.codigo_de_barras}")
                    self.codigo_de_barras = ""
                    
            except KeyboardInterrupt:
                # Interrompe a captura se o programa for interrompido manualmente
                break
    
    def parar(self):
        self.sair.set()
        self.join()
        print(f"Leitor {self.nome_leitor} finalizado.")

# Cria instâncias dos leitores de código de barras
leitor1 = LeitorCodigoBarras("Leitor 1")
leitor2 = LeitorCodigoBarras("Leitor 2")

# Inicia as threads dos leitores
leitor1.start()
leitor2.start()

try:
    # Mantém o programa em execução até que seja interrompido manualmente
    while True:
        continue
except KeyboardInterrupt:
    # Interrompe o programa quando uma interrupção de teclado é detectada
    leitor1.parar()
    leitor2.parar()
