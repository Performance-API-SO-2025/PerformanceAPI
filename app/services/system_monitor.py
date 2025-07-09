import psutil
from prometheus_client import Gauge, Counter

process_count = Gauge("system_process_count", "Número de procesos activos")
thread_count = Gauge("system_thread_count", "Número de hilos activos")
uptime_seconds = Gauge("system_uptime_seconds", "Tiempo desde el último arranque (segundos)")
net_bytes_sent = Counter("network_bytes_sent_total", "Bytes enviados desde el arranque")
net_bytes_recv = Counter("network_bytes_received_total", "Bytes recibidos desde el arranque")

def update_system_metrics():
    # Número de procesos activos
    process_count.set(len(psutil.pids()))

    # Número de hilos activos (suma de todos los procesos)
    total_threads = 0
    for pid in psutil.pids():
        try:
            p = psutil.Process(pid)
            total_threads += p.num_threads()
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            continue
    thread_count.set(total_threads)

    # Uptime (tiempo desde el boot)
    uptime = psutil.boot_time()
    current = psutil.time.time()
    uptime_seconds.set(current - uptime)

    # Red
    net_io = psutil.net_io_counters()
    net_bytes_sent.inc(net_io.bytes_sent)
    net_bytes_recv.inc(net_io.bytes_recv)

    def get_system_info():
        import time
        return {
            "process_count": len(psutil.pids()),
            "uptime_seconds": time.time() - psutil.boot_time()
        }
    
    def get_network_info():
        io = psutil.net_io_counters()
        return {
            "bytes_sent": io.bytes_sent,
            "bytes_received": io.bytes_recv
        }
    
    def get_thread_count():
        count = 0
        for pid in psutil.pids():
            try:
                count += psutil.Process(pid).num_threads()
            except (psutil.NoSuchProcess, psutil.AccessDenied):
                continue
        return count