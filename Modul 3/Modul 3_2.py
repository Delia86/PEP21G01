# def my_func(arg1,arg2,arg3):
#     print (arg1, arg2,arg3, )
#     return arg1, arg2, arg3
#
# my_func('val 1', 'val 2' 'val 3 ')
# my_return=my_func('value 1','value 2','value 3')

def prime(max_prime):
    my_primes=[]

    print('Primes are:', end='')

    for number in range(1, max_prime + 1):
        if number < 3:
            my_primes.append(number)
            continue
        for divider in range(2, number):
            if number % divider == 0:
                break
        else:
            my_primes.append(number)
    return my_primes

my_primes=prime(21)
print(my_primes)



# #lists
# my_list=[1,2,3]
# list_iter=my_list.__iter__()
# for number in my_list:
#     print(number)
#
# number=1
# print(id(number))
# number += 1
# print(id(number))
#
# print(id(my_list))
# my_list.append(4)
# print (my_list)
# print(id(my_list))
# print(my_list==[1,2,3,4])
# print(my_list==my_list.append(5))
# print(id(my_list)==id(my_list.append(5))
#
# # new_object1= 'my_str_{}'.format('1')
# # print(new_object1)
# # new_object2=[1,2,3]
#



my_list=[]
print(type(my_list)==str)
print(type(my_list)==int)
print(type(my_list)==list)

#ex1

data=[1,[2,[3]],4,[5,[6]],7,[8,[9]]]
result=[1,2,3,4,5,6,7,8,9]

def flatten_list(complex_list):
    flat_list=[]
    for obj_primary in complex_list:
        if type(obj_primary )==list:
            result= flatten_list(obj_primary)
            for obj_secondary in obj_primary:
                if  type(obj_secondary)==list:
                    for obj_third in obj_secondary:
                        if type(obj_third)==list:
                          pass
                        else:
                            flat_list.append(obj_third)
                else:
                    flat_list.append(obj_secondary)
        else:
            flat_list.append(obj_primary)
    return flat_list

result=flatten_list(complex_list=data)
print(result)

# XOR

print(10 & 10)
print((11).__and__(10))

#1010-10
#1011-11
#1010-10

print(11^10)
print((11).__xor__(10))
result=((11).__xor__(10))
result= result.__xor__(10)
print(result)

#1010-10
#1011-11
#0001-1
#1010-10
#-----
#1011-11

text= 'Éÿå°óñþðä°âõñô°äøùã'
my_list=[]
for letter in text:
    print(chr(ord(letter).__xor__(144)),sep='',end='')

print()
x='y'.join(['word1','word 2','x'])
print(x)

def encript (text, number=144):
 my_list=[]
 for letter in text:
    my_letter=chr(ord(letter).__xor__(number))
    my_list.append(my_letter)
    result=''.join(my_list)
 return result
print(encript(text))

def add_numbers():
    suma=0
    my_list=[]
    while suma<100:
        number=int(input('Enter number:'))
        suma = suma +number
        my_list.append(number)
        if suma>100:
            return my_list
    else:
        return suma
result=add_numbers()
print(result)

