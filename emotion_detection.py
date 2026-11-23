"""Emotion detection using the IBM Watson NLP embedded emotion endpoint."""
import json
import requests

URL = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
HEADERS = {'grpc-metadata-mm-model-id': 'emotion_aggregated-workflow_lang_en_stock'}


def emotion_detector(text_to_analyze):
    """Return emotion scores and the dominant emotion for input text."""
    if not isinstance(text_to_analyze, str) or not text_to_analyze.strip():
        return {'anger': None, 'disgust': None, 'fear': None,
                'joy': None, 'sadness': None, 'dominant_emotion': None}
    response = requests.post(URL, json={'raw_document': {'text': text_to_analyze}},
                             headers=HEADERS, timeout=20)
    if response.status_code == 400:
        return {'anger': None, 'disgust': None, 'fear': None,
                'joy': None, 'sadness': None, 'dominant_emotion': None}
    response.raise_for_status()
    payload = response.json()
    emotions = payload['emotionPredictions'][0]['emotion']
    scores = {name: emotions[name] for name in ('anger', 'disgust', 'fear', 'joy', 'sadness')}
    scores['dominant_emotion'] = max(scores, key=scores.get)
    return scores
