import time
from C7E25 import *

@clock('{name}:{elapsed}s') # elapsed 消逝 from Bing Dictionary
def snooze(seconds):
    time.sleep(seconds)

for i in range(3):
    snooze(.123)