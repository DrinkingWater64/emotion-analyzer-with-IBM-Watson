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
        emotion_data = emotion_detector(text_to_analyze)  # Call your function
        if emotion_data:
            dominant_emotion, emotion_scores = emotion_data  # Unpack the tuple
            # Format the output as requested JSON
            output_json = {
                "anger": emotion_scores.get('anger', 0.0),
                "disgust": emotion_scores.get('disgust', 0.0),
                "fear": emotion_scores.get('fear', 0.0),
                "joy": emotion_scores.get('joy', 0.0),
                "sadness": emotion_scores.get('sadness', 0.0),
                "dominant_emotion": dominant_emotion
            }
            return jsonify(output_json)
        else:
            return jsonify({"error": "No emotion detected. Please try again!"}), 400  # Return JSON error

    except Exception as e:
        # Handle potential errors during emotion detection
        error_message = f"Error processing text: {e}"
        print(error_message)  # Log the error for debugging
        return jsonify({"error": error_message}), 500  # Return JSON error

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)