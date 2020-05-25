import serial
import time
import utils

class Phone:
    def __init__(self):
        self.phone = serial.Serial("/dev/ttyUSB2",  460800, timeout=5)

    def unlock(self):
        try:
            self.phone.write(b'AT+CPIN="3451"\r')
            self.phone.flush()
        except:
            print('could not unlock')
    
    def write(self,message, recipient):
        try:
            self.phone.write(b'ATZ\r')
            self.phone.flush()
            self.phone.write(b'AT+CMGF=1\r')
            self.phone.flush()
            self.phone.write(b'AT+CMGS="' + recipient.encode() + b'"\r')
            self.phone.flush()
            self.phone.write(message.encode() + b"\r")
            self.phone.flush()
            self.phone.write(bytes([26]))
            self.phone.flush()
        except:
            print('could not send message')
        finally:
            time.sleep(5)
    
    def read(self):
        messages = None
        try:
            self.phone.write(b'AT+CMGF=1\r')
            self.phone.flush()
            self.phone.write(b'AT+CPMS="ME",SM","ME"\r')
            self.phone.flush()
            self.phone.write(b'AT+CMGF=1\r')
            self.phone.flush()
            self.phone.write(b'AT+CMGL="ALL"\r')
            self.phone.flush()
        except:
            print('could not read messages')
        finally:
            messages = utils.split_messages(self.phone.readlines())
            return messages

    def done(self):
        self.phone.close()
