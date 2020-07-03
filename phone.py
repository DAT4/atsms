import mpv
import os
import serial
import signal
import subprocess
import threading
import sys
import traceback
import utils
import json
import time

class Phone:
    def __init__(self,usb):
        self.phone = serial.Serial(usb,  9600, timeout=5)
        
        self.phone.write(b'ATZ\r')

        self.phone.write(b'AT+CMGF=1\r')
        self.phone.flush()

        self.phone.write(b'AT+CSCS="GSM"\r')
        self.phone.flush()

    def unlock(self,pin):
        self.phone.write(b'AT+CPIN="' + pin.encode() + b'"\r')
        self.phone.flush()
    
    def write(self,message, recipient):
        self.phone.write(b'AT+CMGS="' + recipient.encode() + b'"\r')
        self.phone.flush()

        self.phone.write(message.encode() + b"\r")
        self.phone.flush()

        self.phone.write(bytes([26]))
        self.phone.flush()
    
    def read(self):
        messages = None

        self.phone.write(b'AT+CMGL="REC UNREAD"\r')
        self.phone.flush()

        messages = utils.split_messages(self.phone.readlines())
        return messages

    def done(self):
        self.phone.close()

class Musical:
    def __init__(self):
        self.p = Phone('/dev/ttyUSB2')

    def start_music(self):
        self.player = mpv.MPV(ytdl=True)
        self.player['video'] = False
        self.player.play('https://www.youtube.com/watch?v=zbUqGFSET-o')
    
    def handle_message(self, msgs):
        for msg in msgs:
            if msg != []:
                print(json.dumps(msg,indent=4))
                if msg['mesg'].lower() == 'music':
                    self.start_music()
                    print('Starter musikken...')
                elif msg['mesg'].lower() == 'stop':
                    print('Stopper musikken...')
                    self.player.terminate()
                elif msg['mesg'].lower() == 'up':
                    subprocess.call('pactl set-sink-volume @DEFAULT_SINK@ +50000'.split())
                elif msg['mesg'].lower() == 'down':
                    subprocess.call('pactl set-sink-volume @DEFAULT_SINK@ -50000'.split())

    
    def listen(self):
        while True:
            try:
                self.handle_message(self.p.read())
            except KeyboardInterrupt:
                os.system('clear')
                print('Exiting!')
                print('Exiting!')
                print('Exiting!')
                self.p.done()
                sys.exit(0)
            except:
                traceback.print_exc()

m = Musical()
m.listen()
