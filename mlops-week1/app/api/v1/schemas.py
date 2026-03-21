from pydantic import BaseModel, Field
from typing import List, Optional

class ClassificationResult(BaseModel):
    label: str = Field(..., description="The predicted class label")
    confidence: float = Field(..., ge=0.0, le=1.0, description="The confidence score of the prediction")

class ClassificationResponse(BaseModel):
    results: List[ClassificationResult]
    latency_ms: float = Field(..., description="Inference latency in milliseconds")
    model_version: str = Field(..., description="Version of the model used")

class ErrorResponse(BaseModel):
    error: str
    detail: Optional[str] = None
