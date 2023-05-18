import usb.core
import usb.util

# Encontra todos os dispositivos USB com o VID e PID do leitor de código de barras
devs = usb.core.find(find_all=True, idVendor=0x1234, idProduct=0x5678)

for dev in devs:
    print('Lendo dados do dispositivo:', dev)

    # Configura o dispositivo para leitura de código de barras
    usb.util.claim_interface(dev, 0)
    ep = dev[0][(0,0)][0]
    ep.read(64)

    # Lê dados de código de barras indefinidamente
    while True:
        data = ep.read(64, timeout=5000)
        barcode = ''.join([chr(x) for x in data])
        print('Código de barras lido:', barcode.strip())