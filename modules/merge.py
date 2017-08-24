# -*- coding: utf-8 -*-


def func(dict_one, dict_two):
    final_dict = {}
    if len(dict_one) > len(dict_two):
        final_dict = dict_one
        for key in dict_two:
            if key in dict_one:
                pass
            else:
                final_dict.update({key: dict_two[key]})
    else:
        final_dict = dict_two
        for key in dict_one:
            if key in dict_two:
                pass
            else:
                final_dict.update({key: dict_one[key]})
    return final_dict
