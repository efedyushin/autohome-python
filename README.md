# Autohome-Python

**WARNING: DON'T USE FOR PRODUCTION NOW**

Autohome is a simple server for emulate control services for smart-home devices in local network.



### Installation

Autohome requires [Python](https://www.python.org/downloads/) <3.6 to run.


Create virtualenv and install the dependencies.

```sh
$ cd autohome-python
$ python3 -m venv .env
$ source .env/bin/activate
$ pip install -r requirements.txt
```
Create *config/config.yaml* from template.
```sh
$ mv config/config.example.yaml config/config.yaml 
```
Start server.
```sh
 python -m server -c config/config.yaml
 ```



