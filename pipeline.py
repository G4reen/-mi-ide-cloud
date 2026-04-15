import pandas as pd
import time

from ingestion._pycache_.lectura_csv import leer_datos_csv
from ingestion._pycache_.leer_batch import leer_datos_batch

def run_orchestator():
    almacen_datos = {}

    print("--- Lectura de csv")
    almacen_datos["Titanic"]=leer_datos_csv()

    print("--- Lectura de titulos libros")
    almacen_datos['Libros']=leer_datos_batch
    return almacen_datos

if __name__ =="__main__":
    results=run_orchestator()