# Funciones Interirores
"""def validation_test(text):
    def is_valid_char(char):
        return char in 'xyz'
    checklist = []
    for char in text:
        checklist.append(is_valid_char(char))

    return sum(checklist)/len(text)
print(validation_test("abzyxabcdz"))
def extraer_vovales(texto):
    def validar_vovales(vocal):
        if vocal in "aeiou":
            return vocal
        else:
            return '-'
    resultado = []
    for vocal in texto:
        resultado.append(validar_vovales(vocal))
    resultado = list(''.join(resultado).replace('-',''))
    return resultado
print(extraer_vovales("hola"))
# Clausuras
def make_printer(msg):
    msg = "hi there"
    def printer():
        print(msg)
    return printer
my_printer = make_printer("ga")
my_printer()
def make_multiplier_of(n):
    def multiplier(x):
        return x*n
    return multiplier
m2 = make_multiplier_of(2)
print(m2(100))"""
# Funciones Anónimas "LAMBDA"
num_words = lambda t: len(t.strip().split())
datos = ['como te llamas', 'buenos dias', 'comprar una botella de leche']
x = [num_words(x) for x in datos]
for i, x in enumerate(map(num_words, datos), start=1):
    print(i,'.- tiene ', f'{x} palabras')
logic_and = lambda x, y: x & y
for i in range(2):
    for j in range(2):
        print(f'{i} & {j} = {logic_and(i,j)}')
productos=[{'nombre': 'Teclado', 'precio': 54.9, 'color': 'black'}]

geolog = (
    (13.1, 12.0),
    (16.2, 19.5),
    (-13.8, 72.0)
)
print(sorted(geolog, key=lambda x: x[1]))
# Enfoque funcional "MAP","FILTER","REDUCE"
contar = list(map(num_words, datos))
print(contar)
numeros = [1,2,3,4,5,6,7]
pares = list(filter(lambda x: x % 2 == 0,numeros))
print(pares)
from functools import reduce
suma = reduce(lambda x, y: x + y, numeros)
suma2 = lambda x, y , *args: x+y+ args, numeros
print(suma)
print(suma2)
