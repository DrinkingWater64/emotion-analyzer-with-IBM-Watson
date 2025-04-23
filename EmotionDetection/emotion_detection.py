import requests
import json


empty_response = {"anger": None, "disgust": None, "fear": None, "joy": None, "sadness": None}
def emotion_detector(text_to_analyse):
    """
    Detects the emotion of a text
    :param text_to_analyse:
    :return: The 'text' attribute of the response object, or None if an error occurs.
    """
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    input_json = {"raw_document": {"text": text_to_analyse}}
    if not text_to_analyse:  # Check for empty input
        return None, {"anger": None, "disgust": None, "fear": None, "joy": None, "sadness": None}
    try:
        response = requests.post(url, headers=headers, json=input_json)
        response.raise_for_status()  # Raise HTTPError for bad responses (4xx or 5xx)
        result = response.json()
        if 'emotionPredictions' in result and result['emotionPredictions']:
            emotion_scores = result['emotionPredictions'][0].get('emotion')
            if emotion_scores:
                dominant_emotion = max(emotion_scores, key=emotion_scores.get)
                return dominant_emotion, emotion_scores
        return None, empty_response
    except requests.exceptions.HTTPError as e:
        print(f"HTTPError: {e}")
        return None, empty_response
    except requests.exceptions.RequestException as e:
        print(f"RequestException: {e}")
        return None, empty_response
    except KeyError as e:
        print(f"KeyError: {e}")
        return None, empty_response
