import usb.core
import usb.util

# Encontra todos os dispositivos USB
devs = usb.core.find(find_all=True)

dev = devs[3]  # Obtém o quarto dispositivo da lista

# Configura o dispositivo para leitura
usb.util.claim_interface(dev, 0)
ep = dev[0][(0,0)][0]
next(devs for _, _, devs in zip(range(4), devs, devs))

# Lê os inputs do dispositivo indefinidamente
while True:
    try:
        data = ep.read(64, timeout=5000)
        key = chr(data[0])
        print("Tecla pressionada:", key)
    except usb.core.USBError as e:
        if e.args == ('Operation timed out',):
            continue
    except ValueError:
        print("\n\nNão tem DESCRIPTOR\n\n")