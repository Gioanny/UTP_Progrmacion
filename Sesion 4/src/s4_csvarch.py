import csv
from datetime import datetime
from pathlib import Path #importo el comando path (busca el lugar del codigo)
from statistics import mean

#crear mis variables de rutas para ingreso de archivo y salida de archivo
ROOT=Path(__file__).resolve().parents[1]#busca el lugar donde esta guardado el codigo
#/USUARIO/Sesion4
IN_FILE=ROOT/"datos"/"raw"/"voltajes_250_sucio.csv" #ruta de ingreso
OUT_FILE=ROOT/"datos"/"proccesing"/"voltajes_250_sucio_limpio.csv" #ruta de salida

with open(IN_FILE,'r',encoding="utf-8", newline="") as fin, \
    open(OUT_FILE, "w", encoding="utf-8", newline="") as fout:
    reader=csv.DictReader(fin,delimiter=';')
    writer=csv.DictWriter(fout,fieldnames=["Tiempo","voltaje","control"])
    writer.writeheader()
#leer linea por lineal y seleccionar en crudo raw 
#control de KPIs
    total = kept = 0
    Voltaje=[]
    bad_ts = bad_val = 0 #valores malos
    for row in reader:
        total+=1
        ts_raw  = (row.get("timestamp") or "").strip() #toma todos los valores de la columna timestamp
        val_raw = (row.get("value") or "").strip() #toma todos los valores de la columna value
#limpiar datos
        val_raw = val_raw.replace(",", ".")
        val_low = val_raw.lower() #empezar a eliminar valores no existentes
        if val_low in {"", "na", "n/a", "nan", "null", "none", "error"}:
            bad_val += 1
            continue #salta el comando
        try:
            val = float(val_raw)
        except ValueError:
            bad_val += 1
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
            bad_ts += 1
            continue  # saltar fila si no pudimos interpretar la fecha
        
#sistema de control de voltaje - si V>= a 5 V entonces lanza una alerta
        control="CUIDADO" if val >= 5 else "OK" #compactos para condiciones simples
        Voltaje.append(val)
        
#grabar datos en writer
        writer.writerow({"Tiempo": ts_clean, "voltaje": f"{val:.2f}", "control":control})
        kept += 1 #sume 1 kept, en nuestro caso suma los valores que si sirven
        
#KPIs / DATOS
n=len(Voltaje)
if n==0:
    KPIs={"n":0,"min":None,"max":None,"prom":None,"alertas":0,"alertas_pct":0}
else:
    alertas=sum(v >= 5 for v in Voltaje) #conteo rapido de estructura repetitiva
    KPIs={
        'n': n,
        'min': min(Voltaje),
        "max": max(Voltaje),
        "prom":mean(Voltaje),
        "alerts": alertas,
        "alerts_pct": 100.0 * alertas / n,
    }
#KPIs / Calidad

descartes_totales = bad_ts + bad_val            # equivale a (total - kept) con esta lógica
pct_descartadas = (descartes_totales / total * 100.0) if total else 0.0 #condiciones simples
kpis_calidad = {
    "filas_totales": total,
    "filas_validas": kept,
    "descartes_timestamp": bad_ts,
    "descartes_valor": bad_val,
    "%descartadas": round(pct_descartadas, 2), # redondea a 2 decimales
}

# --- Salida/Verificación ---
print(f"Entrada:  {IN_FILE}")
print(f"Salida:   {OUT_FILE}")
print("\nKPIs de calidad:", kpis_calidad)
print("KPIs de voltaje:", {
    "n": KPIs["n"],
    "min": None if KPIs["min"] is None else round(KPIs["min"], 2),
    "max": None if KPIs["max"] is None else round(KPIs["max"], 2),
    "prom": None if KPIs["prom"] is None else round(KPIs["prom"], 2),
    "alerts": KPIs["alerts"],
    "alerts_pct": round(KPIs["alerts_pct"], 2),
})