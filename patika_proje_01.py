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



