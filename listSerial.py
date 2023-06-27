import serial.tools.list_ports

# Lista todas as portas seriais disponíveis no sistema
ports = serial.tools.list_ports.comports()

if len(ports) == 0:
    print("Nenhuma porta serial encontrada.")
else:
    print("Portas seriais disponíveis:")
    for port in ports:
        print(port.device)
