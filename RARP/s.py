import socket
s = socket.socket()
s.bind(('localhost', 5000))
s.listen(5)
print("Server is listening...")

c, addr = s.accept()
print(f"Connection established with {addr}")

address = {
    "6A:08:AA:C2":"165.165.80.80",
    "8A:BC:E3:FA":"165.165.79.1" 
}

while True:
    mac = c.recv(1024).decode()

    if not mac:  
        break

    try:
        ip = address[mac]  # Get the IP address for the mac
        print(f"MAC: {mac} -> IP: {ip}")
        c.send(ip.encode())  
    except KeyError:
        print(f"MAC: {mac} not found in RARP table.")
        c.send("Not Found".encode())
c.close()
s.close()