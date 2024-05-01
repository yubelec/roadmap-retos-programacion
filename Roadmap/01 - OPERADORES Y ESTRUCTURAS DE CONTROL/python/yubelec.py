# OPERADORES
# Arítmeticos
sum = 20 + 6
print(sum)

resta = 20 - 6
print(resta)

multi = 20 * 6
print(multi)

div = 20 / 6
print(div)

mod = 20 % 6
print(mod)

exp = 10 ** 3
print(exp)

dive = 10 // 3
print(dive)

#Lógicos

print(True and True)   
print(True and False)  
print(False and True)  
print(False and False) 

print(True or True)   
print(True or False)  
print(False or True)
print(False or False)

print(not True)
print(not False)
print(not not not not True)

#Comparación

print(20 == 6)
print(20 != 6)
print(20 > 6)
print(20 < 6)
print(20 <= 6)
print(20 >= 6)

# Asignación
a=10; b=7
x=a; x+=b;  print("x+=", x)

x=2      
print(x)

x=5
x+=1
print(x)

i = 5
i -= 1
print(i)

a=10; b=2
a*=b      
print(a)

x = 3
x%=2
print(x)

x=5
x//=3
print(x)

x=5      
x**=3
print(x) 

#Identidad
a = 10
b = 10

print(a is b)

a = 5
b = 5

print(a is not b)

# Pertenencia

print(3 in [1, 2, 3])
print(3 not in [1, 2, 4, 5])

# Bitwise

print(f"AND: 10 & 3={10&3}")
print(f"OR: 10 & 3={10|3}")
print(f"XOR: 10 & 3={10^3}")
print(f"NOT: 10 & 3={~10}")
print(f"Desplazamiento a la derecha: 10 >> 3={10 >> 2}")
print(f"Desplazamiento a la izquierda: 10 << 3={10 >> 2}")


# Condicional

x = 6
if not x%2:
    print("Es par")
else:
    print("Es impar")
    
x = 5
x-=1 if x>0 else x
print(x)

# Iterativa
for i in range(0, 5):
    print(i)

i=0
    
while i <=7:
    print(i)
    i +=1
    
#Excepciones
try:
    print (10/0)
except:
    print("Error Error")
finally:
    print("Fin")
    
#Extra

for number in range(10,56):
    if number %2 ==0 and number !=16 and number %3 !=0:
        print(number)

