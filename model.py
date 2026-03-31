from transformers import pipeline
from PIL import Image
import io


classifier = pipeline("image-classification", model="Falconsai/nsfw_image_detection")

def detect_nsfw(image_bytes: bytes) -> dict:
    image = Image.open(io.BytesIO(image_bytes)).convert("RGB")
    results = classifier(image)

    # finding nsfw score
    nsfw_score = 0.0
    for result in results:
        if result["label"].upper() == "NSFW":
            nsfw_score = result["score"] * 100
            break

    nsfw_detected = nsfw_score > 60.0

    return {
        "nsfw_detected": nsfw_detected,
        "confidence": round(nsfw_score, 2)
    }