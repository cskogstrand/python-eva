# python-eva
A python module for reading and changing status of eva devices through Eva High Level API. Compatible with Python3.

### Legal Disclaimer
This software is not affiliated with Datek Smart Home AS and the developers take no legal responsibility for the functionality or security of your Eva Smart Home and devices.


### Version History
```
0.0.1 Initial setup
```


## Command line usage

```
usage: eva.py [-h] [-i HOME_ID] [-c COOKIE]
                   username password environment
                   {homes, home}
                   ...

Read status of Eva devices

positional arguments:
  username              Eva username
  password              Eva password
  environment           Eva environment
  {homes, home}
                        commands
    homes               Get all homes for chosen environment
    home                Get a specific home

optional arguments:
  -h, --help            show this help message and exit
  -i HOME_ID, --home-id HOME_ID
                        Home Id of your home
  -c COOKIE, --cookie COOKIE
                           File to store cookie in

```


## Module usage

### Read all homes


```
import eva

session = eva.Session('user@example.com', 'mypassword', prod)
homes = session.get_homes()
print(homes["homes"])
```

### Read home by home id
```
import eva

session = eva.Session('user@example.com', 'mypassword', prod, home_id)
home = session.get_home(home_id)
print(home)
```
