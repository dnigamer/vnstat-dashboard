# vnstat-dashboard
This is basically a traffic usage monitor using vnStat (for measuring) and vnStati (for graphical design). This whole dashboard runs in Python 3 using Flask and it requires "almost" no configuration.

## How to install it
To start, you need to install git, python3 and vnstat on your machine.

### Ubuntu / Debian
```
sudo apt install git python3 python3-pip vnstat vnstati
```

### CentOS / RHEL
```
yum install git python3 python3-pip vnstat vnstati
```

### Arch Linux / Manjaro Linux
```
pacman -S git python3 python3-pip vnstat vnstati
```
(search on Google how to install git, python3 and vnstat in your distro if it's not here)

### After installing
Run the following command in a empty folder
```
git clone https://github.com/dnigamer/vnstat-dashboard
```
and wait to finish.

### After cloning the repository
Run the next commands to get it installed
```
cd vnstat-dashboard
```
Then install the requirements to run the script
```
python3 -m pip install -r requirements.txt
```
And the needed installations are now done

## Configuration
You will need to configure some things such as the interface name and the update interval (if you want to enable).

To do that, you need to open the ```config.py``` file. There you'll find 3 different variables:

### Webserver port
In this variable you can define what port you want Flask's web server to use to host your dashboard.

Port 8000 for example:
```
web_port = 8000
```

### Interface name
In this variable you need to input the interface name to track.
```
iface_name = "interface name"
```

### Looping
In this variable you can choose from having the script to update the stats for you or you can just click on the "Force system reload" button in the dashboard.

You can pick from ``True`` to ``False`` being ``True`` to activate looping and ``False`` to not activate looping.

Activated looping example:
```
looping = True
```

### Looping update interval
In this variable you can pick how much **seconds** to wait to repeat again the image generation from vnStati.

5 minutes example:
```
update_interval = 300
```

**Remember that vnStat only updates it's database 5 in 5 minutes!!**

## Running
To finally run it, you need to have the port 8000 free. You can also change it in the ``config.py`` file if needed.

Run it this way:
```
python3 main.py
```
And done! Just access it through ``localhost:8000`` or ``<your_IP_address>:8000``

## About
I made this in under a day so it might have some bugs and such, yeaaa...

If you find any, please do not hesitate to create a new issue in the issues page!!

If you want to support me and my work, just do a donation for my PayPal [here](https://paypal.me/dnigamer). 

Thank you!!