from time import sleep
from util import print_avail, get_config

config = get_config()

if not 'check_interval' in config:
    config['check_interval'] = 5

while True:
    try:
        print_avail()
        sleep(config['check_interval'] * 60)
    except Exception as e:
        print(e)
        sleep(1)
        continue