from operator import itemgetter
from utils import hh_data, sj_data, combine


def main():
    while True:
        user_input = input('Выберите действие:\n1. Сформировать список вакансий с HH\n2. Сформировать список вакансий с '
            'SJ\n3. Вывести все вакансии\n4. Вывести 5 вакансий с наибольшей зарплатой\n5. Выход\n')
        if user_input == 1:
            hh_data()
        elif user_input == 2:
            sj_data()
        elif user_input == 3:
            data = combine()
            # for dat in date:







