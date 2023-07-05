import usb.core
import usb.util

# 1) Add your user to the Linux group "lp" (line printer)
# 
# 2) check lsusb to see id vendor and id product of your thermal printer
#
# 3) Add a udev rule to allow all users to use this USB device:
#
#    In /etc/udev/rules.d create a file ending in .rules, such as
#    33-receipt-printer.rules with the contents:
#
#   SUBSYSTEM=="usb", ATTR{idVendor}=="28e9", ATTR{idProduct}=="0289", MODE="666"

dev = usb.core.find(idVendor=0x28e9, idProduct=0x0289)

# Was it found:
if dev is None:
    raise ValueError('Device not found')

# Disconnect it from kernel
needs_reattach = False
if dev.is_kernel_driver_active(0):
    needs_reattach = True
    dev.detach_kernel_driver(0)

# Set the active configuration. With no arguments, the first
# configuration will be the active one
dev.set_configuration()

# get an endpoint instance
cfg = dev.get_active_configuration()
intf = cfg[(0,0)]

ep = usb.util.find_descriptor(
    intf,
    # match the first OUT endpoint
    custom_match = \
    lambda e: \
        usb.util.endpoint_direction(e.bEndpointAddress) == \
        usb.util.ENDPOINT_OUT)

assert ep is not None

# write the data
ep.write('Hello, world!\n\n')
#         000000000111111111122222222223
#         123456789012345678901234567890
ep.write('Soluta sed voluptatem ut\n')
ep.write('facere aut. Modi placeat et\n')
ep.write('eius voluptate sint ut.\n')
ep.write('Facilis minima ex quia quia\n')
ep.write('consectetur ex ipsa. Neque et\n')
ep.write('voluptatem ipsa enim error\n')
ep.write('reprehenderit ex dolore.\n')
ep.write('Cupiditate ad voluptatem nisi.\n\n\n\n')

# Reattach if it was attached originally
dev.reset()
if needs_reattach:
    dev.attach_kernel_driver(0)
    print("Reattached USB device to kernel driver")
