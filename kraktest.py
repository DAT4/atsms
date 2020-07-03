import phone
import time
import find_krak.krak as krak

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
        if message['mesg'].lower().startswith('whois:'):
            try:
                number = message['mesg'].split(':')[1]
                p = krak.find_person(number)
                msg = p['name'].replace('å', 'aa')
                msg += '\n'
                msg += p['address'][0]['streetName'] + ' ' + p['address'][0]['streetNumber']
                msg += '\n'
                msg += p['address'][0]['postCode'] + ' ' + p['address'][0]['postArea']
                print(msg)
                self.phone.write(msg, message['from'])
            except:
                self.phone.write('Der skete en fejl', message['from'])


l = Listener()
