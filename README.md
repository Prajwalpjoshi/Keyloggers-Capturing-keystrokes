# Keylogger Security Research Project

## Overview

This project is a cybersecurity learning and research-based application developed using Python. The purpose of the project is to understand how keystroke logging works, how monitoring tools capture user input, and how endpoint security systems detect such behavior.

The application captures keyboard events and stores the logs in both text and JSON formats for educational and authorized security testing environments only.

> ⚠️ Disclaimer:
> This project was created strictly for educational purposes, cybersecurity learning, and authorized testing in controlled environments. Unauthorized use of keylogging software on systems without explicit permission is illegal and unethical.

---

## Features

* Capture keyboard keystrokes
* Detect key press and key release events
* Store logs in `.txt` format
* Store structured logs in `.json` format
* Simple GUI using Tkinter
* Event-based keyboard monitoring using `pynput`

---

## Technologies Used

* Python
* Tkinter
* pynput
* JSON

---

## Project Structure

```bash
├── Keylogger.py
├── logs.txt
├── logs.json
└── README.md
```

---

## How It Works

1. The application launches a simple Tkinter GUI.
2. A keyboard listener monitors key press and release events.
3. Captured events are stored:

   * In `logs.txt`
   * In `logs.json`
4. The application continuously updates logs while running.

---

## Installation

### Clone Repository

```bash
git clone https://github.com/Prajwalpjoshi/Keyloggers-Capturing-keystrokes.git
cd Keyloggers-Capturing-keystrokes
```

### Install Dependencies

```bash
pip install pynput
```

---

## Run the Application

```bash
python Keylogger.py
```

---

## Learning Outcomes

Through this project, I gained understanding of:

* Keyboard event handling
* Python GUI development
* File handling in Python
* JSON data storage
* Endpoint monitoring concepts
* Security awareness and ethical cybersecurity practices

---

## Future Improvements

* Encrypted log storage
* Secure authentication
* Monitoring dashboard
* Threat detection alerts
* Activity visualization

---

## Author

Prajwal Joshi
