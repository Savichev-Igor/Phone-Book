# -*- coding: utf-8 -*-


def edit(temp):
    good_number = ""
    for j in range(len(temp)):
        if j == 0:
            if temp[0] == '8':
                good_number += '+7-'
            if temp[0] == '7':
                good_number += '+7-'
        if j == 4 or j == 7 or j == 9:
            good_number += '-'
        if j:
            good_number += temp[j]
    return good_number
