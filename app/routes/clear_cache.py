# from flask import current_app
from flask_api import status
from resources.cache import cache


def clear_cache():
    try:
        cache.clear()
        return {"status": "success", "message": "Cache cleared."}, status.HTTP_200_OK
    except:
        return {
            "status": "error",
            "message": "Error clearing cache.",
        }, status.HTTP_500_INTERNAL_SERVER_ERROR
