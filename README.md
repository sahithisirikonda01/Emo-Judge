\# EmoJudge ⚖️🧠



\## AI-Powered Emotion Analysis Platform for Legal Testimonies



EmoJudge is a web-based AI application developed to assist attorneys in analyzing witness testimonies using facial emotion recognition and voice activity detection.



The system uses Artificial Intelligence, Computer Vision, and Deep Learning techniques to identify emotions such as Happy, Sad, Angry, Fear, Surprise, Disgust, and Neutral from witness testimony videos.



\---



\# 🚀 Features



\- Facial Emotion Detection using DeepFace

\- Face Detection using OpenCV Haarcascade

\- Voice Activity Monitoring

\- Secure Login \& Authentication

\- Video Upload and Analysis

\- Interactive Dashboard and Emotion Timeline

\- Sample Witness Video Library



\---



\# 🛠️ Technologies Used



\## Frontend

\- React.js

\- HTML

\- CSS

\- JavaScript



\## Backend

\- Python

\- FastAPI / Flask

\- OpenCV

\- DeepFace

\- TensorFlow



\## Database

\- MongoDB / SQLite



\## AI \& Computer Vision

\- CNN Models

\- DeepFace Emotion Recognition

\- Haarcascade Face Detection

\- Voice Activity Detection



\---



\# 📂 Project Structure



```text

EmoJudge/

├── backend/

├── frontend/

├── sample\_videos/

└── README.md

```



\---



\# ▶️ How to Run the Project



\## 1️⃣ Clone the Repository



```bash

git clone <your-repository-link>

cd EmoJudge

```



\---



\## 2️⃣ Create Virtual Environment



```powershell

python -m venv venv

.\\venv\\Scripts\\Activate.ps1

```



\---



\## 3️⃣ Install Dependencies



\### Backend Dependencies



```powershell

pip install -r requirements.txt

```



\### Frontend Dependencies



```powershell

npm install

```



\---



\## 4️⃣ Start MongoDB



Check MongoDB status:



```powershell

Get-Service MongoDB

```



If MongoDB is not running:



```powershell

Start-Service MongoDB

```



\---



\## 5️⃣ Start Backend Server



```powershell

python start\_backend.py

```



Backend runs on:



```text

http://localhost:8000

```



API Documentation:



```text

http://localhost:8000/docs

```



\---



\## 6️⃣ Start Frontend



Open another terminal and run:



```powershell

.\\start\_frontend.bat

```



Frontend runs on:



```text

http://localhost:3000

```



\---



\# 🌐 Application Workflow



1\. User logs into the platform

2\. Uploads or selects a witness testimony video

3\. Video frames are extracted using OpenCV

4\. Faces are detected using Haarcascade

5\. DeepFace analyzes emotions from each frame

6\. Audio is analyzed for speech activity

7\. Results are displayed on the dashboard with emotion timelines and insights



\---



\# 🎯 Objectives



\- Detect emotions from witness testimony videos

\- Assist attorneys with objective emotional insights

\- Improve legal decision-making

\- Reduce emotional bias in judicial analysis



\---



\# 🧠 AI Techniques Used



\- Convolutional Neural Networks (CNN)

\- DeepFace Emotion Analysis

\- OpenCV Video Processing

\- Haarcascade Face Detection

\- Voice Activity Detection



\---



\# 👨‍⚖️ Use Case



Attorneys can upload or select witness videos and receive:

\- Emotion analysis

\- Speech activity insights

\- Emotion timelines

\- Legal guidance suggestions



\---



\# 🔮 Future Enhancements



\- Real-time courtroom monitoring

\- Speech-to-text transcription

\- AI-generated legal reports

\- Advanced stress detection

\- Cloud deployment support



\---



\# 📌 Developed For



AI-assisted legal testimony analysis and emotion recognition research.



\---



\# 👩‍💻 Author



Developed as a Mini Project on Artificial Intelligence and Web Technologies.

