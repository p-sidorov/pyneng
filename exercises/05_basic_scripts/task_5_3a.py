# -*- coding: utf-8 -*-
"""
Задание 5.3a

Дополнить скрипт из задания 5.3 таким образом, чтобы, в зависимости
от выбранного режима, задавались разные вопросы в запросе о номере
VLANа или списка VLANов:
* для access: 'Введите номер VLAN:'
* для trunk: 'Введите разрешенные VLANы:'

Ограничение: Все задания надо выполнять используя только пройденные темы.
То есть эту задачу можно решить без использования условия if и циклов for/while.
"""

access_template = [
    "switchport mode access",
    "switchport access vlan {}",
    "switchport nonegotiate",
    "spanning-tree portfast",
    "spanning-tree bpduguard enable",
]

trunk_template = [
    "switchport trunk encapsulation dot1q",
    "switchport mode trunk",
    "switchport trunk allowed vlan {}",
]

template = {
        'access': {
                'c1': 'switchport mode access',
                'c2': 'switchport access vlan {}',
                'c3': 'switchport nonegotiate',
                'c4': 'spanning-tree portfast',
                'c5': 'spanning-tree bpduguard enable',
},
        'trunk': {
                'c1': 'switchport trunk encapsulation dot1q',
                'c2': 'switchport mode trunk',
                'c3': 'switchport trunk allowed vlan {}',
    },
}
mode = input('Enter interface mode access/trunk : ')
inter = input('Enter interface type and number: ')
ask = {'access': 'Введите номер VLAN: ', 'trunk': 'Введите разрешенные VLANы:'}
ask1 = ask[mode]
vlans = input(ask1)
new_cmd1 = 'switchport access vlan' 
new_cmd2 = new_cmd1 +  ' ' + vlans
new_cmd3 = 'switchport trunk allowed vlan' 
new_cmd4 = new_cmd3 +  ' ' + vlans

template['access']['c2'] = new_cmd2
template['trunk']['c3'] = new_cmd4
 
dict_tmp = (template[mode])
print('----------------------')
print("interface",inter)
print(dict_tmp.get('c1'))
print(dict_tmp.get('c2'))
print(dict_tmp.get('c3'))
print(dict_tmp.get('c4', ''))
print(dict_tmp.get('c5', ''))

