# -*- coding: utf-8 -*-
"""
Created on Wed Feb 12 05:53:21 2020

@author: Antonia Lopez
"""

#Punto 1
#En esta programa decidi solicitar un numero y luego verificar si era o no
#positivo, en caso de ser positivo se impirmía el mismo numero, si era 
#negativo, lo multiplicaba por -1 e imprimía el nuevo resultado.
print('VALOR ABSOLUTO')
punto1= float(input('Escriba un numero:'))
if punto1 <0:
    resultado= punto1 * -1
    print('El valor absoluto de', punto1,'es:', resultado)
    
else:
    print('El valor absoluto de', punto1, 'es:', punto1)
   
#%%
#Punto 2   
    
#En este programa solicité dos numeros enteros positivos, realicé la diferencia
#y el resultado lo evalue en un ciclo for, donde creé un contador que sumaba 
#las veces que la dferencia podía dividirse por un numero sin dejar residuo
#esto para saber si el número era o no primo. En caso de ser primo el contador
#debía ser igual a dos. 
print("NÚMERO PRIMO")
numero1 = int(input("Escriba un número entero positivo: "))

while numero1 <0: 
    print('Este numero no es entero positivo!')
    numero1 = int(input("Escriba un número entero positivo: "))
    
numero2= int(input("Escriba otro número entero positivo:"))
while numero2<0:  
    print('Este numero no es entero positivo!')
    numero2= int(input("Escriba otro número entero positivo:"))

    
diferencia= numero1 - numero2

contador=0
for i in range (1,diferencia+1):
    if diferencia % i == 0:
        contador +=1
        
if contador==2:
    print(diferencia,'Este número es primo')
else:
    print(diferencia,'Este número no es primo')
    
        
#%%
#Punto3
#En este programa creé una lista vacia a la cual se le añadirian elementos, si
#ciclo for de rango 100+1 se encontraban multiplos de 3. Esto se derminaba 
#conociendo el residuo que el número presentaba al dividirse entre 3, si el
#residuo era cero, el número era multiplo de 3.
#Los primero 15 multiplos se agregaban a la lista vacia creada al principio
# y luego desde el ultimo numero de esta lista, hasta cien, se empezaban a 
#evaluar los multiplos de 4 utilizando igualmente el residuo. Estos nuevos
#numeros se guardaban tambien en esta lista.         
def multiplos():
    lista1 = []


    n=0
    for x in range(1, 100):
        if (x%3 == 0):
            lista1.append(x)
            n+=1
            if n == 15:
                break
    for i in range(lista1[-1],100+1) :
        if (i%4 == 0):
            lista1.append(i)
                    
    print(lista1)
      
        
#%%
#Punto 4
#En este ejercicio solicite un punto en el espacio, el cual se determinaria si
#estaba contenido en 2 circulos ya creados, los cuales eran concentricos y 
#contaban con un radio especifico predetermindo. Luego segun el punto ingresado
# por el usuario, se determinaba si el punto estaba contenido en ambos 
#circulos, solo en uno o en ninguno. Lo anterior se lograba con condicionales
#y con operadores logicos
import math as math 
       
p= eval(input('Digite las coordenadas (a,b):'))
a= p[0]
b= p[1]
#Se aclara que el circulo 1 es el más grande, el circulo 2 es el interno.
x1=0
x2=0
y1=0
y2=0
r1 = 10
r2 = 5

distancia= math.sqrt((x2-a)**2+(x2-b)**2)

if 5<distancia<10 :
    print(p, 'Esta contenido en el circulo 1')
    
elif distancia <= r2:
    print(p, 'Esta contenido en el circulo 1 y 2')

elif distancia > r2:
    print(p, 'Esta fuera del circulo 1 y del circulo 2')
    
#aqui decidi añadir otro ejemplo de este codigo, donde el usuario puede elegir
# no solo el punto a evaluar, si no tambien los centros y los radios.
#Tambien adjunto la explicación desde cero de este código.

#Inicié solicitando las coordenadas de los centros, el valor de los radios y 
#del punto p que se quiere evaluar. Para solicitar los puntos utilice el
#comando eval, para que el usuario  pudiera ingresar los datos como 
#coordenadas(Puntos en R2). 
#Al obtener los puntos, guarde las abscisas y las ordenadas en variables
#diferentes, utilizando los indices de las coordenadas dadas.
#Después de esto procedí a hallar la longitud desde los centros de cada 
#círculo hasta el punto que se quiere evaluar p, con la ayuda de la fórmula de 
#la distancia.
#Continúe verificando en qué círculos estaba contenido el punto p con la ayuda
#del condicionl if y de operadores lógicos como and.
#Tomando en cuenta que cuando utilizamos if, elif, else el proceso de 
#verificación termina cuando se cumple alguna condición, posicioné las 
#condiciones de forma descendente, es decir, colocando las condiciones que 
#tenían más operadores lógicos de primero y finalizando con las condiciones 
#que no tenían operadores lógicos. De está forma me asegure de evaluar el 
#punto p en el mayor número de círculos posibles, en este caso 3.

import math as math 
centro1=eval(input('Digite las coordenadas del centro del círculo1:'))
x1 = centro1[0]
y1 = centro1[1]
centro2=eval(input('Digite las coordenadas del centro del círculo2:'))
x2 = centro2[0]
y2 = centro2[1]
centro3=eval(input('Digite las coordenadas del centro del círculo3:'))
x3 = centro3[0]
y3 = centro3[1]
radio1 = int(input('Digite el valor del radio1:'))
radio2 = int(input('Digite el valor del radio2:'))
radio3 = int(input('Digite el valor del radio3:'))
       
p= eval(input('Digite las coordenadas (a,b):'))
a= p[0]
b= p[1]


distancia1= math.sqrt(((x1-a)**2)+((y1-b)**2))
distancia2= math.sqrt((x2-a)**2+(y2-b)**2)
distancia3= math.sqrt((x3-a)**2+(y3-b)**2)

if distancia1 <= radio1 and distancia2 <= radio2 and distancia3 <= radio3 :
    print(p, 'Está contenido en los círculos 1, 2 y 3')
    
elif distancia1 > radio1 and distancia2 > radio2 and distancia3 > radio3 :
    print(p, 'No está contenido en ninguno de los círculos')

elif distancia1<= radio1 and distancia2 <= radio2 :
    print(p, 'Está contenido en los círculos 1 y 2')
    
elif distancia1 <= radio1 and distancia3 <= radio3 :
    print(p, 'Está contenido en los círculos 1 y 3')

elif distancia2 <= radio2 and distancia3 <= radio3 :
    print(p, 'Está contenido en los círculos 2 y 3')
        
elif distancia1<=radio1 :
    print(p, 'Está contenido en el círculo 1')
    
elif distancia2 <=radio2 :
    print(p, 'Está contenido en el círculo 2')

elif distancia3 <=radio3 :
    print(p, 'Está contenido en el círculo 3')
    
   
    
#%%
#Punto 5

#En este código se verifican las vocales mayusculas, las letras con tilde
#tanto mayusculas como minisculas, los espacios, los digitos y las palabras 
#reservadas que estan presentes en una cadena de texto previamente solicitada
#Para ello se utiliza el ciclo for para evaluar caracter por caracter dicha
#cadena
def comprobacion():
    palabra = str(input("ingrese una cadena de texto: "))
    vocales = "AEIOU"
    tildes = "áéíóúÁÉÍÓÚ"
    contador = 0
    espacio = 0
    print("ingresaron este numero de vocales de esta palabra", palabra)
    for v in vocales:
        print(v, palabra.lower().count(v))

    print("Se ingresaron estas letras con tildes")
    for v in tildes:
        "print(v, palabra.lower().count(v))"#ver detalladamente
        if(v == "á"  and v == "é" and v == "í" and v == "ó" and v == "ú" and \
           v == "Á"  and v == "É" and v == "Í" and v == "Ó" and v == "Ú"):
            contador = contador+1
    print(contador)

    print("Cuantos digitos entraron")
    for v in palabra:
        contador = contador + 1
    print("Entraron ",contador," digitos")

    print("Cuantos espacios entraron")
    for v in palabra:
        if(v == '' or v == " "):
            espacio = espacio+1
    print("Entraron ",espacio, 'espacios')

    print('cuántas palabras reservadas se entraron.')
    countpalabra = 0;
    PalabrasReservadas = ["and","except","lambda","with","as","finally",
                          "nonlocal","while","assert","false","None","yield",
                          "break","for","not","class","from","or","continue",
                          "global","pass","def","if","raise","del","import",
                          "return","elif","in","True","else","is","try"]
    for i in PalabrasReservadas:
        if (palabra == i):
            countpalabra = countpalabra+1

    print("Entraron ", countpalabra, 'palabras reservadas')

#%%
#Punto 6
#Este programa solicita una cadena de texto, y organiza alfabeticamente los
#digitos contenidos en este, reportandolo las veces que este repetido. Esto se
#logra con un ciclo for que evalua la cadena original punto a punto, posicion 
#a posicion. Los espacios tambien se incluyen. 
    
print("digite la cadena:")
cadena=input()
cadena=cadena.replace(' ', '')
lista=[]
for i in cadena:
    lista.append(i)
    lista.sort()
cadena2=''
for i in lista:
    cadena2 +=i
print(cadena2)

#%%
#Punto 7
#Este programa corre una lista de numero ya ordenados ascendentemente que 
#previamente se le solicita, se verifica que esta lista de verdad este ordenada
# y posteriormente se le solicita al usuario otro valor a ingresar en la lista
#el cual se posicionara de forma correcta. Pra esto es fundamental utilizar
#el comando de ordenamiento sort.


print("digite el arreglo:")
cadena=input()
cadena=cadena.replace(' ', '')
lista=[]
for i in cadena:
    lista.append(i)
    lista.sort()
cadena2=''
for i in lista:
    cadena2 +=i
if(cadena != cadena2):
    print("la lista no está ordenada")
else:
    print("digite el valor a ingresar a la lista")
    num=input()
    lista.append(num)
    lista.sort()
print(lista)

#%%    
#Punto 8

# En este codigo solicito una lista con el comando eval y creó una lista vacia.
# Después con la ayuda del comando max identifico el numero mayor de esta lista
# añado los números a la lista vacia, sin tener en cuenta al mayor. El ciclo 
#for cumple la función de omitir el numero mayor las veces que este se 
#encuentre en la lista solicitada. Ahora evaluo el mayor de la nueva lista y 
#de esta forma obtengo el segundo numero mayor de la lista original.
    
    
def sugundoMayor():
    list1 = eval(input('Digite por favor una lista:'))
    listanueva= []
    m = max(list1)
    for u in range(len(list1)):
        if list1[u] < m:
            listanueva.append(list1[u])
            
    print(max(listanueva))
        
        
#%%
#Punto 9

#Este programa inicialmente solicita un numero al usuario y luego por medio del
#residuo, identifica si este numero es par o impar. Si el residuo al dividirse
#entre 2 es cero, el numero es par, en caso contrario el numero es impar.
#Luego se crea una lista que inicia añadiendo el numero proporcionado por el
#usuario(U0), si es impar el proximo numero a añadir será 3(Un)+1, si es par
#el proximo numero sera (Un)/2. Siempre se tomara como referencia el numero 
#anterior. El usuario decide la magnitud de la lista despues de decidir el 
#numero inicial

punto9 = int(input('Digame el valor de U(O):'))

magnitud = int(input('Digame cuántos términos quiere:'))

lista9= [punto9]

for i in range(magnitud-1):
    if punto9 % 2 == 0:
        punto9 = int(punto9/2)
        lista9.append(punto9)  
        
    else:
        punto9 = int(punto9*3 +1)
        lista9.append(punto9) 
        
print(lista9)
      
#%%

#Punto 10

#El objetivo de este programa, era generar una matriz con numeros aleatorios
#con la libreria random y con el comando .randint, despues empezar a 
#desenvolver la matriz en forma de espiral, para hacer esto se utilizo varios
#ciclos for que llamaban las filas o columnas de la matriz, para posteriormente
#ordenar una lista con el orden deseado, es decir, en espiral.

import random
n = int(5)
matriz=[None]*n
for i in range(0,n):
    matriz[i] = [None]*n
for i in range(0,n):
    for j in range(0,n):
        matriz[i][j] = (int)(random.randint(1,1001))
print(matriz)
for i in range(n-1,-1,-1):
    if(i%2==0):
        for j in range(n-1,-1,-1):
            print (matriz[j][i])
    else:
        for j in range(0,n):
            print (matriz[j][i])  
        
#%%
#Punto 11
#Esta función solicita 2 numeros, que representan la anchura y la altura de un
#rectángulo y un caracter con el cuál se dibujara en la pantalla.
#Para dibujar el rectangulo con las medidas especificadas, se utilizan dos 
#ciclos for, uno para la anchura y otro para la altura y por ultimo imprime el 
#caracter las veces que indico el usuario.

def rectángulo():
    anchura = int(input("Anchura del rectángulo: "))
    altura = int(input("Altura del rectángulo: "))
    caracter = int(input("Carácter a Utilizar:"))
    
    for i in range(altura):
        for j in range(anchura):
            print(str(caracter), end="")
        print()

#%%
#Punto 12
#Esta función  solicita un numero, el cual representa la anchura de un 
#triangulo que se procedera a dibujar con asteriscos(*). Para esto se utiliza 
#un primer ciclo for que dibuja la parte de arriba, es decir desde 1 hasta la 
#anchura especificada mas 1 y luego se utiliza otro ciclo for que va desde
#la anchura especificada-1 hasta 1 para asi dibujar la parte de abajo.
def triángulo():

    anchura = int(input("Anchura del triángulo: "))
    
    for i in range(1, anchura + 1):
        for j in range(i):
            print("* ", end="")
        print()
    
    for i in range(1, anchura):
        for j in range(anchura - i):
            print("* ", end="")
        print()
        
#%%
#Punto 13
#En esta funcion se solicitan dos años con la condicion de que el segundo sea
# mayor al primero y se encuentran los años bisiestos que puedan haber en este
#rango, esto se hace con ayuda de los residuos y de operadores logicos como and
# y or y un ciclo for que evalua el rango entre los años ya mencionados.

def es_bisiesto(t):
    return t % 400 == 0 or (t % 100 != 0 and t % 4 == 0)

print("Contador de años bisiestos")
inicio = int(input("Escriba un año: "))
print("Escriba otro año posterior a", str(inicio) + ": ", end="")
final = int(input())
while final < inicio:
    print(final, "no es mayor que", str(inicio) + ". Inténtelo de nuevo: ",
          end="")
    final = int(input())

contador = 0
for i in range(inicio, final + 1):
    if es_bisiesto(i):
        contador += 1

print("De", inicio, "a", final, "hay", final - inicio + 1, "años,",
      contador, "de ellos bisiestos.")

#%%
#Punto 14
#Esta funcion genera dos numero aleatorios entre 1 y 100, con la libreria 
#random y el comando .randint y le pregunta al usuario la suma de dichos 
#numeros, hasta que el usuario acierte, la funcion le dira que la respuesta es 
#incorrecta y le seguira preguntando. Lo anterior se logra con un ciclo while 
# que solo se rompe cuando el usuario acierta 5 veces. Esto se controla con un 
#contador creado ntes del while.

def sumas():
    import random as rd
    
    print('Escriba el resultado de las siguientes operaciones:')
    
    n= 0
    
    while n!=5:
        a= rd.randint(0,100)
        b= rd.randint(0,100)
    
        rusuario= int(input(f'{a}+{b}='))
        
        resultado= a+b
        
        if (rusuario==resultado):
            n+=1
            print('¡RESPUESTA CORRECTA!')
            
        elif(rusuario!=resultado):
            print('¡RESULTADO INCORRECTO!')
            
    
    print('Programa Terminado')

#%%
#Punto 15
#En este juego, se genera una caden aleatoria con random.randint y con la 
#longitud deseada por el usuario.
#El usuario debe adivinar la cadena o el programa le seguira preguntando, 
#lo cual se logra con un ciclo while. En cada intento el programa reporta los
#aciertos alcanzados.
    
import random as rd

def mastermind():
    long= int(input('Digite la longitud de la cadena entre (2 y 9):'))
    cadena = ''
    
    for i in range(long):
        aleatorio= rd.randint(0,9)
        cadena+= str(aleatorio)
    print(cadena)   
    intentos = input('Por favor adivine la cadena:')
    
    c= intentos
    
    while c != cadena:
        print('Se ha equivocado, vuelva a intentarlo')
            
        intentos = input('Por favor adivine la cadena:')
        v= 0
        for z in range(0,len(cadena)):
            if cadena[z] == intentos[z]:
                v += 1
        print('Ha adivinado', v, 'palabras')
        
    print('Ha adivinado completamente la cadena')    
    
     