from abc import ABC, abstractmethod
import requests


class Engine(ABC):
    @abstractmethod
    def get_request(self, page):
        pass


class HH(Engine):
    def __init__(self):
        self.url = 'https://api.hh.ru/vacancies'
        self.name = 'python'


    def get_request(self, page):
        params = {'text': self.name, 'area': '113', 'per_page': '10', 'page': page}
        return requests.get(self.url, params=params)


class Superjob(Engine):
    def __init__(self):
        self.url = 'https://russia.superjob.ru/vacancy/search/?keywords=python'
        self.headers = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:105.0) Gecko/20100101 Firefox/105.0'
        }
        self.name = 'python'


    def get_request(self, page):
        params = {'text': self.name, 'page': page}
        return requests.get(self.url, params=params)


class Vacancy:
    def __init__(self, name, url, salary, description):
        # self.data = data
        # self.hh = hh
        self.salary = salary
        self.name = name
        self.description = description
        self.url = url


    def __repr__(self):
        return (f'Название вакансии: {self.name}\nСсылка на вакансию: {self.url}\nЗаработная плат'
                f'а: {self.salary}\nОписание вакансии: {self.description}')
