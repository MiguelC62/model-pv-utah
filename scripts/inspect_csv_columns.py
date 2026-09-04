from pathlib import Path
import pandas as pd

# ============================================================
# Configuración de Rutas
# ============================================================

# Archivo CSV original (grande)
CSV_PATH = Path(
    r"D:\Miguel\Documentos\R-Programs\PV_Utah\resultados\SMN\minuto\batches\SMN_total_batch_01_de_10_full_sapm.csv"
)

# Nuevo archivo CSV más pequeño (se guardará en la misma carpeta)
OUTPUT_PATH = CSV_PATH.parent / "pv_input_test.csv"


# ============================================================
# Lista de Columnas a Extraer
# ============================================================

COLUMNAS_A_EXTRAER = [
    "Tm",
    "FECHA",
    "HORA",
    "MINUTO",
    "LUGAR",
    "latitud",
    "longitud",
    "elevacion",
    "Ta",
    "wind_speed",
    "TL",
    "Albedo_MODIS",
    "superficie",
    "s",
    "azimuth_superficie",
    "Gc_BRL",
]


# ============================================================
# Proceso de Extracción
# ============================================================

print("\n" + "=" * 70)
print("PROCESO DE EXTRACCIÓN DE COLUMNAS")
print("=" * 70)

print(f"\nArchivo de origen:\n{CSV_PATH}")

if not CSV_PATH.exists():
    print("\nERROR: No se encontró el archivo de origen.")
    print("Revisa la ruta indicada en CSV_PATH.")
    raise SystemExit(1)

try:
    print("\nLeyendo y filtrando el archivo original (esto puede tomar un momento)...")

    # 'usecols' permite cargar ÚNICAMENTE las columnas deseadas para ahorrar memoria
    df_filtrado = pd.read_csv(CSV_PATH, usecols=COLUMNAS_A_EXTRAER)

    # Reordenar las columnas para que queden exactamente en el orden de tu lista
    df_filtrado = df_filtrado[COLUMNAS_A_EXTRAER]

    print(f"Columnas cargadas correctamente. Total de filas: {len(df_filtrado):,}")

    print(f"\nGuardando el archivo nuevo en:\n{OUTPUT_PATH}")

    # Guardar el nuevo archivo sin el índice de pandas
    df_filtrado.to_csv(OUTPUT_PATH, index=False)

    print("\n¡Extracción completada con éxito!")

except KeyError as e:
    print(f"\nERROR: Una o más columnas no se encontraron en el archivo original.")
    print(f"Detalle del error: Falta la columna {e}")
    print("\nPor favor, verifica que los nombres coincidan exactamente (mayúsculas/minúsculas).")

except Exception as e:
    print(f"\nOcurrió un error inesperado: {e}")

print("\n" + "=" * 70)
print("FIN DEL PROGRAMA")
print("=" * 70)
