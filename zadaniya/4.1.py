nat = "ip nat inside source list ACL interface FastEthernet0/1 overload"
nat1 = nat.replace('Fast', 'Gigabit')
print(type(nat1))
print(nat1)
