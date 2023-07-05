from escpos.connections import getUSBPrinter


printer = getUSBPrinter()(idVendor=0x28e9,  # USB vendor and product Ids for Bixolon SRP-350plus
                          idProduct=0x0289,  # printer
                          inputEndPoint=0x81,
                          outputEndPoint=0x01)

printer.text("hola luz")
printer.lf()
