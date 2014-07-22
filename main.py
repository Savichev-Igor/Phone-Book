# -*- coding: utf-8 -*-
import sys
import os
import getpass
import moduls.call_book_vk
import moduls.call_book_mc
import moduls.merge
import moduls.google_import
import moduls.vcf


def show(some_dict):
    for key in some_dict:
        print(key)
        print(some_dict[key].decode('cp1251'))


def vk_func():
    while True:
        try:
            email_vk = raw_input('\n' + 'Your e-mail for VK: ')
            password_vk = getpass.getpass()
            session = moduls.call_book_vk.Vk_Contacts(email_vk, password_vk)
            session.auth()
            vk_dict = session.take_friends_contacts()
            print('\n' + "Your auth is success in VK.com" + '\n')
            break
        except:
            print('\n' + "Check your input for VK.com" + '\n')
    return vk_dict


def mc_func():
    while True:
        username_mc = raw_input('\n' + 'Your username for MC: ')
        password_mc = getpass.getpass()
        session = moduls.call_book_mc.MyCircleParser(username_mc, password_mc)
        session.auth()
        if session.check_auth():
            print('\n' + "Your auth is success in MC" + '\n')
            mc_dict = session.take_friends_contacts()
            break
        else:
            print('\n' + 'Check your input for MC' + '\n')
    return mc_dict


def merge(vk_dict, mc_dict):
    final_dict = moduls.merge.func(vk_dict, mc_dict)
    return final_dict


def google_import(final_dict):
    while True:
        try:
            email_g = raw_input("\n" + 'Your e-mail for Google: ')
            password_g = getpass.getpass()
            moduls.google_import.run_import(email_g, password_g, final_dict)
            break
        except:
            print('\n' + "Check your input for Google" + '\n')
    print('\n' + 'You can check your Google contacts' + '\n')


def vcf(some_dict):
    while True:
        try:
            raw_input('\n' + 'Click "Enter" for continue' + '\n')
            os.makedirs('Contacts')
            print('\n' + 'Dir "Contacts" created' + '\n')
            moduls.vcf.create_contact_vcf(some_dict)
            break
        except:
            print('\n' + 'We try created directory "Contacts"' + '\n')
            print('\n' + 'Probably this dicectory exists, please remove this' + '\n')
    print('\n' + 'You can check dir' + '\n')


if len(sys.argv) == 1:
    print('\n' + 'This program uses for import your contacts from VK ' +
          'and My Circle in Google Contacts or on HDD (.vcf)' + '\n')
    print('If you want load in Google Contacts write one option' + '\n')
    print('Example: python2 main.py G' + '\n')
    print('For import contacts in ".vcf" format write also one option' + '\n')
    print('Example: python2 main.py .vcf')
    print('Also you can import contacts only from one service' + '\n')
    print('Example: python2 main.py VK G' + '\n')
    print('Example: python2 main.py MC .vcf' + '\n')
else:
    if sys.argv[1] == 'G':
        vk_dict = vk_func()
        mc_dict = mc_func()
        final_dict = merge(vk_dict, mc_dict)
        print('\n' + 'All is okay, now we will import contacts in Google')
        google_import(final_dict)
        sys.exit(0)
    else:
        if sys.argv[1] == '.vcf':
            vk_dict = vk_func()
            mc_dict = mc_func()
            final_dict = merge(vk_dict, mc_dict)
            vcf(final_dict)
            sys.exit(1)
        if sys.argv[1] == 'VK':
            vk_dict = vk_func()
            if sys.argv[2] == 'G':
                print('\n' + 'All is okay, now we will import contacts in Google')
                google_import(vk_dict)
                sys.exit(3)
            if sys.argv[2] == '.vcf':
                vcf(vk_dict)
                sys.exit(4)
        if sys.argv[1] == 'MC':
            mc_dict = mc_func()
            if sys.argv[2] == 'G':
                print('\n' + 'All is okay, now we will import contacts in Google')
                google_import(mc_dict)
                sys.exit(5)
            if sys.argv[2] == '.vcf':
                vcf(mc_dict)
                sys.exit(6)
