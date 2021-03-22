config = "switchport trunk allowed vlan 1,3,10,20,30,100"
config_split = config.split()
#print(config_split)
vlans = config_split[-1].split(',')
print(vlans)
