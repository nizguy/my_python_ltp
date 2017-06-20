import socket

s = socket.socket()
host = socket.gethostname()
port = 3333
s.bind((host,port))

s.listen(5)
while True:
    c, addr = s.accept()
    print "Connection Made From: ", addr
    c.send('Thanks For Connecting Today')
    c.close()
    
