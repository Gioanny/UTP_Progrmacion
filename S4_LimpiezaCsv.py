# limpiar_csv_simple.py
# Objetivo: leer CSV "sucio", limpiar y guardar "limpio" con:
#- timestamp en formato ISO YYYY-MM-DDTHH:MM:SS
#- value como float con punto y 3 decimales
#- separador de salida: coma
#- filas inválidas: se saltan

#para lectura de varios archivos se usa el For y tambien el comando *.csv

import csv
from datetime import datetime
from pathlib import Path

#Path - ruta de acceso
ROOT = Path(__file__).resolve().parents[0] #raiz del proyecto
TXT = ROOT / "archivos" 
IN_FILE=TXT  /"voltajes_250_sucio.csv" #archivos de ingreso
OUT_FILE=TXT /"Voltajes_250_limpio.csv" #archivos de salida
#apertura de archivos
with open(IN_FILE, 'r', encoding="utf-8",newline="") as fin, \
    open(OUT_FILE, 'w', encoding="utf-8",newline="") as fout:
    reader = csv.DictReader(fin, delimiter=';') #usa ',' si tu archivo lo requiere
    writer = csv.DictWriter(fout, fieldnames=["timestamp","value"]) #crea el archivo y su cabera
    writer.writeheader()
#leer linea por lineal y seleccionar en crudo raw
    total = kept = 0
    for row in reader:
        total += 1
        ts_raw    = (row.get("timestamp") or "").strip()
        val_raw = (row.get("value") or "").strip()
        print(ts_raw, val_raw)
#limpiar datos
        val_raw = val_raw.replace(",", ".")
        val_low = val_raw.lower()
        if val_low in {"", "na", "n/a", "nan", "null", "none", "error"}:
            continue  # saltar fila
        try:
            val = float(val_raw)
        except ValueError:
            continue  # saltar fila si no es número
#limpieza de datos de tiempo
        ts_clean = None
        for fmt in ("%Y-%m-%dT%H:%M:%S", "%d/%m/%Y %H:%M:%S"):
            try:
                dt = datetime.strptime(ts_raw, fmt)
                ts_clean = dt.strftime("%Y-%m-%dT%H:%M:%S")
                break
            except ValueError:
                pass
#milisegundo (opcional)
        if ts_clean is None and "T" in ts_raw and len(ts_raw) >= 19:
            try:
                dt = datetime.strptime(ts_raw[:19], "%Y-%m-%dT%H:%M:%S")
                ts_clean = dt.strftime("%Y-%m-%dT%H:%M:%S")
            except ValueError:
                ts_clean = None

        if ts_clean is None:
            continue  # saltar fila si no pudimos interpretar la fecha

#grabar datos en writer
        writer.writerow({"timestamp": ts_clean, "value": f"{val:.2f}"})
        kept += 1 #sume 1 kept, en nuestro caso cambia de fila