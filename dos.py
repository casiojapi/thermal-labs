printer = open('/dev/usb/lp0', 'w')


for i in range(0, 25):
    printer.write("hola luz, hoy quiero tu locro.\n\n");
