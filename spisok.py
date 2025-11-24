# #список
# list = [1,2,3,4,5] 
# print ('Spisok' ,list)

# # Добавить элемент в конец список
# list.append (15)
# print ("append", list)

# #добавление множество элементв в конец списка
# list.extend ([16,17,18]) 
# print ("extend", list)

# #Вставка значения с учетом номера вставки элемента
# list.insert (3, 19)
# print ("insert", list)

# #удаление первого найденного элементов
# list.remove (15)
# print ("remove", list)

# #Удаление элекмента по индексу 
# list.pop (1)
# print ("pop", list)
# #возвращается список с удаленными значениями 
# removed_last = list.pop ()
# print ("pop", removed_last, list)
# #удаление по индексу
# removed_index = list.pop (5)
# print ("pop", removed_index, list)





# #удаление всех элементов
# list.clear()
# print ("clear", list)


# #подсчет и копирование 
# list_copy = list.copy()
# print ("copy", list)

# # вхождение элементов в список 
# list_copy.count(2)



# # #поиск элементов
# first2 = list.index(2)
# print ("index(2)", first2)



# #сортировка
# list.sort(reverse=True)
# print ("sort()", list)

# # Новый сортированный спсиок
# new_sorted=sorted(list)
# print ("sorted", new_sorted)

# print ("len(list)", len(list))
# print ("sum(list)", sum(list))
# print ("max(list)", max(list))
# print ("min(list)", min(list))



#Создание кортежа 
t = (1,2,3,4,5,6)
print ("Исходные кортеж",t)

# методы кортежа 
index_3 = t.index(3)
print("index (3)",index_3)

# Операции над кортежами

# конкатенация
t = (1,2)
t2= (3,4)
new_tuple = t+t2
print ("t+t2", new_tuple)


#Повторение кортежа 
repeat_tuple = t*3
print ("t",t[0])

#Индексация и срезы
print ("t",t[0])
print ("t",t[1:4])