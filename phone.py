import time
import json
import serial

class Message:
    def __init__(self,sender,date,txt):
        self.sender = sender
        self.date = date
        self.txt = txt


def write(message, recipient):
    phone = serial.Serial("/dev/ttyUSB2",  460800, timeout=5)
    try:
        phone.write(b'ATZ\r')
        phone.flush()
        phone.write(b'AT+CMGF=1\r')
        phone.flush()
        phone.write(b'AT+CMGS="' + recipient.encode() + b'"\r')
        phone.flush()
        phone.write(message.encode() + b"\r")
        phone.flush()
        phone.write(bytes([26]))
        phone.flush()
    finally:
        phone.close()

def read():
    phone = serial.Serial("/dev/ttyUSB2",  115200, timeout=1)
    phone.flush()
    phone.write(b'AT+CMGF=1\r')
    phone.flush()
    phone.write(b'AT+CPMS="ME",SM","ME"\r')
    phone.flush()
    try:
        phone.write(b'AT+CMGF=1\r')
        phone.flush()
        phone.write(b'AT+CMGL="ALL"\r')
        phone.flush()
        a = phone.readlines()
        b = []
        for x in a:
            if x.decode().startswith('+CMGL:'):
                r = a.index(x)
                t = r+1
                q = str.encode(a[r].decode(), 'utf-8')
                q = q.decode().split(',')
                z = str.encode(a[t].decode('utf-8'), 'utf-8') 
                try:
                    b.append(
                                {
                                'from':q[2].rstrip().replace('\"',''),
                                'date':q[4].rstrip().replace('\"',''),
                                'time':q[5].rstrip().replace('\"',''),
                                'mesg':z.decode('utf-8').rstrip().replace('\"',''),
                                }
                            )
                except:
                    print('err')
    finally:
        phone.close()
        for i in b:
            print(i)

read()
