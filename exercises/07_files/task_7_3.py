# -*- coding: utf-8 -*-

"""
Задание 7.3

Скрипт должен обрабатывать записи в файле CAM_table.txt. Каждая строка,
где есть MAC-адрес, должна быть обработана таким образом, чтобы
на стандартный поток вывода была выведена таблица вида:

100      01bb.c580.7000      Gi0/1
200      0a4b.c380.7c00      Gi0/2
300      a2ab.c5a0.700e      Gi0/3
10       0a1b.1c80.7000      Gi0/4
500      02b1.3c80.7b00      Gi0/5
200      1a4b.c580.7000      Gi0/6
300      0a1b.5c80.70f0      Gi0/7
10       01ab.c5d0.70d0      Gi0/8
1000     0a4b.c380.7d00      Gi0/9


Ограничение: Все задания надо выполнять используя только пройденные темы.

"""

dynamic = '----    -----------       --------    -----'
with open('CAM_table.txt', 'r') as f:
	for line in f:
		line = line.rstrip()
		if dynamic in line:
			for line in f:
				line = line.split()
				vlan, mac, mode, interface = line
				new_line = (vlan + "    " + mac + "    " + interface)
				print(new_line)
#				print("{:5}".format(vlan), "{:5}".format(mac), "{:5} ".format(interface))
