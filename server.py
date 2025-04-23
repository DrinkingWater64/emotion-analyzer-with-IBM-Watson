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
            emotion_analysis = emotion_detector(text_to_analyze)
            if emotion_analysis:
                dominant_emotion, emotion_scores = emotion_analysis
                formatted_output = {
                    "anger": emotion_scores.get('anger', 0.0),
                    "disgust": emotion_scores.get('disgust', 0.0),
                    "fear": emotion_scores.get('fear', 0.0),
                    "joy": emotion_scores.get('joy', 0.0),
                    "sadness": emotion_scores.get('sadness', 0.0),
                    "dominant_emotion": dominant_emotion
                }
                response_text = (f"For the given statement, the system response is "
                                  f"'anger': {formatted_output['anger']:.7f}, "
                                 f"'disgust': {formatted_output['disgust']:.7f}, "
                                 f"'fear': {formatted_output['fear']:.7f}, "
                                 f"'joy': {formatted_output['joy']:.7f} and "
                                 f"'sadness': {formatted_output['sadness']:.7f}."
                                 f" The dominant emotion is {formatted_output['dominant_emotion']}.")

                return render_template('result.html', analysis_result=response_text)
            else:
                return render_template('result.html', analysis_result="Could not detect emotion.")
        else:
            return render_template('result.html', analysis_result="Please enter text to analyze.")
    else:
        return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)