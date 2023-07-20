import requests
import json

config_file = open('config.json', 'r')
config = json.loads(config_file.read())
config_file.close()

if 'api_key' not in config:
    raise Exception('no api key')

def get_avail():
    res = requests.get('https://cloud.lambdalabs.com/api/v1/instance-types', headers={
        "Authorization": f"Basic {config['api_key']}"
    })
    if res.status_code != 200:
        raise Exception(f'Error: code {res.status_code}\n{res.content.decode()}')
    return json.loads(res.content.decode())['data']

def launch_inst(gpu_name: str, region_name: str):
    data = get_avail()
    found = False
    for region in data[gpu_name]['regains']['regions_with_capacity_available']:
        if region['name'] == region_name:
            found = True
            break
    if not found:
        raise Exception('Instance not available')
    res = requests.post('https://cloud.lambdalabs.com/api/v1/instance-operations/launch', headers={
        "Authorization": f"Basic {config['api_key']}"
    }, json={
        'region_name': region_name,
        'instance_type_name': gpu_name,
        'ssh_key_names': [ 'lambda_test' ],
        'file_system_names': [ 'Llama' ]
    })
    if res.status_code != 200:
        raise Exception(f'Error creating instance, status code: {res.status_code}\n{res.content.decode()}')
    id = int(json.loads(res.content.decode())['data']['instance_ids'][0])
    res = requests.get(f'https://cloud.lambdalabs.com/api/v1/instances/{id}')
    if res.status_code != 200:
        raise Exception(f'Error retrieving instance data, status code: {res.status_code}\n{res.content.decode()}')
    return json.loads(res.content.decode())['data']

def print_avail(data = None):
    if data is not None:
        data = get_avail()
    for key in data.keys():
        gpu_data = data[key]
        availability = ''
        for loc in gpu_data['regions_with_capacity_available']:
            availability += loc['name'] + '\n'
        if availability == '':
            continue
        print(f'{key}:\n{availability}\n')