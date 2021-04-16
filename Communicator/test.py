def test()
print('test')

# class A:
#     def __str__(self):
#         return 'a'
#
#
# class B(A):
#     def __str__(self):
#         return 'b'
#
#
# class C(A,B):
#     pass
#
#
# o = C()
# print(o)

# try:
#     raise Exception(1,2,3)
# except Exception as e:
#     print(len(e.args))
# def f (x):
#     try:
#         x=x/x
#     except:
#         print('a',end='')
#     else:
#         print('b',end='')
#     finally:
#         print('c',end='')
# f(1)
# f(0)

# class A:
#     X=0
#     def __init__(self,v=0):
#         self.Y=v
#         A.X+=v
#
# a=A()
# b=A(1)
# c=A(2)
# print(c.X)
#
# class Ex(Exception):
#     def __init__(self,msg):
#         Exception.__init__(self,msg+msg)
#         self.args=(msg,)
# try:
#     raise Ex('ex')
# except Ex as e:
#     print(e)
# except Exception as e:
#     print(e)
#
# class A:
#     def __init__ (self):
#         pass
# a=A(1)
# print(hasattr(a,'A'))
#
# class A:
#     pass
#
# class B(A):
#     pass
# class C(B):
#     pass
#
# print(issubclass(C,A))
#

# class I:
#     def __init__(self):
#         self.s='abc'
#         self.i=0
#     def __iter__(self):
#         return self
#     def __next__(self):
#         if self.i== len(self.s):
#             raise StopIteration
#         v=self.s[self.i]
#         self.i+=1
#         return v
#
# for x in I:
#     print(x, end='')

# class A:
#     v=2
#
# class B(A):
#     v=1
#
# class C(B):
#     pass
#
# o=C()
# print(o.v)
#
#
# class A:
#     A=1
# print(hasattr(A,'A'))
#
# class A:
#     def __init__(self,v=1):
#         self.v=v
#
#     def set(self,v):
#         self.v=v
#         return v
# a=A()
# print(a.set(a.v+1))
#
# class A:
#     def __init__(self, v):
#         self.__a=v+1
# a=A(0)
# print(a.__a)
#
#
# class A:
#     pass
# class B(A):
#     pass
# class C (B):
#     pass
#
# print(__name__)
#
# print(issubclass(A,C))

# class A:
#     A=1
#     def __init__(self):
#         self.a=0
#
# print(hasattr(A,'a'))

# x="\\\"
# print(len(x))


# class A:
#     def __init__(self,v=2):
#         self.v=v
#
#     def set(self,v=1):
#         self.v+=v
#         return v
# a=A()
# b=a
# b.set()
# print(a.v)
#
# class A:
#     def __init__ (self):
#         pass
# a=A(1)
# print(hasattr(a,'A'))

#
# try:
#     raise Exception(1,2,3)
# except Exception as e:
#     print(len(e.args))

# print(chr(ord('p')+2))

# # file a.py
# print('a',end='')
#
# # file b.py
# import a
# print('b',end='')
#
# # file c.py
# print('c',end='')
# import a
# import b

# class A:
#     def a (self):
#         print('a')
#
# class B(A):
#     def b(self):
#         print('b')
#
# class C (B,A):
#     def c(self):
#         self.a()
#
# o=C()
# o.c()

try:
    raise Exception
except BaseException:
    print('a')
except Exception:
    print('b')
except:
    print('c')