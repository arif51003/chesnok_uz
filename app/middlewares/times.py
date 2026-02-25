# app/middlewares/timing.py
import time
import logging
from starlette.requests import Request

logger = logging.getLogger("request_timing")

async def timing_middleware(request: Request, call_next):
    start = time.perf_counter()
    try:
        response = await call_next(request)
        return response
    finally:
        elapsed = time.perf_counter() - start
        ms = elapsed * 1000

        method = request.method
        path = request.url.path
        status = getattr(locals().get("response", None), "status_code", "ERR")

        print(f"[TIMING] {method} {path} -> {status} | {elapsed:.6f}s ({ms:.2f}ms)")
       