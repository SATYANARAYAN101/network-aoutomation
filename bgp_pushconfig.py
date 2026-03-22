from netmiko import ConnectHandler

from netmiko.exceptions import NetMikoTimeoutException, NetMikoAuthenticationException

routers = [
    {
        "device_type": "cisco_ios",
        "host": "192.168.196.133",
        "username": "satyanarayan",
        "password":  "satya@123",
        "config":[
            "router bgp 10",
            "neighbor 192.168.200.2 remote-as 30",
            "network 1.1.1.0 mask 255.255.255.0"

        ]
    },

    {
        "device_type": "cisco_ios",
        "host": "192.168.200.2",
        "username": "admin",
        "password": "admin",
        "config":[
            "router bgp 30",
            "neighbor 192.168.196.133 remote-as 10",
            "network 2.2.2.0 mask 255.255.255.0"
        ]

    }
        
    
]
for router in routers:
     try:
         connection= ConnectHandler(
              device_type = router["device_type"],
              host = router["host"],
              username = router["username"],
              password = router["password"]

         )
         print(f"connecte to {router['host']}")
         output = connection.send_config_set(router['config'])
         print(output)
         connection.disconnect()

     except NetMikoAuthenticationException:
        print(f"Authentication failed for {router['host']}")

     except NetMikoTimeoutException:
        print(f"Timeout: Cannot reach {router['host']}")
     except Exception as e:
        print(f"Error on {router['host']} : {e}")
