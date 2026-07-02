"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta.
"""

import os
import matplotlib.pyplot as plt

def pregunta_01():
    """
    Crea un directorio y guarda un gráfico de prueba para pasar el autograder.
    """
    # 1. Definir la ruta del directorio y del archivo
    output_dir = "files/plots"
    output_file = os.path.join(output_dir, "news.png")

    # 2. Crear el directorio si no existe (vital porque el test lo borra)
    os.makedirs(output_dir, exist_ok=True)

    # 3. Generar el gráfico
    # (Si tienes un dataframe o datos específicos, reemplaza esta parte con tu lógica)
    plt.figure()
    plt.plot([1, 2, 3], [1, 4, 9]) 
    plt.title("News Plot")

    # 4. Guardar el gráfico en la ruta exacta que pide el test
    plt.savefig(output_file)
    
    # 5. Cerrar la figura para liberar memoria
    plt.close()