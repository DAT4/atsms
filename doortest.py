import phone
import time
import client

class Listener:
    def __init__(self):
        self.phone = phone.Phone()
        #self.phone.unlock()
        while(True):
            x = self.phone.read(mode='new')
            if x != None and x != []:
                for i in x:
                    print(i)
                    self.handle_message(i)
            time.sleep(1)

    def handle_message(self, message):
        if message['mesg'].lower() == ('open'):
            client.send()



l = Listener()

