from netmiko import ConnectHandler

router = {
    "device_type": "cisco_ios",
    "host": "192.168.196.133",
    "username": "satyanarayan",
    "password": "satya@123"
}

connection = ConnectHandler(**router)

output = connection.send_command("show ip interface brief")

print("===== Router Interfaces =====")
print(output)

connection.disconnect()
