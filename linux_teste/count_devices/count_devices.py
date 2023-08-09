import usb.core

#backend = usb.backend.libusb1.get_backend()

# with pure PyUSB
lista = usb.core.find(find_all=True)
i = 0
for dev in lista:
    i = i + 1
    print(dev)

print(f"\n\nTAMANHO DA LISTA {i}")

