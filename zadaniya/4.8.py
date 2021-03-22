ip = "192.168.3.1"
ip = ip.split(".")
#ip = list(ip)
ok1, ok2, ok3, ok4 = ip
print('{0:<8} {1:<8} {2:<8} {3:<8}'.format(int(ok1), int(ok2), int(ok3), int(ok4)))
print('{0:08b} {1:08b} {2:08b} {3:08b}'.format(int(ok1), int(ok2), int(ok3), int(ok4)))
