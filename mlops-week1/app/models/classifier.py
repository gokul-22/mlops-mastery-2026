import torch
import torchvision.models as models
import torchvision.transforms as transforms
from PIL import Image
import io
import time
from typing import List, Tuple
from app.api.v1.schemas import ClassificationResult
from app.core.config import settings

class ImageClassifier:
    """
    Image Classification Model Wrapper using PyTorch.
    Handles loading, preprocessing, and inference.
    """
    def __init__(self):
        # 1. Configuration
        self.model_name = settings.MODEL_NAME
        self.model_version = f"{self.model_name}_v1.0.0"
        
        # 2. Hardware Selection (CPU vs GPU)
        self.device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
        
        # 3. Model Initialization
        # We load a pre-trained MobileNetV3 model from torchvision
        self.model = models.mobilenet_v3_small(weights=models.MobileNet_V3_Small_Weights.DEFAULT)
        self.model.eval()  # Set to evaluation mode (turns off Dropout/BatchNorm)
        self.model.to(self.device)
        
        # 4. Image Preprocessing Pipeline
        self.transform = transforms.Compose([
            transforms.Resize(256),
            transforms.CenterCrop(224),
            transforms.ToTensor(),
            transforms.Normalize(
                mean=[0.485, 0.456, 0.406], 
                std=[0.229, 0.224, 0.225]
            ),
        ])
        
        # 5. Label Mapping (ImageNet 1000 classes)
        self.categories = [f"Class_{i}" for i in range(1000)]

    async def predict(
        self, 
        image_bytes: bytes, 
        top_k: int = 3
    ) -> Tuple[List[ClassificationResult], float]:
        """
        Runs the inference pipeline on raw image bytes.
        """
        # Start timer for latency tracking
        start_time = time.perf_counter()
        
        # 1. Convert bytes to Image and preprocess
        image = Image.open(io.BytesIO(image_bytes)).convert("RGB")
        input_tensor = self.transform(image).unsqueeze(0).to(self.device)
        
        # 2. Inference (No Gradient calculation needed for speed)
        with torch.no_grad():
            outputs = self.model(input_tensor)
            # Convert raw scores (logits) to probabilities
            probabilities = torch.nn.functional.softmax(outputs[0], dim=0)
            
        # 3. Post-processing: Extract top K results
        top_probs, top_indices = torch.topk(probabilities, top_k)
        
        results = [
            ClassificationResult(
                label=self.categories[idx], 
                confidence=prob.item()
            )
            for prob, idx in zip(top_probs, top_indices)
        ]
        
        # Calculate latency in milliseconds
        latency = (time.perf_counter() - start_time) * 1000
        return results, latency

# Global instance for re-use (Singleton Pattern)
classifier = ImageClassifier()
