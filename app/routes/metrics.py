from fastapi import APIRouter
from app.services import cpu_monitor, memory_monitor, io_monitor

router = APIRouter(prefix="/metrics", tags=["Metrics"])

@router.get("/cpu")
def get_cpu():
    return {"cpu_percent": cpu_monitor.get_cpu_percent()}

@router.get("/memory")
def get_memory():
    return memory_monitor.get_memory_usage()

@router.get("/disk")
def get_disk():
    return io_monitor.get_disk_usage()
