from time import sleep
from util import print_avail

interval = 5 * 60

while True:
    try:
        print_avail()
        sleep(interval)
    except Exception as e:
        print(e)
        sleep(1)
        continue