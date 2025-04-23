import requests
import json

def emotion_detector(text_to_analyse):
    """
    Detects the emotion of a text
    :param text_to_analyse:
    :return: The 'text' attribute of the response object, or None if an error occurs.
    """
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    input_json = {"raw_document": {"text": text_to_analyse}}
    try:
        response = requests.post(url, headers=headers, json=input_json)
        response.raise_for_status()
        result = response.json()
        dominant_emotion = None
        if 'emotionPredictions' in result and result['emotionPredictions']:
            emotion_scores = result['emotionPredictions'][0].get('emotion')
            if emotion_scores:
                dominant_emotion = max(emotion_scores, key=emotion_scores.get)
        return dominant_emotion, emotion_scores

    except requests.exceptions.HTTPError as e:
        print(e)
        return None

    except requests.exceptions.RequestException as e:
        print(e)
        return None

    except KeyError as e:
        print(e)
        return None
