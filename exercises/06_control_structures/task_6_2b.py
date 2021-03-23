# -*- coding: utf-8 -*-
"""
Задание 6.2b

Сделать копию скрипта задания 6.2a.

Дополнить скрипт: Если адрес был введен неправильно, запросить адрес снова.

Ограничение: Все задания надо выполнять используя только пройденные темы.
"""
while True:
	ip = input('Веведи IP: ')
	oks = ip.split('.')
	try:
		ok1, ok2, ok3, ok4 = oks
		ok1 = int(ok1)
		ok2 = int(ok2)
		ok3 = int(ok3)
		ok4 = int(ok4)
		if ip.startswith('255.255.255.255'):
			print('local broadcast')
			break
		elif ip.startswith('0.0.0.0'):
			print('unassigned')
			break
		elif ok1 < 0:
			print('Неправильный IP-адрес')
		elif ok1 < 224:
			print('unicast')
			break
		elif ok1 < 240:
			print('multicast')
			break
		elif ok1 > 256:
			print('Неправильный IP-адрес')
		else:
			print('unused')
			break
	except ValueError:
	        print("Неправильный IP-адрес")

