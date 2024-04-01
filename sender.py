from socket import *

file = input("Enter your file for send :")
file = open(file,"rb")
data = file.read()
file.close
ip = str(input("Enter Server IP:"))
port = int(input("Enter server port:"))

sock = socket(AF_INET,SOCK_STREAM)
sock.connect((ip,port))

        
while True:
    if len(data) > 0:
        temp_data = data[0:1024]
        if len(temp_data) < 1024:
            temp_data += chr(0).encode() * (1024 - len(temp_data))
            
        data =data[1024:]

        sock.send(temp_data)
        print("*", end = "")
    else:
        sock.send(b"Ended")
        print(" END :)")
        sock.close()
        break