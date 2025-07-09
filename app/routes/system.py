from fastapi import APIRouter
from app.services import system_monitor

router = APIRouter(prefix="/metrics/system", tags=["System"])

@router.get("/")
def get_system_metrics():
	return {
		"uptime": system_monitor.get_system_info(),
		"threads": system_monitor.get_thread_count(),
		"processes": system_monitor.get_system_info()["process_count"]
	}

@router.get("/network")
def get_network_metrics():
	return system_monitor.get_network_info()