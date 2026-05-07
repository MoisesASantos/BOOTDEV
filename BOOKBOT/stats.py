def count_words(file_contents):
    words = file_contents.split()
    count = 0
    for word in words:
        count += 1
    return count

def count_total_each_appears(file_contents):
    new_string = file_contents.lower()
    dict1 = {} 
    count = 0
    for char in new_string:
        if char in dict1:
            count = dict1[char]
            count += 1
            dict1[char] = count;
        else:
            dict1[char] = 1
    return dict1

def bubble_sort(dict1):
    lista = list()
    for _, v in enumerate(dict1):
        dicio = dict()
        
        dicio["char"] = v
        dicio["num"] = dict1[v]

        lista.append(dicio)
    

    return lista

def sort_on(items):
    return items["num"]

