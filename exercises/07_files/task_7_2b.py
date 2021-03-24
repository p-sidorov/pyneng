# -*- coding: utf-8 -*-
"""
Задание 7.2b

Переделать скрипт из задания 7.2a: вместо вывода на стандартный поток вывода,
скрипт должен записать полученные строки в файл

Имена файлов нужно передавать как аргументы скрипту:
 * имя исходного файла конфигурации
 * имя итогового файла конфигурации

При этом, должны быть отфильтрованы строки, которые содержатся в списке ignore
и строки, которые начинаются на '!'.

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""

ignore = ["duplex", "alias", "configuration"]
from sys import argv

config = argv[1]
dest = argv[2]
with open(config, 'r') as f, open(dest, 'w') as dest:
	for line in f:
		found_ignore = False
		for item in ignore:
			if item in line:
				found_ignore = True
				break
		if found_ignore:
			continue
		elif not line.startswith('!'):
			dest.write(line)

