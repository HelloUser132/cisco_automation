import time
from netmiko import ConnectHandler as CH

R1 = {
    "device_type": "cisco_ios",
    "ip": "hashibros.com",
    "username": "alex",

}

device = input('Please enter your device: ')
net_connect = CH(**eval(device))
input1 = input('Please input your command')
output = net_connect.send_command(input1)
print(output)