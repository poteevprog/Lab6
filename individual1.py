#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == '__main__':
    a = tuple(map(int, input("Введите кортеж: ").split()))

    k = a.count(a[0])
    index = a[0]
    a1 = list(a)  # переделываем кортеж в список

    i = 0
    while a1[i] == a[0]:
        a1.remove(a[0])

    if k == len(a):
        print("Кортеж состоит из одинаковых элементов.")
    else:
        print("Количество первых элементов равных между собой: ", k)
        print("Элементы после первых равных элементов: ", a1)
