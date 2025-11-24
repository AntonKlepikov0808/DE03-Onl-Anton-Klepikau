# #задание 1
# file1 = open ('задание 5\Тут просто информация из файла 1.txt',)
# content = file1.read ()
# file1.close ()

# file2 = open ('задание 5\Тут информация из файла 2.txt', 'w')
# file2.write (content)
# file2.close ()


#Здание2

file3 = open(r"zadanie5\tytfile3.txt", "r+")
info = file3.read()
file3.close()

file4 = open(r"zadanie5\tytfile4.txt", "r+")
file4.write(info.upper())
file4.close()