def in_print_1():
 
    paul = False

    while paul == False:

        q = input("Введите число: ")
        if int(q) == 1 :
            print("1 процент")
            paul == True
        off ='ов' 
        if int(q) > 1 :
            print(f"{q} процент" + off)
            paul == True


        if q == 101:
            print(type(q))
            enddd = True



in_print_1()

paul2 = True

# while paul2 == True :

#     q = input("1 процент: ")
#     if int(q) == 1 :

#                 print("2 процента")
#                 print(type(q))
#                 print(type(2))
#                 print(type('2 процента'))

#     if q == 2:
#         print(type(q))
#         endd = True


