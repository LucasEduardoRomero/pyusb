import usb.core
import usb.util


if __name__ == '__main__':
    devs = usb.core.find(find_all=True)
    for dev in devs:

        #dev = usb.core.find(idVendor=0xffff, idProduct=0x0035)
        if (dev is None):
            raise ValueError("Device not found")

        print("CP 1")
        dev.set_configuration()

        configuration = dev.get_active_configuration()
        cfg_ = configuration[(0, 0)]

        #outPoint = usb.util.find_descriptor(
        #    cfg_,
            # match the first OUT endpoint
        #    custom_match=lambda e: usb.util.endpoint_direction(e.bEndpointAddress) == usb.util.ENDPOINT_OUT)
        
        inPoint = usb.util.find_descriptor(
            cfg_,
            # match the first OUT endpoint
            custom_match=lambda e: usb.util.endpoint_direction(e.bEndpointAddress) == usb.util.ENDPOINT_IN)

        assert inPoint is not None

        #print(outPoint)
        print(inPoint)
    
   