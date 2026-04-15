import pandas as pd
import time

from ingestion._pycache_.lectura_csv import leer_datos_csv
from ingestion._pycache_.leer_batch import leer_datos_batch
from ingestion._pycache_.fuente_realtime import leer_clima_tiempo_real

def run_orchestator():
    almacen_datos = {}

    print("--- Lectura de csv")
    almacen_datos["Titanic"]=leer_datos_csv()

    print("--- Lectura de titulos libros")
    almacen_datos['Libros']=leer_datos_batch

    total_lecturas=[]

    print("--- Lectura del clima en tiempo real")
    for i in range(5):
        df_lectura=leer_clima_tiempo_real()
        if not df_lectura.empty:
            total_lecturas.append(df_lectura)
            time.sleep(5)
    if total_lecturas:
        almacen_datos['clima']=pd.concat(total_lecturas,ignore_index=True)
    return almacen_datos

if __name__ =="__main__":
    results=run_orchestator()