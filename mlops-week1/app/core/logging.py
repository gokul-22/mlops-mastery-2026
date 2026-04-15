import sys
from loguru import logger
from app.core.config import settings

def setup_logging():
    """
    Configures Loguru for structured logging.
    - JSON format for production (if desired)
    - Console output with colors for development
    """
    # Remove default handler
    logger.remove()
    
    # Add a new handler with specific formatting
    logger.add(
        sys.stderr,
        format="<green>{time:YYYY-MM-DD HH:mm:ss}</green> | <level>{level: <8}</level> | <cyan>{name}</cyan>:<cyan>{function}</cyan>:<cyan>{line}</cyan> - <level>{message}</level>",
        level="DEBUG" if settings.DEBUG else "INFO",
        colorize=True
    )
    
    # Optional: Add a file handler
    logger.add(
        "logs/app.log",
        rotation="10 MB",
        retention="10 days",
        level="INFO",
        compression="zip"
    )

    return logger
