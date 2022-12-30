"""
 Bir listeyi düzleştiren (flatten) fonksiyon yazın.
 Elemanları birden çok katmanlı listelerden ([[3],2] gibi) oluşabileceği gibi, non-scalar verilerden de oluşabilir.
 Örnek olarak:

input: [[1,'a',['cat'],2],[[[3]],'dog'],4,5]
output: [1,'a','cat',2,3,'dog',4,5]
"""




list_1 = [[1,'a',['cat'],2],[[[3]],'dog'],4,5]
flatten_list =[]

def flatten(list_name):
    for small_list in list_name:
        if type(small_list) == list:
            flatten(small_list)
        else:
            flatten_list.append(small_list)
    return flatten_list

print(flatten(list_1))

#****************************************************************************************************************************************************

"""
Verilen listenin içindeki elemanları tersine döndüren bir fonksiyon yazın.
Eğer listenin içindeki elemanlar da liste içeriyorsa onların elemanlarını da tersine döndürün.
Örnek olarak:
input: [[1, 2], [3, 4], [5, 6, 7]]
output: [[[7, 6, 5], [4, 3], [2, 1]]
"""



list_2 = [[1, 2], [3, 4], [5, 6, 7]]

def reverse_list(l):
    l.reverse()
    for sublist in l:
        if type(sublist) == list:
            reverse_list(sublist)

reverse_list(list_2)
print(list_2)

