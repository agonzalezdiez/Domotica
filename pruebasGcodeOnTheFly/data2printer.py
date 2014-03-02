from printingLib import printcore
import json
import sys
import time

baud = 115200
#port = "usbserial-A6023GPD"
port = '/dev/tty.usbserial-A6023GPD'

printer_ifaz = printcore(port=port,baud=baud)

while(not printer_ifaz.is_ready()):
    print "ESPERO"
    time.sleep(0.5)

#printer_ifaz.send("G28")
printer_ifaz._send('G28',-1)

while(not printer_ifaz.is_ready()):
    print "ESPERO"
    time.sleep(0.5)
printer_ifaz._send('G1 Z40',-1)

while(not printer_ifaz.is_ready()):
    print "ESPERO"
    time.sleep(0.5)

esperando=True
while(esperando):
    command = raw_input("Enter your command: ")
    print type(command)
    if command=="quit":
        esperando=None
    else:
        printer_ifaz._send(command,-1)
        while(not printer_ifaz.is_ready()):
            print "ESPERO"
            time.sleep(0.5)
#mensaje = "MSJ:"
#while(mensaje!=""):
#    mensaje = printer_ifaz._readline()
#    print mensaje
print "DESCONECTO"
printer_ifaz.disconnect()
