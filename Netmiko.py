from netmiko import ConnectHandler
import time
import getpass


#passwd = getpass.getpass('Enter device password: ')


R1 = {
    "device_type": "cisco_ios",
    "ip": "hashibros.com",
    "username": "alex",
'

}

R2 = {
    "device_type": "cisco_ios",
    "ip": "blablatest.com",
    "username": "alex",
    "password": "Enderm@n13579"

}



def Connect():
    while True:
            device = input('Please enter a device to connect to (by hostname): ')
            #WARNING: eval allows execution of arbitrary code!!!
            net_connect = ConnectHandler(**eval(device))
            net_connect.enable()
            print('Connected successfully.')
            return net_connect
            print('Error, hostname/device not found or connection failed.')
            continue



def Control():
    net_connect = Connect()
    while True:
        command = input('Enter your command: ')
        if 'exit' in command:
            print('Goodbye!')
            net_connect.disconnect
            break
        else:
            output = net_connect.send_command_timing(command)
            print(output)
            continue


def Choice():
    print('Please make a selection from the following menu: \n1. Enter custom commands on a device. \n2. Choose config. file to send to device')
    time.sleep(1)
    user_input = input('> ')
    while True:
        if str(1) in user_input:
            Control()





Control()
#Choice()
#with open('test.txt', 'r') as document:
#    print(document.read())