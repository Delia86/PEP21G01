# import random
#
# def check_cpu():
#     output = """top - 16:18:11 up  5:12,  2 users,  load average: 0.12, 0.03, 0.01
# Tasks: 138 total,   1 running, 137 sleeping,   0 stopped,   0 zombie
# %Cpu(s):  {} us,  0.0 sy,  0.0 ni, {} id,  0.0 wa,  0.0 hi,  0.0 si,  0.0 st
# MiB Mem :   7962.4 total,   7176.4 free,    164.8 used,    621.1 buff/cache
# MiB Swap:   1971.0 total,   1971.0 free,      0.0 used.   7552.2 avail Mem """
#     while True:
#         yield output.format(random.randint(0, 100), random.randint(0, 100))
# # print(type(check_cpu())
#
# from time import sleep
# for i in check_cpu():
#     counter = 0
#     for line in i.splitlines():
#         counter += 1
#         if line.startswith('%'):
#            list1 = line.split(':')[1].split(',')
#            print(list1)
#            print(int(list1[0].strip().split(' ')[0]))
#            print(int(list1[3].strip().split(' ')[0]))
#            if (int(list1[0].strip().split(' ')[0]) > 80 or int(list1[3].strip().split(' ')[0]) > 80):
#                print('Alarm!!!')
#
#     sleep(2)

# generators
def values_3():
    yield 1
    yield 2
    yield 3
gen =values_3()
print(type(gen))
print(gen.__next__())
print(next(gen))
print(next(gen))
# print(next(gen))

def values_inf():
    counter=0
    while True:
        if counter >20:
           break

        counter+=1
        yield counter
gen=values_inf()
for value in gen:
    print(value)


def values_inf():
    counter=0
    for counter in range (1,25):
        yield counter
        counter += 1
gen=values_inf()
for value in gen:
    print(value)


def string_gen(my_str):
    for char in my_str:
        yield char
gen=string_gen('blabla')
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))

# Generatorul va primi ca si argument un IP cu masca din subnet-ul dorita (ex: ‘192.168.0.3/24’)
# Generatorul va verifica daca IP-ul si masca sunt corecte
# La final generatorul va fi iterat si valorile sale printate

import random
def ip_generator(subnet):
    ip,mask=subnet.split('/')
    print(ip, mask, sep=('\n'))
    if mask!='24':
        raise ValueError('Mask is incorrect')
    ip4=ip.rsplit('.',maxsplit=1)[0]
    print(ip4)
    for i in random.sample(range(0,256),k=256) :
        new_ip=ip4+'.'+str(i)
        yield new_ip +'/'+mask


ip_gen=ip_generator ("192.168.0.3/24")
for j in ip_gen:
    print(j)

def ip_gen():
    ip = '192.168.0.{}/24'
    list1 = random.sample(range(0, 10), 10)
    for x in list1:
            yield ip.format(x)

gen = ip_gen()
for value in gen:
    print(value)
    sleep(0.5)