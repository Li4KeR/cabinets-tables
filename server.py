from base64 import encode
import socket
from logic import *



sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # создаем сокет
sock.bind(('', 55000))  # связываем сокет с портом, где он будет ожидать сообщения
sock.listen(30)  # указываем сколько может сокет принимать соединений


""" Создаем объекты для каждого кабинета и добавляем все в 1 переменную """
cab_1 = Cabinets('01')
cab_2 = Cabinets('02')
cab_3 = Cabinets('03')
cab_4 = Cabinets('04')
cab_5 = Cabinets('05')
cab_6 = Cabinets('06')
cab_8 = Cabinets('08')
cab_11 = Cabinets('11')
cab_12 = Cabinets('12')
cab_13 = Cabinets('13')
cab_14 = Cabinets('14')
cab_15 = Cabinets('15')
cab_16 = Cabinets('16')
cab_17 = Cabinets('17')
cab_19 = Cabinets('19')
cab_20 = Cabinets('20')
cab_21 = Cabinets('21')
cab_22 = Cabinets('22')
cab_23 = Cabinets('23')
cab_25 = Cabinets('25')

cabs = (cab_1, cab_2, cab_3,  cab_4, cab_5, cab_6, cab_8, 
        cab_11, cab_12, cab_13, cab_14, cab_15, cab_16, 
        cab_17, cab_19, cab_20, cab_21, cab_22, cab_23, cab_25)

""" Зацикливаем получение соеденений """
while True:
    conn, addr = sock.accept()  # начинаем принимать соединения
    data = conn.recv(1024)  # принимаем данные от клиента, по 1024 байт
    data = data.decode('UTF-8') # переводим байт-код в UTF-8
    kab_num = data.split('@')[0]
    kab_data = data.split('@')[1]
    for cab in cabs:
        if cab.cab == kab_num: 
            cab.get_schedule() # запускаем метод из logic.py
            cab.check_status() # запускаем метод из logic.py
            data = f'{cab.data};{cab.status}'
            if data != kab_data:
                conn.send(bytes(data, encoding = 'UTF-8'))
    conn.close()