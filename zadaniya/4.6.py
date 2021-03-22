ospf_route = "	10.0.24.0/24 [110/41] via 10.0.13.3, 3d18h, FastEthernet0/0"
ospf_route = ospf_route.replace('[', '').replace(']', '').replace(',', '').split()
ospf_route.remove('via')
print('Prefix:            ',"{:<1}".format(ospf_route[0]))
print('AD/Metric:         ',"{:<1}".format(ospf_route[1]))
print('Next-Hop:          ',"{:<1}".format(ospf_route[2]))
print('Last update:       ',"{:<1}".format(ospf_route[3]))
print('Outbound Interface:',"{:>100}".format(ospf_route[4]))
