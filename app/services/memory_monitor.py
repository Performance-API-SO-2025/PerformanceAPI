import psutil
from prometheus_client import Gauge

memory_usage_percent = Gauge("memory_usage_percent", "Uso de memoria RAM en porcentaje")

def get_memory_usage():
    mem = psutil.virtual_memory()
    memory_usage_percent.set(mem.percent)
    return {"total": mem.total, "used": mem.used, "percent": mem.percent}