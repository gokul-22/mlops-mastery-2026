from fastapi import FastAPI, UploadFile, File, HTTPException
from app.api.v1.schemas import ClassificationResponse, ErrorResponse
from app.models.classifier import classifier
from app.core.config import settings
import uvicorn

app = FastAPI(
    title=settings.PROJECT_NAME,
    version=settings.VERSION,
    description="A high-performance microservice for image classification."
)

@app.get("/")
async def root():
    """
    Health check endpoint.
    """
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
    if not file.content_type.startswith("image/"):
        raise HTTPException(status_code=400, detail="Uploaded file is not an image.")
    
    try:
        contents = await file.read()
        results, latency = await classifier.predict(contents, top_k=settings.TOP_K)
        
        return ClassificationResponse(
            results=results,
            latency_ms=latency,
            model_version=classifier.model_version
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    uvicorn.run(
        "app.main:app", 
        host=settings.HOST, 
        port=settings.PORT, 
        reload=settings.DEBUG
    )
