# Keylogger Program

This project demonstrates a **basic keylogger** implemented in Python. The keylogger captures and logs keystrokes along with additional system details, such as the current date, time, and MAC address, to a log file.

## 🚀 Features
- Logs every key pressed on the keyboard.
- Captures the **current date and time**.
- Retrieves and logs the **MAC address** of the system.
- Saves keystrokes and system details to a file (`keylog.txt`).

## 🛠 Requirements
- Python 3.x
- Required Libraries:
  - `pynput`: For capturing keyboard inputs.
  - `datetime`: For timestamping the logs.
  - `getmac`: For retrieving the MAC address of the system.

- Install the dependencies using pip:
```bash
pip install pynput getmac
```
## 📂 Files
`keylogger.py:` The main Python script for the keylogger.
`keylog.txt`: The output file where keystrokes and system details are stored.
## 🚦 Usage
1. Navigate to the project directory:
```bash
cd SCT_CS_4
```
2. Run the keylogger script:
```bash
python keylogger.py
```
3. Press keys on your keyboard. The strokes will be logged in the keylog.txt file.
4. To stop the keylogger, press the Esc key.

## ⚠️ Disclaimer
This project is intended for educational purposes only. Misuse of keyloggers is illegal and unethical. Always ensure you have permission to test keylogging software on any system.
