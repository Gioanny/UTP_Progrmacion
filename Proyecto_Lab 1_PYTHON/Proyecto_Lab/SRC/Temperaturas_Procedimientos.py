import csv
from datetime import datetime

def limpiar_datos(input_file, output_file):
    filas_totales = 0
    filas_validas = 0
    descartes_timestamp = 0
    descartes_valor = 0
    temp_list = []
    resultados = []

    with open(input_file, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile, delimiter=';')
        for row in reader:
            filas_totales += 1
            ts = row.get('timestamp', '').strip()
            val = row.get('value', '').strip()

            # Limpiar valor
            val = val.replace(',', '.').replace(' ', '')  # normaliza decimales
            try:
                voltaje = float(val)
            except:
                descartes_valor += 1
                continue

            # Limpiar timestamp
            fecha_valida = None
            formatos = ["%Y-%m-%dT%H:%M:%S", "%d/%m/%Y %H:%M"]
            for fmt in formatos:
                try:
                    fecha_valida = datetime.strptime(ts, fmt)
                    break
                except:
                    continue
            if not fecha_valida:
                descartes_timestamp += 1
                continue

            # Convertir a temperatura
            temp_c = round(18*voltaje - 64, 2)
            temp_list.append(temp_c)

            # Generar alerta
            alerta = "ALERTA" if temp_c > 40 else "OK"

            resultados.append({
                "Timestamp": fecha_valida.strftime("%Y-%m-%d %H:%M:%S"),
                "Voltaje": round(voltaje, 6),
                "Temp_C": temp_c,
                "Alertas": alerta
            })
            filas_validas += 1

    # Guardar CSV procesado
    with open(output_file, 'w', newline='', encoding='utf-8') as outcsv:
        writer = csv.DictWriter(outcsv, fieldnames=["Timestamp","Voltaje","Temp_C","Alertas"])
        writer.writeheader()
        writer.writerows(resultados)

    # Calcular KPIs
    temp_min = round(min(temp_list),2) if temp_list else 0
    temp_max = round(max(temp_list),2) if temp_list else 0
    temp_prom = round(sum(temp_list)/len(temp_list),2) if temp_list else 0
    total_alertas = sum(1 for t in resultados if t["Alertas"]=="ALERTA")

    KPIs = {
        "Filas_totales": filas_totales,
        "Filas_validas": filas_validas,
        "Descartes_Timestamp": descartes_timestamp,
        "Descartes_valor": descartes_valor,
        "Temp_min": temp_min,
        "Temp_max": temp_max,
        "Temp_prom": temp_prom,
        "Total_alertas": total_alertas
    }

    return KPIs

