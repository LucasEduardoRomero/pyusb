

## 1. Abre uma interface listando todos dispositivos com seus: idVendor, idProduct, Bus e Address.
## 2. Usuário seleciona quais devices da lista ele quer capturar
## 3. Salva a lista em arquivo como "list.json"


import usb.core
import json
import threading
import time
import logging
import sys

#################################################################################
# Este codigo recebe uma lista de objetos com id_vendor, id_produt, e bus_address
# e então cria uma thread de leitura para cada dispositivo/item da lista.
#################################################################################

#backend = usb.backend.libusb1.get_backend()

CONFIG_FILE_PATH = '/home/bingo/projetos/pyusb/linux_teste/read_multiple/list.json'

def try_read(device, prefix):
    DATA_SIZE = 16 # 224
    NO_SCAN_CODE = {0x1E:'1', 0x1F:'2', 0x20:'3', 0x21:'4', 0x22:'5', 0x23:'6', 0x24:'7'
        , 0x25:'8', 0x26:'9', 0x27:'0', 0x28:'', } # 28=enter

    #prefix = device_info['prefix']
    #id_vendor = int(device_info['id_vendor'], 16)
    #id_product = int(device_info['id_product'], 16)
    #bus = int(device_info['bus'])
    #address= int(device_info['address'])
    #print(id_vendor)
    #print(id_product)
    #print(bus)
    #print(address)
    #device = usb.core.find(idVendor=id_vendor, idProduct=id_product, bus=bus, address=address)
    #print(device.iProduct)
    if device is None:
        print("not found")
        sys.exit("Could not find Id System Barcode Reader.")

    if device.is_kernel_driver_active(0):
        try:
            device.detach_kernel_driver(0)
        except usb.core.USBError as e:
            sys.exit("Could not detatch kernel driver: %s" % str(e))


    endpoint = device[0][(0,0)][0]
    data = []
    lu = False
    print( "Waiting to read...")
    lecture=''

    while 1:
        try:
            data += device.read(endpoint.bEndpointAddress, endpoint.wMaxPacketSize)

            if not lu:
                print( "Waiting to read...")
            lu = True

        except usb.core.USBError as e:
            if e.args == (110,'Operation timed out') and lu:
                if len(data) < DATA_SIZE:
                    print( "Lecture incorrecte, recommencez. (%d bytes)" % len(data))
                    print( "Data: %s" % ''.join(map(hex, data)))
                    data = []
                    lu = False
                    continue
                else:
                    for char in data:
                        if (char != 0):
                            lecture += NO_SCAN_CODE[char]                    
                    print(f"{prefix} - {lecture}") # no futuro esse print vira um "escrever no arquivo do leitor PREFIX"
                    lu = False
                    data = []
                    lecture = ''
                    continue
    return 1




if __name__ == '__main__':
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO, datefmt="%H:%M:%S")

    thread_list = []
    devices = usb.core.find(find_all=True)
    for idx, dev in enumerate(devices):
        dev_info = dev
        t = threading.Thread(target=try_read, args=(dev, idx,))
        thread_list.append(t)
        # TODO -> VER COMO FECHAR AS THREADS CORRETAMENTE
        t.start()