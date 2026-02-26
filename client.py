import socket

# Create a TCP socket (IPv4)
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Set a timeout to avoid infinite waiting
client.settimeout(5)

# Connect to the server
client.connect(("127.0.0.1", 5000))

# Ask the student for their name
student_name = input("Ingresa tu nombre: ")

# Send the name to the server
client.sendall(student_name.encode())

# Receive the server response
message = client.recv(1024).decode()
print(message)

# Close the connection
client.close()
