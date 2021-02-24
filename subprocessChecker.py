import subprocess
import time

p1 = subprocess.Popen('python pygletGIF.py')
# p2 = subprocess.Popen('sort /R', shell=True, stdin=p1.stdout)
time.sleep(2)
p1.kill()
# out, err = p2.communicate()