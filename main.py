from fastapi import FastAPI, File, UploadFile, HTTPException
from database import save_log
from model import detect_nsfw
from datetime import datetime, timezone
import uuid

app = FastAPI(title="NSFW Image Detection API")

@app.post("/nsfw-detect")
async def nsfw_detect(file: UploadFile = File(...)):
    
    if not file.content_type.startswith("image/"):
        raise HTTPException(status_code=400, detail="Only image files are accepted.")

    try:
        image_bytes = await file.read()
        result = detect_nsfw(image_bytes)

        # Save log to MongoDB
        log_entry = {
            "request_id": str(uuid.uuid4()),
            "timestamp": datetime.now(timezone.utc).isoformat(),
            "nsfw_detected": result["nsfw_detected"],
            "confidence": result["confidence"]
        }
        save_log(log_entry)

        return {
            "success": True,
            "message": "Detection completed",
            "data": {
                "nsfw_detected": result["nsfw_detected"],
                "confidence": result["confidence"]
            }
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))