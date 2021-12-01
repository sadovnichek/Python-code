import sys
import traceback

class A:
    def f(self):
        print('A.f')

class B(A):
    def g(self):
        print('B.g')

class C(B):
    def f(self):
        print('C.f')

a = A()
b = B()
c = C()

# print(isinstance(c, A)) # True
# print(C.__bases__) # B
# print(B.__subclasses__()) # C

try:
    a = 1 / 0
except:
    t, v, tb = sys.exc_info()
    print(traceback.print_exception(t, v, tb))
else:
    print('no exceptions')
finally:
    print('finally')
