# 1: Definición de una función
def say_hello():
    print('Hello!')

say_hello()
def one():
    return 1
print(one())
if one() == 1:
    print("It's work!")
else:
    print("Something is broken")
def empty():
    x = 0
print(empty())
# 2: Veracidad
def truthiness(obj):
    if obj:
        print(f'{obj} is True')
    else:
        print(f'{obj} is False')
truthiness(True)
truthiness(False)
# Parámetros y argumentos
def _min(a, b):
    if a < b:
        return a
    else:
        return b
print(_min(7,9))
def exercise(x, y):
    return x**2 + y**2
print(exercise(3, 4))
def build_cpu(vendor, num_cores, freq=2.0):
    return dict(
        vendor = vendor,
        num_cores = num_cores,
        freq = freq
    )
print(build_cpu('AMD', 8, 2.4))
print(build_cpu('INTEL', 4))
def factorial(n):
    f=1
    for i in range(1,n+1):
        f = f*i
    return f
print(factorial(5))
