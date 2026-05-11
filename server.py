import cv2
import uvicorn
import numpy as np
import mediapipe as mp
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from deepface import DeepFace

app = FastAPI()

# Enable CORS (Modify for production security)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Change to allowed domains in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Initialize MediaPipe Face Detection
mp_face_detection = mp.solutions.face_detection
face_detection = mp_face_detection.FaceDetection(min_detection_confidence=0.5)

# Emotion-based advice
ADVICE_MAP = {
    "angry": "The witness may be defensive. Consider calming them with neutral questions.",
    "disgust": "The witness may feel uncomfortable. Reframe questions to ease tension.",
    "fear": "The witness is nervous. Use a gentle approach to gain trust.",
    #"happy": "The witness seems cooperative. Continue in the current direction.",
    "sad": "The witness may be distressed. Show empathy and slow down questioning.",
    "surprise": "Unexpected reaction! Ask follow-ups to clarify their stance.",
    "neutral": "The witness is composed. Maintain the current questioning tone.",
}

# Request Model
class EmotionRequest(BaseModel):
    video_path: str
    time: float

@app.post("/analyze_emotion/")
async def analyze_emotion(request: EmotionRequest):
    video_path = request.video_path
    analysis_time = request.time

    # Load video
    cap = cv2.VideoCapture(video_path)
    if not cap.isOpened():
        raise HTTPException(status_code=400, detail="Error: Cannot open video")

    # Move to specific timestamp
    cap.set(cv2.CAP_PROP_POS_MSEC, analysis_time * 1000)
    ret, frame = cap.read()
    if not ret:
        raise HTTPException(status_code=400, detail="Error: Cannot read frame at given time")

    # Convert to RGB for MediaPipe
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = face_detection.process(frame_rgb)

    if not results.detections:
        return {"error": "No face detected"}

    try:
        # Analyze emotion using DeepFace
        analysis = DeepFace.analyze(frame_rgb, actions=['emotion'], enforce_detection=False)
        if isinstance(analysis, list) and len(analysis) > 0:
            detected_emotion = analysis[0]['dominant_emotion']
            advice = ADVICE_MAP.get(detected_emotion, "No specific advice available.")
            return {
                "video": video_path,
                "time": analysis_time,
                "detected_emotion": detected_emotion,
                "advice": advice
            }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"DeepFace analysis failed: {str(e)}")

    return {"error": "No emotion detected"}

# Run the server
if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
