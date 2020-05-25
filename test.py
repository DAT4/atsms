import phone

mag = 'Godmorgen min elskede! <3'
mod = '+4542708118'
phone = phone.Phone()
phone.write(mag,mod)
inbox = phone.read()
print(inbox)
phone.done()
