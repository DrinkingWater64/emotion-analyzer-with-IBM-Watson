import unittest
from EmotionDetection import emotion_detector

class TestEmotionDetection(unittest.TestCase):
    def test_positive_joy(self):
        text = "I am glad this happened"
        result = emotion_detector(text)
        self.assertEqual(result[0], 'joy')

    def test_negative_disgust(self):
        text = "I feel disgusted just hearing about this"
        result = emotion_detector(text)
        self.assertEqual(result[0], 'disgust')

    def test_negative_sadness(self):
        text = "I am so sad about this"
        result = emotion_detector(text)
        self.assertEqual(result[0], 'sadness')

    def test_negative_fear(self):
        text = "I am really afraid that this will happen"
        result = emotion_detector(text)
        self.assertEqual(result[0], 'fear')

if __name__ == '__main__':
    unittest.main()