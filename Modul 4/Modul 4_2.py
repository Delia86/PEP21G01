# #set
#
# empty_set=set()
# print(type(empty_set))
#
# set1={1,2,3}
# set2={2,3,4}
# intersect=set1.intersection(set2)
# print(intersect)
#
# union=set1.union(set2)
# print(union)

# pinball test with 10  possible result
test_data=[[1,2,3],[3,3,5],[8,9,4],[2,8,4]]
iter_test_data=[]
def pinball_test(data):
    comparison_data=list(range(1,11))
    print(comparison_data)
    for test_data in comparison_data.copy():

        for iner_list in data:
            for elem in iner_list:
                if elem in comparison_data:
                    comparison_data.remove(elem)
    return comparison_data


resoult=pinball_test(test_data)
print(resoult)

set1={0,1,2,3}
set2={2,3,4,5}
print('Diff3:',set1.symmetric_difference(set2))
print('Diff3:',set2.symmetric_difference(set1))
print('Diff3:',set1.symmetric_difference_update(set2))
print(set1)

var1='var1'
def outer():
    global  var1
    var1='something new'
    print(var1)

print('outside',var1)
outer()
print('outside',var1)

def func1():
    global var1
    print(f'in func1"{var1}')



def wrapper():
    name = "Sir" # This is not used
    def conversation():
        name = "Lady"

        def hello():
            nonlocal name
            print(f"Hello {name}")

        def question():
            print(f"how is your day {name}?")
        def response():
            nonlocal name
            name = input("My name is ")
            print(f"My name is :{name}")
        hello()
        response()
        question()
        conversation()
wrapper()

#recursivitate
#3!= 1*2*3

def factorial(number):
    number=list(range(1,number+1))

    if len (number)<=1:
        return 1
    else:
        return number[-1]*factorial(number[-2])

print(factorial(3))

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

