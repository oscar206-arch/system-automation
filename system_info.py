import getpass
import socket
import platform

def get_local_ip():

    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    try:
         sock.connect(("192.0.2.1", 80))
         return sock.getsockname()[0]

    except OSError:
        return "Unavailable"

    finally:
        sock.close()


name = getpass.getuser()
hostname = socket.gethostname()
operating_system = platform.system()
os_release = platform.release()
python_version = platform.python_version()
local_ip = get_local_ip()

print("SYSTEM INFORMATION")
print("==================")
print("System Information Tool")
print("Username:", name)
print("Hostname:", hostname)
print("Operating System:", operating_system)
print("OS Release:", os_release)
print("Python Version:", python_version)
print("Local IPV4 Address:", local_ip)
