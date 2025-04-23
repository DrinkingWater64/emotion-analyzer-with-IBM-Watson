"""Flask application for emotion detection."""

from flask import Flask, render_template, request, jsonify
from EmotionDetection import emotion_detector
app = Flask(__name__)

@app.route('/')
def index():
    """
    Renders the main page (index.html).
    """
    return render_template('index.html')

@app.route('/emotionDetector', methods=['POST', 'GET'])
@app.route('/emotionDetector', methods=['POST', 'GET'])
def emotion_detection_route():
    """
    Handles the emotion detection request.
    It expects a POST or GET request with text to analyze.
    It calls the emotion_detector function and returns the result as JSON.
    """
    if request.method == 'POST':
        text_to_analyze = request.form['text']  # Get text from the form
    elif request.method == 'GET':
        text_to_analyze = request.args.get('textToAnalyze')
    else:
        return jsonify({"error": "Invalid request method. Please use POST or GET."}), 400

    try:
        dominant_emotion, emotion_scores = emotion_detector(text_to_analyze)
        if dominant_emotion is None:
            return jsonify({"error": "Invalid text! Please try again!"}), 400

        output_json = {
            "anger": emotion_scores.get('anger', 0.0),
            "disgust": emotion_scores.get('disgust', 0.0),
            "fear": emotion_scores.get('fear', 0.0),
            "joy": emotion_scores.get('joy', 0.0),
            "sadness": emotion_scores.get('sadness', 0.0),
            "dominant_emotion": dominant_emotion
        }
        return jsonify(output_json)

    except Exception as e:
        error_message = f"Error processing text: {e}"
        print(error_message)
        return jsonify({"error": error_message}), 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
