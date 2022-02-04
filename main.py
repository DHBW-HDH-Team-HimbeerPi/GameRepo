import subprocess
import os

os.chdir('..')
os.chdir('./raspberry-cementary/Pong')
os.system('python3 main.py')
subprocess.Popen(['ls', '-l'])
