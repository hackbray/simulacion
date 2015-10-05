# -*- coding: cp1252 -*-

import numpy as np
import math
import matplotlib.pyplot as plt



def randuX(n):
    """
    Generador Congruencial Mixto  Xn = (170*Xn-1 + 1) mod 30323.
    Devuelve una lista que tiene n valores aproximados a una distribución uniforme.
           """
    #Semilla
    x0 = 7          
    valores = []

    for i in range(0,n):
        xi = (170*x0 + 1)%30323
        ui = xi/30323.0
        valores.append(ui)
        x0 = xi
    
    return valores


def randuY(n):
    """
    Generador Congruencial Mixto  Xn = (170*Xn-1 + 1) mod 30323.
    Devuelve una lista que tiene n valores aproximados a una distribución uniforme.
           """
    #Semilla
    x0 = 7         
    valores = []

    for i in range(0,n):
        xi = (172*x0 + 1)%30307
        ui = xi/30307.0
        valores.append(ui)
        x0 = xi

    return valores


def calcular_area_circulo(r):
    """Devuelve el área del circulo con radio r."""

    #Número de coordenadas (x,y) para generar. 
    num = 500

    #Obteniendo lista de valores Ux.                   
    coordenadasUx = randuX(num)

    #Obteniendo lista de valores Uy.  
    coordenadasUy = randuY(num)  
    coordenadasXi = []
    coordenadasYi = []

    # 2*k = valor para el lado del cuadrado en el cual se registrará el círculo.
    k = r       
    
    #Conversión de las coordenadas [Ux,Uy] en el rango [0,1], 
    #Obteniendo los valores para las nuevas coordenadas [Xi,Yi] en el rango [-r,r].
    for i in range(0, num):
        xi = 2*k*coordenadasUx[i]-k
        coordenadasXi.append(xi)
        yi = 2*k*coordenadasUy[i]-k
        coordenadasYi.append(yi)
        
    #Graficando el círculo registrado en un cuadrado de lado 2*k .  
    x = np.arange(-r,r+1,0.01)

    # Obteniendo los valores de y con la función para el circulo 
    # Centro en (0,0);  y = raízCuadrada(r^2 - x^2)
    y = np.sqrt(r**2 - x**2) 
    y1 = -y
    x1 = np.arange(-k,k,0.01)
    y2 = 0*x1 + k
    y3 = 0*x1 -k
    y4 = np.arange(-k,k,0.01)
    x2 = 0*y4 + k
    x3 = 0*y4 - k
    plt.plot(x,y)
    plt.plot(x,y1,color='blue')
    plt.plot(x1,y2,color='red')
    plt.plot(x1,y3,color='red')
    plt.plot(x2,y4,color='red')
    plt.plot(x3,y4,color='red')
    
    cont = 0    
    for i in range(0, num):
        xi = coordenadasXi[i]
        yi = coordenadasYi[i]
        if r**2 >= (xi**2 + yi**2):
           cont = cont + 1        
           plt.plot(coordenadasXi[i], coordenadasYi[i], 'ro')
        else:
           plt.plot(coordenadasXi[i], coordenadasYi[i], 'go')
    
   
    areaEstimada = (cont/float(num))*((2*r)**2)
    areaReal = math.pi*(r**2)
    
    plt.axis([-k-3, k+3, -k-3, k+3 ])
    plt.xlabel('Coordenadas x')  
    plt.ylabel('Coordenadas y')  
    plt.title('Area real = ' + str(areaReal) + '\nArea estimada = ' + str(areaEstimada) + 
    '\nError = ' + str(abs(areaReal-areaEstimada)) )
    plt.show()
    
