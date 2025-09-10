import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def log_request(request):
    logger.info(f"Request: {request.method} {request.url}")