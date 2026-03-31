# NSFW Image Detection API

An end-to-end API to detect NSFW content in images using the
Falconsai/nsfw_image_detection model from Hugging Face.

# Tech Stack
- Python 3.10
- FastAPI
- Hugging Face Transformers
- MongoDB
- PyTorch

# Project Structure
```
nsfw-detection-api/
├── main.py
├── model.py
├── database.py
├── requirements.txt
├── .env
└── README.md
```

# Setup Instructions

# 1. Clone the Repository
```bash
git clone <your-repo-url>
cd nsfw-detection-api
```

# 2. Create Virtual Environment
```bash
python -m venv venv
venv\Scripts\activate
```

# 3. Install Dependencies
```bash
pip install -r requirements.txt
```

# 4. MongoDB Setup
- Install MongoDB from https://www.mongodb.com/try/download/community
- Start MongoDB:
```bash
mongod --dbpath "C:\data\db"
```

# 5. Configure Environment
Create a `.env` file:
```env
DB_URL=mongodb://localhost:27017
DB_NAME=nsfw_logs
```

# 6. Run the API
```bash
uvicorn main:app --reload
```

# How to Use

Visit: http://127.0.0.1:8000/docs

Or use curl:
```bash
curl -X POST "http://127.0.0.1:8000/nsfw-detect" \
  -H "accept: application/json" \
  -F "file=@your_image.jpg"
```

# Example Response
```json
{
  "success": true,
  "message": "Detection completed",
  "data": {
    "nsfw_detected": false,
    "confidence": 0.15
  }
}
```
# Detection Rule
- If NSFW confidence > 60% → `nsfw_detected: true`
- If NSFW confidence ≤ 60% → `nsfw_detected: false`

# MongoDB Logs
Each request is logged with:
- Unique request ID
- Timestamp
- NSFW detection result
- Confidence score