from fastapi import APIRouter
from app.services import profiler

router = APIRouter(prefix="/profiling", tags=["Profiling"])

@router.get("/function")
def profile_function():
    return profiler.profile_sample_function()
