from base64 import encode
from msilib.schema import Class
import socket
import time
from client_conf import ip_serv, port_serv, number_cab, time_update

""" Класс пациента для передачи в pyqt """
class Pac_viewer:
    """ Инициализация """
    def __init__(self, ip, port, cab_num):
        self.ip = ip
        self.port = port
        self.cab_num = cab_num
        self.data_recived = 'нет'
        self.data_status = 'нет'

    """ Отправка и получение данных
        Отправка в формате 'xx', хх = номер каб 
        Получение в формате:
        ('ФИО', '№ кабинета', 'время работы', 'Специализация'); статус
        """
    def send_data(self):
        
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # создаем сокет
        sock.connect((self.ip, self.port))  # подключемся к серверному сокету
        data_send = f'{self.cab_num}@{self.data_recived}' # создаем переменную для отправки
        sock.send(bytes(data_send, encoding = 'UTF-8'))  # отправляем переменную в двоичном формате
        data_rec = sock.recv(1024)  # читаем ответ от серверного сокета
        data_recy = data_rec.decode('UTF-8') # перекодиуем ответ в UTF-8'
        if data_rec == self.data_recived:
            print(data_recy)
        else:
            print(data_recy)
            print(self.data_recived)
            self.data_recived = data_rec
        sock.close() 

cab = Pac_viewer(ip_serv, port_serv, number_cab)

while True:
    cab.send_data()
    time.sleep(time_update)

