# -*- coding: utf-8 -*-
"""
Задание 7.3b

Сделать копию скрипта задания 7.3a.

Переделать скрипт:
- Запросить у пользователя ввод номера VLAN.
- Выводить информацию только по указанному VLAN.

Пример работы скрипта:

Enter VLAN number: 10
10       0a1b.1c80.7000      Gi0/4
10       01ab.c5d0.70d0      Gi0/8

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""
number = input('Enter VLAN number: ')
result = []
result1 = []
dynamic = 'DYNAMIC'
with open('CAM_table.txt', 'r') as f:
    for line in f:
        if dynamic in line:
            line = line.split()
            result.append(line)
    for vlan in result:
        if number in vlan:
            result1.append(vlan)
for vlan in result1:
	print(vlan[0],'   ',vlan[1],'   ',vlan[3])


