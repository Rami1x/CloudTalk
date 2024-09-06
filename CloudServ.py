import socket

try:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print("Socket works!")
except socket.error as err:
    print("Socket failed: Error %s" %(err))

HOST = socket.gethostname()     #SERVER HOST
PORT = 6543     #SERVER PORT

sock.bind((HOST, PORT))


try:
    sock.listen(3)
    print("Socket is listening...")
except:
    print("Socket is not listening, error ;(")

## setting eberythig up slowlyidk wehn finish lol