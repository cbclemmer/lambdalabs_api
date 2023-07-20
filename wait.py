from sys import argv
from time import sleep, time

from util import get_avail, launch_inst, print_avail

if len(argv) < 2:
    raise Exception('Usage: python wait.py [gpu_name]')

def print_run_time(idx: int, total: int, start_time: float):
    run_time = time() - start_time
    print(f'Current Run time #{idx} of {total}: {run_time / 60 // 60}h {(run_time // 60) % 60}m {run_time % 60:.2f}s')

gpu_name = argv[1]
interval = 5 * 60

tries = 0
start_time = time()
while True:
    try:
        list_data = get_avail()
        gpu_data = list_data[gpu_name]
        avail = gpu_data['regions_with_capacity_available']
        if len(avail) == 0:
            print_avail(list_data)
            print('No availability')
            print_run_time(tries, 'inf', start_time)
            sleep(interval)
            continue
        launch_data = launch_inst(gpu_name, avail[0]['name'])
        ip = launch_data['ip']
        print('###############################################')
        print('###############################################')
        print('###############################################')
        print('##############STARTED INSTANCE#################')
        print('###############################################')
        print('###############################################')
        print('###############################################')
        print(f'IP: {ip}')
    except Exception as e:
        print(e)
        sleep(1)
        continue