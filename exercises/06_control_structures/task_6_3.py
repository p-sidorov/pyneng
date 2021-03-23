trunk_template = [
    "switchport trunk encapsulation dot1q",
    "switchport mode trunk",
    "switchport trunk allowed vlan",
]

trunk = {"0/1": ["add", "10", "20"], "0/2": ["only", "11", "30"], "0/4": ["del", "17"]}

for intf, vlan in trunk.items():
    print("interface FastEthernet " + intf)
    for command in trunk_template:
        if command.endswith("allowed vlan"):
            if trunk[intf][0].startswith('add'):
                print(f" switchport trunk encapsulation dot1q")
                print(f" switchport mode trunk")
                vlans = trunk[intf]
                vlans.remove("add")
                vlans = str(vlans)
                vlans = vlans.strip('[]').replace("'", '').replace(" ", '')
                print(f" {command} " f"add " f"{vlans}")
            elif trunk[intf][0].startswith('del'):
                print(f" switchport trunk encapsulation dot1q")
                print(f" switchport mode trunk")
                vlans = trunk[intf]
                vlans.remove("del")
                vlans = str(vlans)
                vlans = vlans.strip('[]').replace("'", '').replace(" ", '')
                print(f" {command} " f"remove " f"{vlans}")
            elif trunk[intf][0].startswith('only'):
                print(f" switchport trunk encapsulation dot1q")
                print(f" switchport mode trunk")
                vlans = trunk[intf]
                vlans.remove("only")
                vlans = str(vlans)
                vlans = vlans.strip('[]').replace("'", '').replace(" ", '')
                print(f" {command} " f"{vlans}")

