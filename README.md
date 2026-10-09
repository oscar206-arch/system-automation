# System Automation

A Python-based system information tool designed to automate the collection of basic information from a Linux system.

## Purpose

The purpose of this project is to demonstrate how Python can be used to automate common IT system administration tasks.

The tool currently collects:

- Current username
- System hostname

## Technologies

- Python 3
- Linux / WSL

## Current Features

- Automatically detects the current username
- Automatically detects the system hostname
- Displays collected information in the terminal

## Project Structure

```text
system-automation/
├── README.md
├── logs/
├── requirements.txt
└── system_info.py

```

Then add:

````markdown
## Usage

Run the program with:

```bash
python3 system_info.py
```

## Example Output

```text
SYSTEM INFORMATION
==================
System Information Tool
Username: oscar
Hostname: DESKTOP-D6KOOO8
```

## Project Status

In development.
