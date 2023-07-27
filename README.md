# Lambda API Tools

This repository is a collection of tools to use with [lambda labs gpu cloud compute infrastructure](https://lambdalabs.com/).  

## Setup
The tools depend on a `config.json` file at the root of the project directory. This is an example of the contents.
```
{
  "api_key": "xxx",
  "check_interval": 5,
  "wait_interval": 1
}
```
`api_key`: api key for lambda labs, you can create by going to [this link](https://cloud.lambdalabs.com/api-keys).  
`check_interval`: number of minutes to wait when running `check.py`, defaults to 5  
`wait_interval`: number of minutes to wait when running `wait.py`, defaults to 1  
  
## Tools

### check.py
Contiously checks for availability and prints the currently available instances and the locations they are available at to the terminal. The check is run every 5 minutes.
  python wait.py [gpu_name]
### start.py
starts a new instance assuming the gpu and location is available.  
*Usage:* `python start.py  [gpu_name] [region_name]`

### wait.py
Continously checks for availability of a particular gpu and launches an instance at the first oppertunity. The terminal will display the ip address of the started machine after it has launched.  
*Usage:* `python wait.py [gpu_name]`
