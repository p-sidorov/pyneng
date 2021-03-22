# -*- Network:Network:coding: utf-8 -*-
"""
Задание 5.2

Запросить у пользователя ввод IP-сети в формате: 10.1.1.0/24

Затем вывести информацию о сети и маске в таком формате:

Network:
10        1         1         0
00001010  00000001  00000001  00000000

Mask:
/24
255       255       255       0
11111111  11111111  11111111  00000000

Проверить работу скрипта на разных комбинациях сеть/маска.

Подсказка: Получить маску в двоичном формате можно так:
In [1]: "1" * 28 + "0" * 4
Out[1]: '11111111111111111111111111110000'


Ограничение: Все задания надо выполнять используя только пройденные темы.
"""
inp = input('Введите адрес сети с маской вида 10.0.0.0/24: ')
ip = inp.split('/')
ip_addr = ip[0]
ip_mask = ip[1]
ip_addr = ip_addr.split('.')
ok1, ok2, ok3, ok4 = ip_addr
mask = ("1" * int(ip_mask) + "0" * (32 - int(ip_mask)))
mask1 = mask[0:8]
mask2 = mask[8:16]
mask3 = mask[16:24]
mask4 = mask[24:32]
mask1_2 = int(mask1, 2)
mask2_2 = int(mask2, 2)
mask3_2 = int(mask3, 2)
mask4_2 = int(mask4, 2)
print("Network:")
print('{0:<8} {1:<8} {2:<8} {3:<8}'.format(int(ok1), int(ok2), int(ok3), int(ok4)))
print('{0:08b} {1:08b} {2:08b} {3:08b}'.format(int(ok1), int(ok2), int(ok3), int(ok4)))
print()
print("Mask:")
mask_0 = '/'+ ip_mask
print(mask_0)
print('{0:<8} {1:<8} {2:<8} {3:<8}'.format(int(mask1_2), int(mask2_2), int(mask3_2), int(mask4_2)))
print(mask1, mask2, mask3, mask4)

