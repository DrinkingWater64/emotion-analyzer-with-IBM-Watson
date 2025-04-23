from flask import Flask, render_template, request, jsonify
from EmotionDetection import emotion_detector
app = Flask(__name__)
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/emotionDetector', methods=['POST', 'GET'])
def emotion_detection_route():
    """
    Handles the emotion detection request.
    It expects a POST or GET request with text to analyze.
    It calls the emotion_detector function and returns the result.
    """
    if request.method == 'POST':
        text_to_analyze = request.form['text']  # Get text from the form
    elif request.method == 'GET':
        text_to_analyze = request.args.get('text')
    else:
        return render_template('result.html', analysis_result="Invalid request method. Please use POST or GET.")

    try:
        emotion_data = emotion_detector(text_to_analyze)  # Call your function
        if emotion_data:
            dominant_emotion, emotion_scores = emotion_data  # Unpack the tuple
            # Format the output as requested
            output_string = f"For the given statement, the system response is 'anger': {emotion_scores.get('anger', 0.0):.7f}, 'disgust': {emotion_scores.get('disgust', 0.0):.7f}, 'fear': {emotion_scores.get('fear', 0.0):.7f}, 'joy': {emotion_scores.get('joy', 0.0):.7f} and 'sadness': {emotion_scores.get('sadness', 0.0):.7f}. The dominant emotion is <b>{dominant_emotion}</b>."
            return render_template('result.html', analysis_result=output_string)
        else:
            return render_template('result.html', analysis_result="No emotion detected. Please try again!")
    except Exception as e:
        # Handle potential errors during emotion detection
        error_message = f"Error processing text: {e}"
        print(error_message)  # Log the error for debugging
        return render_template('result.html', analysis_result=error_message)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)