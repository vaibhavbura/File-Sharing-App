from socket import *

ip = str(input(" Enter Server IP: "))
port = int(input(" Enter Server Port: "))


sock = socket (AF_INET, SOCK_STREAM)

sock.bind((ip, port))
print(" please wait for sender... ")
sock.listen(1)

sender, addr = sock.accept()

data = b""
while True:
    end_data = sender.recv(1024)

    if end_data == b"Ended":
        print(" END :)")
        break
    data += end_data

file_name = input(" output File Name: ")
new_file = open(file_name, "wb")
new_file.write(data)
new_file.close()