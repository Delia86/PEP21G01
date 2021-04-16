# Write a function that takes in a list of objects and converts each object in the list into a int.
# For objects that can't be directly converted to int should have their length counted
# The function will return a list with a int values ordered from largest to smallest.
# example [1, True, '123', False, 6, ()] will be transformed into [123, 6, 1, 1, 0, 0]

# ordered_list=[]
# def ordered_ints(list_of_objects: list):
#     for elem in list_of_objects:
#         if type (elem)== 'str':
#             list_of_objects[elem]=int(list_of_objects[elem])
#             ordered_list.append(elem)
#         elif type (elem)==bool:
#             list_of_objects[elem] = int(list_of_objects[elem])
#             ordered_list.append(elem)
#
#         else:
#             ordered_list.append(elem)
#
#
# print(ordered_ints(ordered_list))

#
# ints_list=[]
# def ordered_ints(list_of_objects: list):
#     for object in list_of_objects:
#         if type(object)== int:
#             ints_list.append(object)
#         elif type(object) == bool:
#             bool_object=int(object==True)
#             ints_list.append(bool_object)
#         elif type(object) is str:
#             str_object=int(object)
#             ints_list.append(str_object)
#         elif type(object) is tuple:
#             tuple_object=0
#             ints_list.append(tuple_object)
#         else:
#             print("The list is already updated")
#
#     return(sorted(ints_list,reverse=True))
#
# print(ordered_ints([1, True, '123', False, 6, ()]))



# def ordered_ints(list_of_objects:list):
#     for elem in range (0,len(list_of_objects)):
#         list_of_objects[elem]=int(list_of_objects[elem])
#
#         return sorted(list_of_objects)
#
# print(ordered_ints([1,True,'123',False,7,()]))



# 25P - (do not rush to resolve this)
# For recursive functions try reading the articles below if you find need more information
# https://realpython.com/python-thinking-recursively/
# https://www.python-course.eu/python3_recursive_functions.php
# After reading the above articles try creating a function to calculate the series (1^2)+(2^2)+(3^2)...(n^2)
# The function will receive an int that indicate the number of iterations, or how many times we have (x^2)+
# when resolving try using this logic: 1^2+2^2 is 1^2+(1^2+1^2)^2
#
# def sum_of_square(n: int):
#     sum= 0
#     for i in range (1,n+1):
#         sum=sum +pow(i,2)
#     return sum
#
# print(sum_of_square(10))


# 25P
# Write a function that will calculate factorial of numbers squared.
# For n = 3 the function should calculate (1^2)*(2^2)*(3^2)

# def factorial_of_squares(n: int):
#     if n**2==1:
#         return 1
#     else:
#         return n**2factorial_of_squares(n-1)
#
# print(factorial_of_squares(5))



# 25P
# Write a function that takes in a string as argument and returns a tuple after performing the following actions:
# - the string is split after the first encountered space.
# - all letters in the first half will be transformed to upper case letters
# - all characters that are not lower-case letters in the second half will be replaced with "_"
# - returned tuple contains the two processed strings
# example: "1234567a Text to te5t" will become ("1234567A", "_ext_to_te_t")
#


def process_text(text: str):
    for chr in text:
        if chr==" ":
            text=text.split(" ",maxsplit=1)
            text1=text[0]
            text2=text[1]
            tup_1=tuple([text1.upper()])
            for chr in text2:
                if chr.isupper():
                    text2=text2.replace(chr,"_")
                elif chr.isdigit():
                    text2=text2.replace(chr,"_")
            tup_2=tuple([text2])
            return tup_1+tup_2


print(process_text('1234567a Text to te5t'))






