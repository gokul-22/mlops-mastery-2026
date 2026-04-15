import pytest
from fastapi.testclient import TestClient
from io import BytesIO
from PIL import Image
from app.main import app

client = TestClient(app)

def create_test_image():
    """Generates a small RGB image for testing."""
    file = BytesIO()
    image = Image.new("RGB", (224, 224), color="red")
    image.save(file, "jpeg")
    file.seek(0)
    return file

def test_read_root():
    """Tests the health check endpoint."""
    response = client.get("/")
    assert response.status_code == 200
    assert response.json()["status"] == "healthy"

def test_predict_success():
    """Tests a successful image prediction."""
    image_file = create_test_image()
    files = {"file": ("test.jpg", image_file, "image/jpeg")}
    
    response = client.post("/predict", files=files)
    
    assert response.status_code == 200
    data = response.json()
    assert "results" in data
    assert "latency_ms" in data
    assert len(data["results"]) > 0
    # Verify the first result has a label and confidence
    assert "label" in data["results"][0]
    assert isinstance(data["results"][0]["confidence"], float)

def test_predict_invalid_file():
    """Tests uploading a non-image file."""
    files = {"file": ("test.txt", BytesIO(b"not an image"), "text/plain")}
    
    response = client.post("/predict", files=files)
    
    assert response.status_code == 400
    assert "detail" in response.json()
