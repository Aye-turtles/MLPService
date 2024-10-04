import pandas as pd
from sklearn.preprocessing import StandardScaler
import tensorflow as tf

def evaluate(filePath):
    # Leer el archivo CSV
    data_prueba = pd.read_csv(filePath)

    # Seleccionar las columnas relevantes para el modelo
    x_prueba = data_prueba[['X', 'Y', 'Z', 'Energy', 'Temp']]

    # Normalizar los datos
    scaler = StandardScaler()
    x_prueba_scaled = scaler.fit_transform(x_prueba)
    print("SI entra antes de cargar el modelo")
    # Cargar el modelo preentrenado
    modelo = tf.keras.models.load_model('model.h5')

    # Hacer la predicción de probabilidades
    predicciones_probabilidades = modelo.predict(x_prueba_scaled)

    # Definir el umbral para clasificar los comportamientos
    umbral = 0.5
    predicciones_clases = (predicciones_probabilidades > umbral).astype(int)

    # Agregar las predicciones al DataFrame original (solo en memoria)
    data_prueba['Prediccion_Comportamiento'] = predicciones_clases

    # Calcular el número total de registros
    total_registros = len(data_prueba)

    # Calcular el número de registros con comportamiento = 1
    registros_comportamiento_1 = len(data_prueba[data_prueba['Prediccion_Comportamiento'] == 1])

    # Calcular el porcentaje de registros con comportamiento = 1
    porcentaje_comportamiento_1 = (registros_comportamiento_1 / total_registros) * 100

    return porcentaje_comportamiento_1
