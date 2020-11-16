# GVE_DevNet_Meraki_MX_Firewall_Provisioner
prototype code to provision L3 and L7 firewall rules to selected Meraki networks


## Contacts
* Jorge Banegas

## Solution Components
* Meraki
*  MX

## Installation/Configuration

This is as a template, project owner to update

1. First step will be to include your personal api key inside the config.py file for the script to use

```python
    api_key=""
    
```
2. Next will be to edit the l3 and l7 json files that will help provision the firewall rules. 

Make sure to visit https://developer.cisco.com/meraki/api-v1/#!update-network-appliance-firewall-l-3-firewall-rules and https://developer.cisco.com/meraki/api-v1/#!update-network-appliance-firewall-l-7-firewall-rules for reference

```python
    
[
    {
        "comment": "test",
        "policy": "allow",
        "protocol": "tcp",
        "destPort": "443",
        "destCidr": "192.168.1.0/24",
        "srcPort": "Any",
        "srcCidr": "Any",
        "syslogEnabled": "false"
    }
]
    
```

3. create virtual environment and name it env, then activate it

```console
foo@bar:~$ virtualenv env
foo@bar:~$ source env/bin/activate
```

4. install the dependencies required for the python script
```console
foo@bar(env):~$ pip install -r requirements.txt
```

5. run python script
```console
foo@bar(env):~$ python main.py
```

# Notes
- If a firewall rule depends on specific LAN configurations, the script will error out. Make sure within these firewall rules, that given subnets have already been declared.

![/IMAGES/step1.png](/IMAGES/error.png)

# Screenshots
MX configuration before launching the script

![/IMAGES/before_script.png](/IMAGES/before_script.png)

Firewall L3 and L7 rules declared in the json files

![/IMAGES/layer7_rules.png](/IMAGES/layer7_rules.png)

![/IMAGES/layer3_rules.png](/IMAGES/layer3_rules.png)

1st step

![/IMAGES/step1.png](/IMAGES/step1.png) 

2nd step

![/IMAGES/step2.png](/IMAGES/step2.png)

MX configuration after launching the script

![/IMAGES/before_script.png](/IMAGES/after_script.png)

![/IMAGES/0image.png](/IMAGES/0image.png)

### LICENSE

Provided under Cisco Sample Code License, for details see [LICENSE](LICENSE.md)

### CODE_OF_CONDUCT

Our code of conduct is available [here](CODE_OF_CONDUCT.md)

### CONTRIBUTING

See our contributing guidelines [here](CONTRIBUTING.md)

#### DISCLAIMER:
<b>Please note:</b> This script is meant for demo purposes only. All tools/ scripts in this repo are released for use "AS IS" without any warranties of any kind, including, but not limited to their installation, use, or performance. Any use of these scripts and tools is at your own risk. There is no guarantee that they have been through thorough testing in a comparable environment and we are not responsible for any damage or data loss incurred with their use.
You are responsible for reviewing and testing any scripts you run thoroughly before use in any non-testing environment.
