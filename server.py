from flask import Flask, render_template, request, jsonify
from EmotionDetection import emotion_detector
app = Flask(__name__)
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/emotionDetector', methods=['POST'])
def emotion_detector_route():
    if request.method == 'POST':
        text_to_analyze = request.form.get('text')
        if text_to_analyze:
            emotio_scores = emotion_detector(text_to_analyze)