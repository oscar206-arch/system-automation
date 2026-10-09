import getpass
import socket

name = getpass.getuser()
hostname = socket.gethostname()

print("SYSTEM INFORMATION")
print("==================")
print("System Information Tool")
print("Username:", name)
print("Hostname:", hostname)
