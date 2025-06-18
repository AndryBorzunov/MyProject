from typing import List, Dict
from datetime import datetime

def filter_by_state(list_of_dicts: List, state='EXECUTED') -> List:
    """ Выборка словарей из списка словарей с заданным статусом"""
    filter_list = []
    for dict_item in list_of_dicts:
        if dict_item['state'] == state:
            filter_list.append(dict_item)

    return filter_list
