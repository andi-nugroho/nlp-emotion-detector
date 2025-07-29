import unittest
import json
from unittest.mock import patch
from emotion_detection.emotion_detection import emotion_detector

class TestEmotionDetector(unittest.TestCase):
    @patch('emotion_detection.emotion_detection.requests.post')
    def test_emotion_detector(self, mock_post):
        # Definisikan contoh respons dari server tiruan (mock)
        mock_response_joy = {'emotionPredictions': [{'emotion': {'joy': 0.9}}]}
        mock_response_anger = {'emotionPredictions': [{'emotion': {'anger': 0.9}}]}
        mock_response_disgust = {'emotionPredictions': [{'emotion': {'disgust': 0.9}}]}
        mock_response_sadness = {'emotionPredictions': [{'emotion': {'sadness': 0.9}}]}
        mock_response_fear = {'emotionPredictions': [{'emotion': {'fear': 0.9}}]}

        # Test untuk emosi 'joy'
        mock_post.return_value.status_code = 200
        # PERBAIKAN: Ubah dictionary menjadi string JSON untuk .text
        mock_post.return_value.text = json.dumps(mock_response_joy)
        result1 = emotion_detector("I am glad this happened")
        self.assertEqual(result1['dominant_emotion'], 'joy')

        # Test untuk emosi 'anger'
        mock_post.return_value.text = json.dumps(mock_response_anger)
        result2 = emotion_detector("I am really mad about this")
        self.assertEqual(result2['dominant_emotion'], 'anger')

        # Test untuk emosi 'disgust'
        mock_post.return_value.text = json.dumps(mock_response_disgust)
        result3 = emotion_detector("I feel disgusted just hearing about this")
        self.assertEqual(result3['dominant_emotion'], 'disgust')

        # Test untuk emosi 'sadness'
        mock_post.return_value.text = json.dumps(mock_response_sadness)
        result4 = emotion_detector("I am so sad about this")
        self.assertEqual(result4['dominant_emotion'], 'sadness')

        # Test untuk emosi 'fear'
        mock_post.return_value.text = json.dumps(mock_response_fear)
        result5 = emotion_detector("I am really afraid that this will happen")
        self.assertEqual(result5['dominant_emotion'], 'fear')

if __name__ == '__main__':
    unittest.main()