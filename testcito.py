import os
unmount = os.system('sudo modprobe -r g_mass_storage')
print("`mount` ran with exit code %d" % unmount)
mount = os.system(
    "sudo modprobe g_mass_storage file=/usb-drive.img stall=0 ro=0 removable=1")
print("`mount` ran with exit code %d" % mount)
