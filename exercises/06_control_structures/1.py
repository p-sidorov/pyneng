trunk_template = [
    "switchport trunk encapsulation dot1q",
    "switchport mode trunk",
    "switchport trunk allowed vlan",
]

trunk = {"0/1": ["add", "10", "20"], "0/2": ["only", "11", "30"], "0/4": ["del", "17"]}
for i in trunk:
	if trunk[i][0].startswith('add'):
		print("add")
	elif trunk[i][0].startswith('del'):
		print("remove")
	elif trunk[i][0].startswith('only'):
		print("only")

for intf, vlan in trunk.items():
	print("interface FastEthernet " + intf)
	for command in trunk_template:
		if command.endswith("access vlan"):
			print(f" {command} {vlan}")
		else:
			print(f" {command}")
