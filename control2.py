import usb.core

# Encontra todos os dispositivos USB
devs = usb.core.find(find_all=True)
# Verifica se algum dispositivo foi encontrado
print("Dispositivos USB encontrados:")
backend = usb.backend.libusb1.get_backend()

# Itera sobre os dispositivos encontrados
for dev in devs:
    # Obtém as informações do dispositivo
    dev_info = dev
    try:
        # Imprime as informações do dispositivo
        print("ID do dispositivo: 0x{:04x}:0x{:04x}".format(dev_info.idVendor, dev_info.idProduct))
        print("Fabricante: {}".format(usb.util.get_string(dev_info, dev_info.iManufacturer)))
        print("Produto: {}".format(usb.util.get_string(dev_info, dev_info.iProduct)))
        print("Serial: {}".format(usb.util.get_string(dev_info, dev_info.iSerialNumber)))
        print("--------------------------------------")
    except Exception:
        print("\nNão conseguiu ler Device\n")
        
