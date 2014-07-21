# -*- coding: utf-8 -*-
import sys
import re
from grab import Grab
import click
import pytils
import myparser


class MyCircleParser:

    def __init__(self, username, password):
        self.session = Grab()
        self.username = username
        self.password = password

    def auth(self):
        self.session.go('https://mail.yandex.ru/')
        self.session.set_input('login', self.username)
        self.session.set_input('passwd', self.password)
        self.session.submit()
        self.check = re.findall(r"auth__social", self.session.response.body)
        if len(self.check) != 0:
            print('\n' + "Check your input for My Circle")
            sys.exit(0)
        else:
            print('\n' + "Your auth is success in My Circle" + '\n')

    def take_friends_contacts(self):
        self.session.go('http://moikrug.yandex.ru/')
        self.session.go('http://moikrug.ru/circles/first/users/')
        self.urls = re.findall(r'"name"><a href="http://(.+?).moikrug.ru/"',
                               self.session.response.body)
        self.cont_dict = {}
        print('Taking mobile phone from My Circle' + '\n')
        with click.progressbar(range(len(self.urls))) as bar:
            for x in bar:
                self.session.go('http://'+str(self.urls[x]) +
                                '.moikrug.ru/contact/')
                full_name = re.findall(r'<meta.+?content="(.+)"><meta.item',
                                       self.session.response.body.decode('cp1251'))
                number = re.findall(r'class="tel">(.+?)</span',
                                    self.session.response.body)
                if len(number) == 1:
                    number[0] = number[0].replace(' ', '')
                    number[0] = number[0].replace('+', '')
                    final_number = myparser.edit(number[0])
                    self.cont_dict.update({final_number:
                                          pytils.translit.translify(full_name[0])})
        print('\n')
        return self.cont_dict


def run(username, password):
    session = MyCircleParser(username, password)
    session.auth()
    return session.take_friends_contacts()
