command1 = "switchport trunk allowed vlan 1,2,3,5,8"
command2 = "switchport trunk allowed vlan 1,3,8,9"
vl1 = command1.split()
vl2 = command2.split()
vlans1 = vl1[-1].split(',')
vlans2 = vl2[-1].split(',')
vlans1 = set(vlans1)
vlans2 = set(vlans2) 
vlans = vlans1 & vlans2
#print(vlans)
vlans = list(vlans)
print(vlans)
print(type(vlans))
result = sorted(vlans)
print(result)
