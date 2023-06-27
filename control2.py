import usb.core

# Encontra todos os dispositivos USB
devs = usb.core.find(find_all=True)
# Verifica se algum dispositivo foi encontrado

backend = usb.backend.libusb1.get_backend()

# Itera sobre os dispositivos encontrados
for dev in devs:
    # Obtém as informações do dispositivo
    dev_info = dev
        # Imprime as informações do dispositivo        

    print("ID do dispositivo: 0x{:04x}:0x{:04x}".format(dev_info.idVendor, dev_info.idProduct))
    print("Fabricante: {}".format(usb.util.get_string(dev_info, dev_info.iManufacturer)))
    print("Produto: {}".format(usb.util.get_string(dev_info, dev_info.iProduct)))
    print("Serial: {}".format(usb.util.get_string(dev_info, dev_info.iSerialNumber)))
    print("--------------------------------------")

    if ("0x{:04x}:0x{:04x}".format(dev_info.idVendor, dev_info.idProduct) == "---0xffff:0x0035"):
        print(".\n.\n.Tentando Conexão...")

        usb.util.claim_interface(dev, 0)
        ep = dev[0][(0,0)][0]
        ep.read(64)

        # Lê dados de código de barras indefinidamente
        #while True:
            #data = ep.read(64, timeout=5000)
            #barcode = ''.join([chr(x) for x in data])
            #print('Código de barras lido:', barcode.strip())


   