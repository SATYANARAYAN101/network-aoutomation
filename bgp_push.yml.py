import yaml
from netmiko import ConnectHandler

with open("bgp.yml") as file:
    data = yaml.safe_load(file)

routers = data["routers"]

for router, details in routers.items():

    device = {
        "device_type": details["device_type"],
        "host": details["host"],
        "username": details["username"],
        "password": details["password"],
        "secret": details["password"]
    }

    print(f"\nConnect to {router}")

    connection = ConnectHandler(**device)
    connection.enable()

    config_commands = []

    # -------- Interface Configuration --------
    for interface in details["interfaces"]:
     config_commands.append(f"interface {interface['name']}")
     config_commands.append(f"ip address {interface['ip']} {interface['mask']}")
     config_commands.append("no shutdown")
     config_commands.append("exit")

    # -------- BGP Configuration --------
    config_commands.append(f"router bgp {details['asn']}")

    for neighbor in details["neighbors"]:
        config_commands.append(
            f"neighbor {neighbor['ip']} remote-as {neighbor['remote_as']}"
        )

    print("\nPushing Configuration")
    output = connection.send_config_set(config_commands)
    print(output)

    print("\nChecking BGP Neighborship")
    bgp_output = connection.send_command("show ip bgp summary")
    print(bgp_output)

    connection.disconnect()

print("\nAutomation Completed Successfully")
