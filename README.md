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

It displays the information in the terminal and saves a copy in the `logs/`
directory.

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
