# -*- coding: utf-8 -*-
import click
import gdata.contacts.client


class ImportGoogle:

    def __init__(self, email, password, final_dict):
        self.final_dict = final_dict
        self.gd_client = gdata.contacts.client.ContactsClient(source='Export' +
                                                              'contacts' +
                                                              'to Google')
        self.email = email
        self.password = password

    def auth(self):
        self.gd_client.ClientLogin(self.email, self.password,
                                   self.gd_client.source)

    def create_contact(self, name, phone):
        new_contact = gdata.contacts.data.ContactEntry()
        new_contact.name = gdata.data.Name(
            full_name=gdata.data.FullName(text=name))
        new_contact.phone_number.append(gdata.data.PhoneNumber(text=phone,
                                                               rel=gdata.data.WORK_REL,
                                                               primay='true'))
        self.gd_client.CreateContact(new_contact)


def run_import(email, password, final_dict):
    session = ImportGoogle(email, password, final_dict)
    session.auth()
    print('\n' + "Your auth in Google is success" + '\n')
    print('Importing...' + '\n')
    with click.progressbar(final_dict) as bar:
        for key in bar:
            try:
                session.create_contact(final_dict[key], key)
            except:
                print('\n' + 'Something wrong with' + '\n')
                print(key + '\n')
