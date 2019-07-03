# smarthome
Description： Conversational smart home based on raspberry pi
## usage
1. Configure the needed environment
``` 
run environment_config.sh
```
2. Run the following command, and then speak the control command of smart home.
```
python asrunit.py
```
3. You can also open the web page http://172.20.10.6:8088/myhome/index/ , which is on the same LAN as Raspberry pi. Note that 172.20.10.6 is the Raspberry pi's ip. You should change the ip to your own Raspberry pi's ip in the ALLOWED_HOST list in  Smarthome/settings.py. And then you can control the smart home through the button on the web.
