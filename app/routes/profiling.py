from fastapi import APIRouter, HTTPException
from app.services import profiler
import logging

router = APIRouter(prefix="/profiling", tags=["Profiling"])

# Define un endpoint GET en '/profiling/function' que ejecuta un perfilado de una función de ejemplo.
@router.get("/function")
def profile_function():
    try:
        # Llama a la función 'profile_sample_function' del módulo profiler
        return profiler.profile_sample_function()
    except Exception as e:
        logging.error(f"Error al perfilar función: {e}")
        raise HTTPException(status_code=500, detail="Error durante el perfilado de la función")
