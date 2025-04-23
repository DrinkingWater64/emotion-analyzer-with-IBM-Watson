import unittest
from EmotionDetection import emotion_detector

class TestEmotionDetection(unittest.TestCase):
    def test_positive_joy(self):
        text = "I am glad this happened"
        self.assertEqual(emotion_detector(text), 'joy')

    def test_negative_disgust(self):
        text = "I feel disgusted just hearing about this"
        self.assertEqual(emotion_detector(text), 'disgust')

    def test_negative_sadness(self):
        text = "I am so sad about this"
        self.assertEqual(emotion_detector(text), 'sadness')

    def test_negative_fear(self):
        text = "I am really afraid that this will happen"
        self.assertEqual(emotion_detector(text), 'fear')

if __name__ == '__main__':
    unittest.main()