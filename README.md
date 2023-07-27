# Lambda API Tools

This repository is a collection of tools to use with [lambda labs gpu cloud compute infrastructure](https://lambdalabs.com/).  

## Setup
The tools depend on a `config.json` file at the root of the project directory. This is an example of the contents.
```
{
  "api_key": "xxx"
}
```
The only property that is needed in this file is `api_key` which you can create by going to [this link](https://cloud.lambdalabs.com/api-keys).  

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
