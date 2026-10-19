# System Automation

A simple Python automation tool that collects essential system information,
displays a formatted report, and saves the report to a timestamped log file.

## Features

The script collects the following information:

- Current timestamp
- Logged-in username
- Hostname
- Operating system
- Operating system release
- Python version
- Local IPv4 address

The report is displayed in the terminal and saved in the `logs/` directory.

## Requirements

- Python 3
- Linux or WSL environment

The project uses Python's standard library and requires no external packages.

## Project Structure

```text
system-automation/
├── system_info.py
├── README.md
├── requirements.txt
├── .gitignore
└── logs/
    └── Generated report files
```

## Usage

Run the script from the project directory:

```bash
python3 system_info.py
```

The script collects the system information, displays a formatted report,
and saves it to a timestamped file in `logs/`.

## Example Output File

```text
logs/system_info_20261019_150024.log
```

Each report filename includes the date and time when it was generated.

## Dependencies

No external Python packages are required. The `requirements.txt` file is
intentionally empty because the script uses only the Python standard library.

## Purpose

This project demonstrates practical Python automation skills, including
system information collection, basic network information retrieval,
formatted terminal output, and file handling.
