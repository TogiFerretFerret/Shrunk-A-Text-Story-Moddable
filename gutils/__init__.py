import os  # The os module for making a user interface
import time  # Importing the time module... to add suspense!
from replit import db
from pyfiglet import Figlet
from colored import fore, style
import fkeycapture as fkey  # Better menus 😀
import sys
import termios
import tty

# Custom print system
def printt(text: str, delay: float = 0.1, newline: bool = True) -> None:
    # Store the current terminal settings
    original_terminal_settings = termios.tcgetattr(sys.stdin)  # type: ignore

    # Change terminal settings to prevent arrow key interruptions
    tty.setcbreak(sys.stdin)  # type: ignore

    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)

    if newline:
        print()
    # Restore the original terminal settings
    termios.tcsetattr(sys.stdin, termios.TCSADRAIN,
                      original_terminal_settings)  # type: ignore
    return