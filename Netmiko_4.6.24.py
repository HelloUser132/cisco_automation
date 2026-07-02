from netmiko import ConnectHandler as ConH
import getpass


print('Please enter your password: ')
PASSWD1 = getpass.getpass()
print('Please enter your enable secret: ')
PASSWD2 = getpass.getpass()



R1 = {"device_type": "cisco_ios",
      "host": "hashibros.com",
      "username": "alex",
      "password": PASSWD1,
      "secret": PASSWD2

}


config = ['int range g0-7', 'shut']
config2 = ['int range g0-7', 'no shut']

devices = [R1]


for device in devices:
    net_connect = ConH(eval(**devices))
    net_connect.enable
    output = net_connect.send_config_set(config)
