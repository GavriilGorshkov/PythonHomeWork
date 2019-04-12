a = input('Введите дату рождения:')
b = input('Введите текущую дату:')

def vozrast(a,b):
    print('Ваш возраст ' + str((int(b[6::]) - int(a[6::])) - bool((int(b[3:5:]) < int(a[3:5:])) or (int (b[0:2:]) < int(a[0:2:])))) + ' лет')

vozrast(a,b)




# a='02.10.2001'
# b='01.10.2002'
