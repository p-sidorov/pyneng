# -*- coding: utf-8 -*-
"""
Задание 7.1

Обработать строки из файла ospf.txt и вывести информацию по каждой строке в таком
виде на стандартный поток вывода:

Prefix                10.0.24.0/24
AD/Metric             110/41
Next-Hop              10.0.13.3
Last update           3d18h
Outbound Interface    FastEthernet0/0

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""
with open('ospf.txt', 'r') as f:
	for line in f:
		l1 = line.replace('[', '').replace(']', '').replace(',', '').split()
		l1.remove('via')
		l1.remove('O')
		print('Prefix            ',"{:<1}".format(l1[0]))
		print('AD/Metric         ',"{:<1}".format(l1[1]))
		print('Next-Hop          ',"{:<1}".format(l1[2]))
		print('Last update       ',"{:<1}".format(l1[3]))
		print('Outbound Interface',"{:>0}".format(l1[4]))

