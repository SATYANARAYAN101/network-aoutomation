import yaml
import logging
from netmiko import ConnectHandler

logging.basicConfig(
    filename="health_check.log",
    level=logging.INFO,
    format="%(asctime)s - %(message)s"
)

with open("inventory.yaml") as file:
    devices = yaml.safe_load(file)["devices"]

for device in devices:

    host = device["host"]

    print("\nConnecting to", host)

    connection = ConnectHandler(**device)

    connection.enable()

    ospf = connection.send_command("show ip ospf neighbor")
    bgp = connection.send_command("show ip bgp summary")

    if "FULL" in ospf:
        print("OSPF OK")
    else:
        print("OSPF ISSUE")

    if "Estab" in bgp:
        print("BGP OK")
    else:
        print("BGP DOWN")

    connection.disconnect()
