'''
    terminal_clearing.py

    contains function to clear terminal
'''
import os
import subprocess

def clear_terminal() -> None:
    if os.name == 'nt':
        subprocess.run('cls', shell=True)
    else:
        subprocess.run(['clear'])