# -*- coding: utf-8 -*-
import sys
import os
import moduls.call_book_vk
import moduls.call_book_mc
import moduls.merge
import moduls.google_import
import moduls.vcf


def show(some_dict):
    for key in some_dict:
        print(key)
        print(some_dict[key].decode('cp1251'))


def vk_func(email_vk, password_vk):
    vk_dict = moduls.call_book_vk.run(email_vk,
                                      password_vk)
    return vk_dict


def mc_func(username_mc, password_mc):
    mc_dict = moduls.call_book_mc.run(username_mc,
                                      password_mc)
    return mc_dict


def merge(vk_dict, mc_dict):
    final_dict = moduls.merge.func(vk_dict, mc_dict)
    return final_dict


def google_import(final_dict, email_g, pass_g):
    print('\n' + 'All is okay, now we will import contacts in Google' + '\n')
    try:
        moduls.google_import.run_import(email_g, pass_g, final_dict)
    except:
        print("Error: Check your input for Google")
        sys.exit(0)
    print('\n' + 'You can check your Google contacts' + '\n')


def vcf(some_dict):
    try:
        os.makedirs('Contacts')
        print('\n' + 'dir "Contacts" created' + '\n')
    except:
        print('Probably this dicectory exists, please remove this')
        sys.exit(0)
    moduls.vcf.create_contact_vcf(some_dict)
    print('\n' + 'You can check dir' + '\n')

if len(sys.argv) == 1:
    print('\n' + 'This program uses for import your contacts from VK ' +
          'and My Circle in Google Contacts or on HDD (.vcf)' + '\n')
    print('If you want load in Google Contacts write 3 options (VK, MC, G)')
    print('Example: python2 main.py IvanGrozniy@mail.ru Absolute ' +
          'SpanbeBob@bottom_city.net Gary MaxPayne@gmail.com Family' + '\n')
    print('For import in .vcf format write this options without Google' + '\n')
    print('Example: python2 main.py IvanGrozniy@mail.ru Absolute ' +
          'SpanbeBob@bottom_city.net Gary' + '\n')
    print('And you can make import only from one service' + '\n')
    print('Example: python2 main.py VK email password .vcf' + '\n')
    print('Example: python2 main.py MC username password MaxPayne@gmail.com Family' + '\n')
else:
    if len(sys.argv) == 7:
        final_dict = merge(vk_func(sys.argv[1], sys.argv[2]),
                           mc_func(sys.argv[3], sys.argv[4]))
        google_import(final_dict, sys.argv[5], sys.argv[6])
    else:
        if len(sys.argv) == 5 and sys.argv[1] != 'VK' and sys.argv[1] != 'MC':
            final_dict = merge(vk_func(sys.argv[1], sys.argv[2]),
                               mc_func(sys.argv[3], sys.argv[4]))
            vcf(final_dict)
        else:
            if sys.argv[1] == 'VK':
                some_dict = vk_func(sys.argv[2], sys.argv[3])
            else:
                some_dict = mc_func(sys.argv[2], sys.argv[3])
            if sys.argv[4] == '.vcf':
                vcf(some_dict)
            else:
                google_import(some_dict, sys.argv[4], sys.argv[5])


# Допилить последнюю развилку, проверить 7-ми аргументную
# Добавить 4 режима для одного из сервисов в режиме гугл\vcf
# Проверить, скопирнуть справку в документацию, если остануться силы - сделать тесты.
