import sys

from util import launch_inst

if len(sys.argv) < 3:
    raise Exception('Usage python start.py [gpu_name] [region_name]')

gpu_name = sys.argv[1]
region_name = sys.argv[2]

data = launch_inst(gpu_name, region_name)

id = data['id']
ip = data['ip']

print(f""""
ID: {id}
IP: {ip}
""")