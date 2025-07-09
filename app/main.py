from fastapi import FastAPI
from prometheus_client import start_http_server
from app.routes import metrics, profiling, system
from app.services import cpu_monitor, memory_monitor, io_monitor, system_monitor
import threading
import time

app = FastAPI(title="Performance API")

app.include_router(metrics.router)
app.include_router(profiling.router)
app.include_router(system.router)

# Iniciar Prometheus exporter
start_http_server(8001)

# Hilo para actualizar métricas cada 5 segundos
def actualizar_metricas():
    while True:
        cpu_monitor.get_cpu_percent()
        memory_monitor.get_memory_usage()
        io_monitor.get_disk_usage()
        system_monitor.update_system_metrics() 
        time.sleep(5)

threading.Thread(target=actualizar_metricas, daemon=True).start()
