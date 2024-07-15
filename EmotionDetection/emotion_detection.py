import requests
import json

def emotion_detector(text_to_analyse):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    myobj = { "raw_document": { "text": text_to_analyse } }
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    response = requests.post(url, json = myobj, headers = header)

    if response.status_code==200:
        formatted_response = json.loads(response.text)
        emotion_dict = formatted_response['emotionPredictions'][0]['emotion']
        emotion_dict['dominant_emotion'] = max(emotion_dict, key = emotion_dict.get)     
    elif response.status_code==400:
        emotion_dict={'anger': None, 'disgust': None, 'fear': None, 'joy': None, 'sadness': None, 'dominant_emotion':None}
    return emotion_dict



