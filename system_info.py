import getpass
import socket
import platform

name = getpass.getuser()
hostname = socket.gethostname()


print("SYSTEM INFORMATION")
print("==================")
print("System Information Tool")
print("Username:", name)
print("Hostname:", hostname)




