import socket
user_name=socket.gethostname()
#ip=socket.gethostbyname(socket.gethostname())
ip=socket.gethostbyname(socket.getfqdn())
print ip
print user_name

