"""
Написать функцию host_ping(), в которой с помощью утилиты ping будет проверяться доступность сетевых узлов.
Аргументом функции является список, в котором каждый сетевой узел должен быть представлен именем хоста или ip-адресом.
В функции необходимо перебирать ip-адреса и проверять их доступность с выводом соответствующего
сообщения («Узел доступен», «Узел недоступен»). При этом ip-адрес сетевого узла должен создаваться
с помощью функции ip_address().
"""

from ipaddress import ip_address
from socket import gethostbyname

from subprocess import Popen, PIPE


hosts_list = (
    '192.168.250.2',  # Узел 192.168.250.2 недоступен
    'ya.ru',  # Узел ya.ru [87.250.250.242] доступен
    'gb.ru',  # Узел gb.ru [178.248.232.209] доступен
    'isdubfiubsdcisw.ru',  #Узел isdubfiubsdcisw.ru недоступен
)

TIMEOUT = 300
REQUESTS = 1


def host_ping(hosts_list = hosts_list, timeout=TIMEOUT, requests=REQUESTS):
    hosts_results = {  # словарь для третьего задания
        'reachable': '',  # доступные хосты
        'unreachable': '',  # недоступные хосты
    }
    for host in hosts_list:
        try:
            '''
            вынужден использовать gethostbyname() потому что выдается исключение
            "does not appear to be an IPv4 or IPv6 address"
            '''
            host_ip = gethostbyname(host)
            ipv4 = ip_address(host_ip)
            proc = Popen(f'ping {ipv4} -w {timeout} -n {requests}', shell=False, stdout=PIPE)
            proc.wait()
            if proc.returncode == 0:
                print(f'Узел {host} [{ipv4}] доступен')
                hosts_results['reachable'] += f'{str(ipv4)}\n'
            else:
                print(f'Узел {host} недоступен')
                hosts_results['unreachable'] += f'{str(ipv4)}\n'
        except Exception as e:  # если ip-адрес не получилось определить
            print(f'Узел {host} недоступен')
            hosts_results['unreachable'] += f'{str(ipv4)}\n'
            # print(e)
    return hosts_results

if __name__ == '__main__':
    host_ping()
