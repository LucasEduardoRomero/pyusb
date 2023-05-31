import serial

# Defina a porta serial e a taxa de comunicação adequada para o leitor de código de barras
porta_serial = 'COM1'  # Substitua pela porta serial correta
taxa_comunicacao = 9600  # Substitua pela taxa de comunicação correta

# Inicialize a comunicação com a porta serial
ser = serial.Serial(porta_serial, taxa_comunicacao, timeout=1)

try:
    while True:
        # Leia a linha da porta serial
        linha = ser.readline().decode('utf-8').strip()
        
        if linha:
            # Faça algo com os dados lidos, como imprimir na tela
            print('Código de barras lido:', linha)
            
except KeyboardInterrupt:
    pass

# Encerre a comunicação com a porta serial
ser.close()