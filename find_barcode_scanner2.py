import usb.core
import usb.util

def find_barcode_scanner():
    # ID do fabricante do leitor de código de barras
    MANUFACTURER_ID = "BARCODE SCANNER"

    # Obter todos os dispositivos USB
    devices = usb.core.find(find_all=True)

    # Procurar pelos dispositivos que correspondem ao fabricante
    for device in devices:
        print(f"DEVICE {device.manufacturer}")
        if device.manufacturer == MANUFACTURER_ID:
            if device.get_active_configuration() is None:
                continue

            # Iterar sobre as interfaces do dispositivo
            for config in device:
                for intf in config:
                    # Verificar se a interface possui um endpoint de entrada
                    endpoint = usb.util.find_descriptor(
                        intf,
                        custom_match=lambda e: usb.util.endpoint_direction(e.bEndpointAddress) == usb.util.ENDPOINT_IN
                    )

                    # Encontrar o endpoint de entrada
                    if endpoint:
                        print(f"INICIANDO LEITURA config {config} interface {intf}")
                        data = []
                        lecture = ""
                        try:
                            print(data)        
                            data += device.read(endpoint.bEndpointAddress, endpoint.wMaxPacketSize)

                            if not lu:
                                print ("Waiting to read...")
                            lu = True
                        except usb.core.USBError as e:
                            if e.args == (110,'Operation timed out') and lu:
                                if len(data) < DATA_SIZE:
                                    print ("Lecture incorrecte, recommencez. (%d bytes)") % len(data)
                                    print ("Data: %s" % ''.join(map(hex, data)))
                                    data = []
                                    lu = False
                                    continue
                                else:
                                    for n in range(0,len(data),16):
                                        print (' '.join(map(hex,data[n:n+16])))
                                        lecture+=NO_SCAN_CODE[data[n+2]]
                                    break   # Code lu
                        print(lecture)


    # Retornar None caso nenhum dispositivo seja encontrado
    return None, None

# Exemplo de uso
device, endpoint = find_barcode_scanner()

if device and endpoint:
    data = []
    lu = False
    lecture = ''

    device.detach_kernel_driver(0)
    usb.util.claim_interface(device, 0) 



    while 1:
        try:         
            data += device.read(endpoint.bEndpointAddress, endpoint.wMaxPacketSize)


            if not lu:
                print ("Waiting to read...")
            lu = True

        except usb.core.USBError as e:
            if e.args == (110,'Operation timed out') and lu:
                if len(data) < DATA_SIZE:
                    print ("Lecture incorrecte, recommencez. (%d bytes)") % len(data)
                    print ("Data: %s" % ''.join(map(hex, data)))
                    data = []
                    lu = False
                    continue
                else:
                    for n in range(0,len(data),16):
                        print (' '.join(map(hex,data[n:n+16])))
                        lecture+=NO_SCAN_CODE[data[n+2]]
                    break   # Code lu
    print(lecture)

    ##print(device.read(endpoint.bEndpointAddress, endpoint.wMaxPacketSize))
    print("Dispositivo do leitor de código de barras encontrado!")
    # Faça algo com o dispositivo e o endpoint aqui
else:
    print("Nenhum dispositivo do leitor de código de barras encontrado.")
