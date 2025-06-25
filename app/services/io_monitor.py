import psutil
from prometheus_client import Gauge

disk_usage_percent = Gauge("disk_usage_percent", "Uso de disco en porcentaje")

def get_disk_usage():
    disk = psutil.disk_usage('/')
    disk_usage_percent.set(disk.percent)
    return {"total": disk.total, "used": disk.used, "percent": disk.percent}