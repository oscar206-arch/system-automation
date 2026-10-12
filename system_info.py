import getpass
import socket
import platform
from datetime import datetime
from pathlib import Path


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


def generate_report(info):
    """Format system information as a readable report."""

    lines = [
        "",
        "=" * 45,
        "       SYSTEM INFORMATION REPORT",
        "=" * 45,
    ]

    for label, value in info.items():
        lines.append(f"{label:<22}: {value}")

    lines.append("=" * 45)

    return "\n".join(lines) + "\n"


def save_report(report):
    """Save the report to a timestamped log file."""

    log_directory = Path("logs")
    log_directory.mkdir(parents=True, exist_ok=True)

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    log_file = log_directory / f"system_info_{timestamp}.log"

    with log_file.open("w", encoding="utf-8") as file:
        file.write(report)

    return log_file


if __name__ == "__main__":
    system_info = collect_system_info()
    report = generate_report(system_info)

    print(report)

    saved_file = save_report(report)
    print(f"Report saved to: {saved_file}")
