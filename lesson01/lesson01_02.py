'''
Написать функцию host_range_ping() для перебора ip-адресов из заданного диапазона. Меняться должен только последний
октет каждого адреса. По результатам проверки должно выводиться соответствующее сообщение.
'''


from ipaddress import ip_address
from lesson01_01 import host_ping


def host_range_ping():
    while True:
        start_ip = input('Введите начальный ip-адрес: ')
        try:
            last_digit = int(start_ip.split('.')[3])
            if last_digit > 255:
                print('октет ip-адреса не может быть больше 255')
            else:
                break  # введены корректные данные, идем дальше
        except Exception as e:
            print(e)
    while True:
        quantity_ip = input('Введите количество проверяемых адресов: ')
        if not quantity_ip.isnumeric():
            print('некорректное значение')
        else:
            if last_digit+int(quantity_ip) > 254:
                print(f'при заданном начальном адресе, количество проверяемых адресов не должно превышать {254-last_digit}')
            else:
                break  # введены корректные данные, идем дальше

    hosts_list = [str(ip_address(start_ip)+i) for i in range(int(quantity_ip))]

    return host_ping(hosts_list)


if __name__ == '__main__':
    host_range_ping()


# Результаты:
# Узел 192.168.250.1 [192.168.250.1] доступен
# Узел 192.168.250.2 недоступен
# Узел 192.168.250.3 недоступен
# Узел 192.168.250.4 недоступен
# Узел 192.168.250.5 [192.168.250.5] доступен
