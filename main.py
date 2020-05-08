from collections import deque
from array import *
from algorithms import Algorithms as alg
import time
# Быстрее вставка и удаление данных
list = [2, 3, 1, 9, 4, 5]
# Быстрее чтение
massive = array('i', [1, 2, 3, 4, 5, 6, 7, 8, 9])
# Хэш таблица (словарь)
graph_name = {'You': ['Roma', 'Danyr', 'Liza'], 'Roma': ['Nikita', 'Dasha'], 'Danyr': ['Ylo', 'Kost', 'You'],
 'Liza': ['Polya'], 'Nikita': [], 'Dasha': [], 'Ylo': [], 'Kost': [], 'Polya': ['You']}
queue = deque(graph_name.keys())
graph = {'start': {'a': 2, 'b': 5}, 'a': {'b': 2, 'd': 5}, 'b': {'c': 4, 'd': 2}, 'c': {'d': 6, 'fin': 3},
         'd': {'fin': 1}, 'fin': {}}

graph_two = {'start': {'a': 10}, 'a': {'b': 20}, 'b': {'c': 1, 'fin': 30}, 'c': {'a': 1}, 'fin': {}}

graph_three = {'start': {'a': 6, 'b': 2}, 'a': {'fin': 1}, 'b': {'a': 3, 'fin': 5}, 'fin': {}}

graph_four = {'start': {'a': 9, 'b': 14, 'c': 7}, 'a': {'b': 2, 'fin': 11}, 'b': {'d': 2}, 'c': {'a': 10, 'fin': 15},
              'd': {'fin': 1}, 'fin': {}}
graph_five = {'start': {'a': 5, 'b': 20, 'c': 20}, 'fin': {}, 'a': {'b': 10, 'd': 6}, 'b': {'e': 7, 'fin': 9},
              'c': {'b': 2, 'fin': 20},
              'd': {'c': 1}, 'e': {'fin': 1}}

graph_six = dict(start={'a': 10, 'b': 1, 'c': 10, 'd': 10}, fin={}, a={'c': 10, 'f': 1}, b={'a': 1, 'g': 10},
                 c={'d': 1, 'e': 10}, d={'e': 1}, e={'fin': 1}, f={'c': 1, 'fin': 10}, g={'a': 10, 'f': 10})

print(alg.dijkSearch(graph_five))
# print(alg.dijkSearch(graph_two, 'a', 'fin'))
# print(alg.dijkSearch(graph_three))
# print(alg.rGraphSearch(queue, graph_name, 't'))
# print(alg.rGraphSearch(queue, graph_name, 't'))
# print(alg.rGraphSearch(queue, graph_name, 't'))
# print(alg.rGraphSearch(queue, graph_name, 't'))
# print(time.clock()-start_time)
# print(alg.binarySearch(massive, 3))
# print(alg.fSort(list, False))
# print(alg.sSort(list, True))
stationNeed = {'mt', 'wa', 'or', 'id', 'nv', 'ut', 'ca', 'az'}

stations = {'kone': {'id', 'nv', 'ut'}, 'ktwo': {'wa', 'id', 'mt'}, 'kthree': {'or', 'nv', 'ca'}, 'kfour': {'nv', 'ut'},
            'kfive': {'ca', 'az'}}

# print(alg.setOptimization(stationNeed, stations))

pack = {'guitar': [1, 1500], 'magnitofon': [4, 3000], 'laptop': [3, 2000], 'iphone': [1, 2000], 'MP3': [1, 1000]}
# start_time = time.clock()
# print(alg.backpackAlg(pack, 4))
# print(time.clock()-start_time)

Test = ['Hello world', 'wwooee', 'Codewars', 'Maam', 'queq', 'tttlspss', 'eyekeks', 'Hello world', 'printp']

def function(s):
    list = sorted([s[::-1].index(i) for i in set(s) if s.count(i) % 2], reverse=True)
    return [s[-i - 1] for i in list]

start_time = time.clock()
print(time.clock()-start_time)

