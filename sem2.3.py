#В институте биоинформатики по офису передвигается робот. 
# Недавно студенты из группы программистов написали для него программу, 
# по которой робот, когда заходит в комнату, считает количество программистов в ней 
# и произносит его вслух: "n программистов".
# Для того, чтобы это звучало правильно, для каждого nn нужно использовать верное окончание слова.
# Напишите программу, считывающую с пользовательского ввода целое число nn (неотрицательное), 
# выводящее это число в консоль вместе с правильным образом изменённым словом "программист",
#  для того, чтобы робот мог нормально общаться с людьми, например: 1 программист, 2 программиста, 5 программистов.
# В комнате может быть очень много программистов. Проверьте, что ваша программа правильно обработает все случаи,
#  как минимум до 1000 человек.

prog_num = int(input("Сколько программистов сейчас в комнате?   "))

def Appeal(x):
    if x<0:
        print("Fatal error! Code 404! There is no programmers")
    else:
        y = x%10
        if y == 0 or 4<y<10:
            print(f"{x} программистов в комнате")
        elif y==1:
            print(f"{x} программист в комнате")
        elif 1<y<5:
            print(f"{x} программиста в комнате")


Appeal(prog_num)