from fastapi import FastAPI, UploadFile, File, HTTPException
from app.api.v1.schemas import ClassificationResponse, ErrorResponse
from app.models.classifier import classifier
from app.core.config import settings
from app.core.logging import setup_logging
from loguru import logger
from contextlib import asynccontextmanager
import uvicorn
import time

# Initialize Logging
setup_logging()

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup logic
    logger.info(f"Starting {settings.PROJECT_NAME} version {settings.VERSION}...")
    yield
    # Shutdown logic (if any)
    logger.info("Shutting down...")

app = FastAPI(
    title=settings.PROJECT_NAME,
    version=settings.VERSION,
    description="A high-performance microservice for image classification.",
    lifespan=lifespan
)

@app.get("/")
async def root():
    """
    Health check endpoint.
    """
    logger.debug("Health check hit")
    return {
        "status": "healthy", 
        "project": settings.PROJECT_NAME,
        "version": settings.VERSION,
        "model_version": classifier.model_version
    }

@app.post("/predict", response_model=ClassificationResponse, responses={400: {"model": ErrorResponse}})
async def predict(file: UploadFile = File(...)):
    """
    Image classification endpoint.
    """
    logger.info(f"Received prediction request for file: {file.filename}")
    
    if not file.content_type.startswith("image/"):
        logger.warning(f"Invalid file type: {file.content_type}")
        raise HTTPException(status_code=400, detail="Uploaded file is not an image.")
    
    try:
        start_time = time.perf_counter()
        contents = await file.read()
        results, model_latency = await classifier.predict(contents, top_k=settings.TOP_K)
        
        total_latency = (time.perf_counter() - start_time) * 1000
        
        logger.info(f"Prediction successful for {file.filename}. Model Latency: {model_latency:.2f}ms, Total Latency: {total_latency:.2f}ms")
        
        return ClassificationResponse(
            results=results,
            latency_ms=model_latency,
            model_version=classifier.model_version
        )
    except Exception as e:
        logger.exception(f"Unexpected error during prediction for {file.filename}: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    uvicorn.run(
        "app.main:app", 
        host=settings.HOST, 
        port=settings.PORT, 
        reload=settings.DEBUG
    )
