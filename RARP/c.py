import socket
c = socket.socket()
c.connect(('localhost', 5000))

while True:
    mac = input("Enter MAC address to find IP (or type 'exit' to quit): ")

    if mac.lower() == "exit":  
        break

    c.send(mac.encode())
    ip = c.recv(1024).decode()
    print(f"IP Address for {mac}: {ip}")
c.close()