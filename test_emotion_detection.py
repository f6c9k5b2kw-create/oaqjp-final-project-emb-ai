"""Unit tests for the emotion detector (mock external API to make tests repeatable)."""
import unittest
from unittest.mock import patch, Mock
from EmotionDetection import emotion_detector


class TestEmotionDetector(unittest.TestCase):
    def test_five_emotions(self):
        cases = [('I am glad this happened', 'joy'),
                 ('I am really mad about this', 'anger'),
                 ('I feel disgusted just hearing about this', 'disgust'),
                 ('I am so sad about this', 'sadness'),
                 ('I am really afraid of this', 'fear')]
        for text, expected in cases:
            with self.subTest(expected=expected):
                scores = dict.fromkeys(('anger', 'disgust', 'fear', 'joy', 'sadness'), 0.1)
                scores[expected] = 0.9
                mocked_response = Mock(status_code=200)
                mocked_response.json.return_value = {'emotionPredictions': [{'emotion': scores}]}
                with patch('EmotionDetection.emotion_detection.requests.post', return_value=mocked_response):
                    self.assertEqual(emotion_detector(text)['dominant_emotion'], expected)

    def test_empty_input(self):
        self.assertIsNone(emotion_detector('')['dominant_emotion'])


if __name__ == '__main__':
    unittest.main()
