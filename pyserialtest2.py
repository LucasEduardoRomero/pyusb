import sys
import select

def read_barcode():
    input_ready, _, _ = select.select([sys.stdin], [], [], 5)
    if sys.stdin in input_ready:
        barcode = sys.stdin.readline().strip()
        return barcode
    return None

try:
    while True:
        barcode = read_barcode()
        if barcode:
            print('Código de barras lido:', barcode)

except KeyboardInterrupt:
    pass