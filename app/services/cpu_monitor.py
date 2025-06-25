import psutil
from prometheus_client import Gauge

# Crear la métrica
cpu_usage_percent = Gauge("cpu_usage_percent", "Uso de CPU en porcentaje")

def get_cpu_percent():
    value = psutil.cpu_percent(interval=1)
    cpu_usage_percent.set(value)  # Actualiza métrica para Prometheus
    return value