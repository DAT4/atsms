from phone import Phone

p = Phone("/dev/ttyUSB2")
p.unlock('3451')
p.write('hejsa','+4542708118')
p.done()
