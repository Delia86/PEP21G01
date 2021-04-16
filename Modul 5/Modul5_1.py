def divide(number,divider):
    try:
        raise AttributeError
        if number==0:
            raise Exception
        result=number/divider
    except ZeroDivisionError:
        print('This is a Zero Division error')
        return None
    except AttributeError:
        print('This is an attribute error')
        result= None
    except Exception:
        print('This is an exception')
        return None
    else:
        print('The code executed successfully',result)
    finally:
        print('This will always happen')
    return result
print(divide(2,1))
print('The end')

# pb

list1=[1,10,-2,'100',None,{}]

def compare(my_list):
    result=[]
    for elem in my_list:
        if not result:
            result.append(elem)
            continue
        for obj in result.copy():
            try:
                check=elem<obj
            except TypeError as e:
                print (e.args[0].split("'")[3])
                if e.args[0].split("'")[3]=='str':
                    elem=int(elem)
                elif e.args[0].split("'")[3] == dict:
                    elem=len(elem)
                elif e.args[0].split("'")[3] == 'NoneType':
                    elem = len(str(elem))
                continue
            if elem < obj:
                print (result.index(obj))
                result.insert(result.index(obj),elem)
                break
        else:
            result.append(elem)
    print(result)
compare(list1)

#ex reset global vars on finally/else

var1 = None
var2 = None
var3 = None


def read_input():
    global var1, var2, var3
    try:
        var1 = int(input())
        var2 = int(input())
        var3 = int(input())
        result = var1 + var2 + var3
    except:
        var1, var2, var3 = None, None, None
    else:
        var1, var2, var3 = result, result, result
    finally:
        #?? find out how to check if a variable exists
        return result
read_input()
print(var1, var2, var3)


#Module

