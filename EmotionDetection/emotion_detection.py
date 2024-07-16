import requests
import json

def emotion_detector(text_to_analyse):
    if not text_to_analyse.strip():
        # Return a dictionary with None values for all keys if input is blank
        return {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }
    
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    myobj = {"raw_document": {"text": text_to_analyse}}
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    
    try:
        response = requests.post(url, json=myobj, headers=header)
        response.raise_for_status()  # Raise HTTPError for bad responses (4xx, 5xx)
        
        response_dict = json.loads(response.text)
        emotion_scores = response_dict['emotionPredictions'][0]['emotion']
        emotions = ['anger', 'disgust', 'fear', 'joy', 'sadness']
        dominant_emotion = max(emotion_scores, key=emotion_scores.get)
        
        result = {emotion: emotion_scores.get(emotion, 0) for emotion in emotions}
        result['dominant_emotion'] = dominant_emotion
        
        return result
    
    except requests.exceptions.HTTPError as http_err:
        if response.status_code == 400:
            # Return a dictionary with None values for all keys for status code 400
            return {
                'anger': None,
                'disgust': None,
                'fear': None,
                'joy': None,
                'sadness': None,
                'dominant_emotion': None
            }
        else:
            raise  # Re-raise the exception if it's not a 400 error
    
    except Exception as err:
        print(f"Other error occurred: {err}")
        raise  # Re-raise the exception for other types of errors
