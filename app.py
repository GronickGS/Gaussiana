# Importar la biblioteca NumPy para cálculos numéricos
import numpy as np

# Definir una función para la campana gaussiana con parámetros x, mu, sigma y amplitud
def campana_gaussiana(x, mu, sigma, amplitud):
    # Calcular el exponente de la campana
    exponente = -((x - mu) ** 2) / (2 * sigma ** 2)
    
    # Calcular el coeficiente de la campana gaussiana
    coeficiente = amplitud / (sigma * np.sqrt(2 * np.pi))
    
    # Calcular y devolver el valor de la campana gaussiana
    return coeficiente * np.exp(exponente)

# Solicitar al usuario que ingrese la media (mu), la desviación estándar (sigma) y la amplitud
mu = float(input("Ingrese la media (mu): "))
sigma = float(input("Ingrese la desviación estándar (sigma): "))
amplitud = float(input("Ingrese la amplitud: "))

# Crear un arreglo de valores x que representan el dominio de la función
x = np.linspace(-5, 5, 100)

# Calcular la función de campana gaussiana con los valores ingresados por el usuario
y = campana_gaussiana(x, mu, sigma, amplitud)

# Importar la biblioteca Matplotlib para trazar gráficos
import matplotlib.pyplot as plt

# Trazar la función de campana gaussiana
plt.plot(x, y)  # Trazar los valores de x contra y
plt.title('Función de Campana Gaussiana')  # Agregar un título al gráfico
plt.xlabel('x')  # Etiqueta del eje x
plt.ylabel('f(x)')  # Etiqueta del eje y
plt.grid(True)  # Habilitar las líneas de la cuadrícula en el gráfico

# Mostrar el gráfico resultante
plt.show()
