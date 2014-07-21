# -*- coding: utf-8 -*-
import re
import sys
import vkontakte
from vkappauth import VKAppAuth
import click
import myparser


class Vk_Contacts:

    def __init__(self, email, password):
        self.app_id = 4392739
        self.scope = []
        self.email = email
        self.password = password

    def auth(self):
        try:
            self.access_data = VKAppAuth().auth(self.email,
                                                self.password,
                                                self.app_id, self.scope)
            print('\n' + "Your auth is success in VK.com" + '\n')
        except:
            print('\n' + "Check your input for VK.com")
            sys.exit(0)
        self.vk = vkontakte.API(token=self.access_data["access_token"])

    def take_friends_contacts(self):
        self.profiles = self.vk.friends.get(uids=self.access_data['user_id'],
                                            fields='contacts')
        self.friends = []
        for profile in self.profiles:
            if profile.get('mobile_phone'):
                self.friends.append(profile)
        self.vk_numbers = {}
        print('Taking mobile phones from VK' + '\n')
        with click.progressbar(self.friends) as bar:
            for friend in bar:
                temp = re.findall('[0-9]', friend['mobile_phone'])
                if len(temp) == 11:
                    good_number = myparser.edit(temp)
                    full_name = friend['last_name']+' '+friend['first_name']
                    self.vk_numbers[good_number] = full_name
        print('\n')
        return self.vk_numbers


def run(email, password):
    session = Vk_Contacts(email, password)
    session.auth()
    return session.take_friends_contacts()
