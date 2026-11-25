import os
import rius
from functools import wraps
from dotenv import load_dotenv

load_dotenv()

_initialized = False


def init_tracing():
    global _initialized

    if _initialized:
        return

    api_key = os.getenv("RIUS_API_KEY")

    if not api_key:
        raise RuntimeError("RIUS_API_KEY missing")

    rius.init(
        api_key=api_key,
        service_name="enterprise-ai"
    )

    _initialized = True
    print("Rius initialized successfully")


def trace(name=None):
    """
    Reusable decorator for tracing functions.
    """

    def decorator(func):

        @wraps(func)
        @rius.observe(name=name or func.__name__)
        def wrapper(*args, **kwargs):
            return func(*args, **kwargs)

        return wrapper

    return decorator