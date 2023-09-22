#calcula a média entre dois valores

def media (a, b):
    s= a+b
    m= s/2
    return m

def mediaponderada( a, b, pa, pb):
    s = a*pa + b*pb
    p = pa + pb 
    m = s / p 
    return m

print(media(7,8))
print(mediaponderada(7,8,10,5))


#int: numero inteiro
#str: palavras
#float: numero decimal

#import math ( permite que o programa execulte 
# calculos matematicos )

#else: se não conseguiu faça isso.

#função recursiva é quando a função é
#implementada nela mesma.

def fatorial ( i:int ):
    if ( i == 1 ): return 1
    else:
        return i * fatorial ( i-1 )
    
print (fatorial(8))
print (fatorial(9))
print (fatorial(15))
print (fatorial(3))