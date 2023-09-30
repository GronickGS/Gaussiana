import numpy as np

def campana_gaussiana(x, mu, sigma, amplitud):
    exponente = -((x - mu) ** 2) / (2 * sigma ** 2)
    coeficiente = amplitud / (sigma * np.sqrt(2 * np.pi))
    return coeficiente * np.exp(exponente)

# Solicitar al usuario que ingrese la media, la desviación estándar y la amplitud
mu = float(input("Ingrese la media (mu): "))
sigma = float(input("Ingrese la desviación estándar (sigma): "))
amplitud = float(input("Ingrese la amplitud: "))

# Crear un arreglo de valores x
x = np.linspace(-5, 5, 100)

# Calcular la función de campana gaussiana con los valores ingresados por el usuario
y = campana_gaussiana(x, mu, sigma, amplitud)

import matplotlib.pyplot as plt
plt.plot(x, y)
plt.title('Función de Campana Gaussiana')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.grid(True)
plt.show()
