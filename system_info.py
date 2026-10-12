import getpass
import socket
import platform
from datetime import datetime


def get_local_ip():
    """Return the local IPv4 address selected for the outgoing route."""
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    try:
        sock.connect(("192.0.2.1", 80))
        return sock.getsockname()[0]

    except OSError:
        return "Unavailable"

    finally:
        sock.close()


def collect_system_info():
    """Collect basic system and network information."""

    return {
        "Timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "Username": getpass.getuser(),
        "Hostname": socket.gethostname(),
        "Operating System": platform.system(),
        "OS Release": platform.release(),
        "Python Version": platform.python_version(),
        "Local IPv4 Address": get_local_ip(),
    }


def display_report(info):
    """Display the collected information in a readable format."""

    print()
    print("=" * 45)
    print("       SYSTEM INFORMATION REPORT")
    print("=" * 45)

    for label, value in info.items():
        print(f"{label:<22}: {value}")

    print("=" * 45)
    print()


if __name__ == "__main__":
    system_info = collect_system_info()
    display_report(system_info)
