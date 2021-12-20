"""
Написать функцию host_range_ping_tab(), возможности которой основаны на функции из примера 2. Но в данном случае
результат должен быть итоговым по всем ip-адресам, представленным в табличном формате (использовать модуль tabulate).
"""

from tabulate import tabulate
from lesson01_02 import host_range_ping


def host_range_ping_tab():
    user_dict = host_range_ping()
    print(tabulate([user_dict], headers='keys', tablefmt='pipe'))


if __name__ == '__main__':
    host_range_ping_tab()


# результат:
# | reachable     | unreachable   |
# |:--------------|:--------------|
# | 192.168.250.1 | 192.168.250.2 |
# | 192.168.250.5 | 192.168.250.3 |
# |               | 192.168.250.4 |
# |               | 192.168.250.6 |
