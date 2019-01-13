from pynput import *
import time
import os,sys
import glob
inp = input("enter keyword:")
file = inp + '.txt'

print(file)
# orig_stdout = sys.stdout
# f = open(file, 'w')
# sys.stdout = f
def on_click(x, y, button, pressed):
    if pressed:
        print('{0} {1} {2}'.format('click', x, y))
        print(time.time())

try:
    with mouse.Listener(on_click = on_click) as listener:
        listener.join()
except:
    print("Done")
# sys.stdout = orig_stdout
# f.close()
