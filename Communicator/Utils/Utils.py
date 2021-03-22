# def primes(max_prime):
#     my_primes = []
#
#     print('Primes are: ', end='')
#     for number in range(1, max_prime + 1):
#         if number < 3:
#             _primes.append(number)
#             continue
#         for divider in range(2, number):
#             if number % divider == 0:
#                 break
#         else:
#             primes.append(number)
#     return primes
#
#
# text='You cannot read this'
# def encript (text, number=144):
#  my_list=[]
#  for letter in text:
#     my_letter=chr(ord(letter).__xor__(number))
#     my_list.append(my_letter)
#     result=''.join(my_list)
#  return result
# print(encript(text))
#
#
# def add_numbers():
#     suma=0
#     my_list=[]
#     while suma<100:
#         number=int(input('Enter number:'))
#         suma = suma +number
#         my_list.append(number)
#         if suma>100:
#             return my_list
#     else:
#         return suma
# result=add_numbers()
# print(result)
#
# data=[1,[2,[3]],4,[5,[6]],7,[8,[9]]]
# resoult=[1,2,3,4,5,6,7,8,9]
#
# def flatten_list(complex_list):
#     flat_list=[]
#     for obj_primary in complex_list:
#         if type(obj_primary )==list:
#             result= flatten_list(obj_primary)
#             flat_list.extend(result)
#
#         else:
#             flat_list.append(obj_primary)
#     return flat_list
#
# resoult=flatten_list(complex_list=data)
# print('Flat list:',resoult)
#
# [19: 27] Mario
# Cioara
#
# test_data = [[1, 2, 3], [3, 3, 5], [8, 9, 4], [2, 8, 4]]
#
#
# def func(data_set):
#     full_data = set()
#     set_test_data = set()
#     miss_data = set()
#     for z in range(1, 11):
#         full_data.add(z)
#     for x in data_set:
#         for y in x:
#             set_test_data.add(y)
#     miss_data = full_data.difference(set_test_data)
#     return list(miss_data)
#
#
# print(func(test_data))
#
# ​[19: 28] Mario
# Cioara
#
# test_data = [[1, 2, 3], [3, 3, 5], [8, 9, 4], [2, 8, 4]]
#
#
# def func(data_set):
#     full_data = set(range(1, 11))
#     set_test_data = set()
#     for x in data_set:
#         set_test_data = set_test_data.union(set(x))
#
#     return list(full_data.difference(set_test_data))
#
#
# print(func(test_data))



name='Sir'

def hello ():
    print(f'Hello,{name}!')

def question():
    print(f"how is your day {name}?")

def response():
    name=input('My name is ')
    print(f'My name is:{name}')

hello()
response()
question()

data=[1,[2,[3,{'a','b'}]],4,[5,[6,{'a':'a','b':'b'}]],7,[8,[9,('a','b')]]]
resoult=[1,2,3,4,5,6,7,8,9]


def flatten_list(complex_list):
    flat_list=[]
    for obj_primary in complex_list:
        if type(obj_primary )==list:
            result= flatten_list(obj_primary)
            flat_list.extend(result)
        elif type(obj_primary)==tuple:
            result = flatten_list(obj_primary)
            flat_list.extend(result)
        elif type(obj_primary)== set:
            result = flatten_list(obj_primary)
            flat_list.extend(result)
        elif type(obj_primary)== dict:
            result = flatten_list(obj_primary)
            flat_list.extend(result)
        else:
            flat_list.append(obj_primary)
    return flat_list

resoult=flatten_list(complex_list=data)
print('Flat list:',resoult)

data=[1,[2,[3,{'a','b'}]],4,[5,[6,{'a':'a','b':'b'}]],7,[8,[9,('acd','b')]]]
resoult=[1,2,3,4,5,6,7,8,9]


def flatten_list(complex_list):
    flat_list=[]
    for obj_primary in complex_list:
        if type(obj_primary)==str and len(obj_primary)==1:
            flat_list.append(obj_primary)
        elif getattr(obj_primary.__iter__,False)
            result= flatten_list(obj_primary)
            flat_list.extend(result)
        else:
            flat_list.append(obj_primary)
    return flat_list

resoult=flatten_list(complex_list=data)
print('Flat list:',resoult)