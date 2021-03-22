# # number=int(input('Enter a number:'))
# # if number<10:
# #     print('prea mic')
# # elif number>10:
# #     print('prea mare')
# # else:
# #     print('just right')
# #
# # #type
# my_String= 6
# print(type(my_String))
# my_type=type(my_String)
# print(type(my_type))
# print(type(my_String)== str)
# #
# var=input('Enter something:')
# if 47<ord(var[0]):
#     print(type(var))
#     if ord(var[0])<=57:
#         result=int(var)
# print (result)
# #
# # #bool
# # print(bool(0+0j))
# # print (bool('string'))
# # print(bool('print'))
# #
# # if bool(1<2):
# #     print('This is working')
# #
# # var=input('Enter something:')
# # if var:
# #     print('Success')
#
# #foor loops
# for value in range (1,10,2):
#     print(value)
#     if value==2:# try 2
#         break
#     print('this will never be printed')
# else:
#     print('This is else',value)
# print('This is outside for',value)
#
# # eg
# for letter in 'my_text':
#     print('Letter is:',letter)
#
# # Iterable object
# str_iter='my_text'.__iter__()
# #int_iter=(123).__inter__()#not iterable
#
# print(type(str_iter))
# print(next(str_iter))
# print(next(str_iter))
# print(next(str_iter))
# print(next(str_iter))
# print(next(str_iter))
# print(next(str_iter))
# print(next(str_iter))
# #print(next(str_iter))#stop iteration
#
def
n = int(input("n = "))
for nr in range(1, n + 1):
    if nr < 3:
        print(f"{nr} este prim")
        continue
    for number in range(2, nr):
        if nr % number == 0:21
            print("nr nu este prim")
            break
#     else:
#         print(f"{nr} este prim")
#
#
# # #str+129
# # a = str(input())
# # for i in a:
# #     i_nr = ord(i) + 129
# #     print(chr(i_nr), end='')

print()
a= True
b= False
print('Result',a and b)

# And
if a:
    print(b)
else:
    print(a)

# Or
a = 0
b = 1
print("resoult:", a or b)
if a:
    print(a)
else:
    print(b)


