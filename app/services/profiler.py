import cProfile
import pstats
import io

def profile_sample_function():
    def some_heavy_function():
        total = 0
        for i in range(1000000):
            total += i * i
        return total

    profiler = cProfile.Profile()
    profiler.enable()
    some_heavy_function()
    profiler.disable()

    s = io.StringIO()
    ps = pstats.Stats(profiler, stream=s).sort_stats('cumulative')
    ps.print_stats(10)
    return {"profile": s.getvalue()}
