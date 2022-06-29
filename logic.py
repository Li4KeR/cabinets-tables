import parse
import datetime
import time

class Cabinets:
    """ Инициализация кабинета """
    def __init__(self, cab):
        self.cab = cab
        self.status = ''
        self.data = ''
        print(self.cab)

    """ Выгрузка ФИО врача, время приема, специализацию!!!, кабинет """
    def get_schedule(self):
        cur = parse.sql_schedule()
        data = []
        cache_kab = []
        """ Перебираем скуль запрос и отдаем нужное расписание """
        for row in cur:
            fio = row[0]
            #dcode = row[1]
            hfinish = row[3]
            mfinish = row[4]
            hstart = row[5]
            mstart = row[6]
            kab = row[7]
            spek = row[8]
            #cach = f'{fio};{dcode};{hstart};{mstart};{hfinish};{mfinis};{kab}'
            """<! Перевод строки во время !>"""
            if hstart == 24:
                hstart = 23
                mstart = 59
            if hfinish == 24:
                hfinish = 23
                mfinish = 59

            work_time_start = f'{hstart}:{mstart}'
            work_time_end = f'{hfinish}:{mfinish}'
            time_now = time.strftime("%H.%M", time.localtime())

            work_time_start1 = datetime.datetime.strptime(work_time_end, '%H:%M')
            work_time_end1 = datetime.datetime.strptime(work_time_start, '%H:%M')

            work_time_start2 = work_time_start1.strftime("%H.%M")
            work_time_end2 = work_time_end1.strftime("%H.%M")
            """<! end_translate_time !>"""

            """ находим нужное расписание """
            if kab is not None:
                if kab not in cache_kab:
                    if kab == self.cab:
                        if work_time_start2 <= time_now <= work_time_end2:
                            cache_kab.append(kab)
                            full_work = f'{work_time_start2}:{work_time_end2}'
                            answer = (fio, kab, full_work, spek)
                            data.append(answer)
        """ Конец скуль перебор """

        if data == []:
            data = 'Нет приема'
        else:
            data = data[0]
        if self.data != data:
            self.data = data

    """ Проверка статуса(свободно\занято) кабинета """
    def check_status(self):
        cur = parse.sql_all_treat_today()
        data_start = []
        data_finish = []
        data_start_cache = 0
        data_end_cache = 0

        for row in cur.itermap():
            cab_name = row['SHORTNAME']
            start_treat = row['STARTTREAT']
            finish_treat = row['FINISHTREAT']
            if cab_name == self.cab:
                data_start.append(start_treat)
                data_finish.append(finish_treat)

        for x in data_start:
            if x is None:
                data_start_cache += 1

        for x in data_finish:
            if x is None:
                data_end_cache += 1

        if data_start_cache == data_end_cache:
            status = 'Свободно'
        else:
            status = "Занято"

        if self.status != status:
            self.status = status



#---------------------------------------------------------------------------

#cab_1 = Cabinets('01')
#cab_2 = Cabinets('02')
#cab_3 = Cabinets('03')
#cab_12 = Cabinets('14')
#
#if __name__ == '__main__':
#    while True:
#        print(cab_12.status)
#        cab_12.check_status()
#        print(cab_12.status)
#        time.sleep(2)
#status = f'{cab_12.data} {cab_12.status}'
#print(status)
#cabs = (cab_1, cab_2, cab_3)
#perem = '02'  # so what?!

#for cabin in cabs:
#    if cabin.cab == perem:
#        print("YES")

#for item in all_cabinets:
#    print(item)
