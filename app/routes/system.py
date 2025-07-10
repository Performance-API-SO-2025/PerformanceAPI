from fastapi import APIRouter, HTTPException
from app.services import system_monitor
import logging

router = APIRouter(prefix="/metrics/system", tags=["System"])

# Endpoint para obtener métricas generales del sistema operativo.
@router.get("/")
def get_system_metrics():
    try:
         # Obtiene información del sistema
        uptime = system_monitor.get_system_info()
        # Obtiene el número de hilos activos
        threads = system_monitor.get_thread_count()
        processes = uptime["process_count"]  # Reutiliza lo ya consultado
        # Devuelve un JSON con las métricas principales del sistema.
        return {
            "uptime": uptime,
            "threads": threads,
            "processes": processes
        }
    except Exception as e:
        logging.error(f"Error en GET /metrics/system/: {e}")
        raise HTTPException(status_code=500, detail="No se pudo obtener métricas del sistema")
# Endpoint para obtener métricas de red
@router.get("/network")
def get_network_metrics():
    try:
        # Llama a la función que devuelve información de red en formato JSON.
        return system_monitor.get_network_info()
    except Exception as e:
        logging.error(f"Error en GET /metrics/system/network: {e}")
        raise HTTPException(status_code=500, detail="No se pudo obtener métricas de red")
