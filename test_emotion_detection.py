from EmotionDetection.emotion_detection import emotion_detector
import unittest

class TestEmotionDetector(unittest.TestCase):
    def text_emotion_detector(self):
        testcase_one = emotion_detector('I am glad this happened')
        self.assertEqual(testcase_one['dominant_emotion'],'joy')
        testcase_two = emotion_detector('I am really mad about this')
        self.assertEqual(testcase_two['dominant_emotion'], 'anger')
        testcase_three = emotion_detector('I feel disgusted just hearing about this')
        self.assertEqual(testcase_three['dominant_emotion'], 'disgust')
        testcase_four = emotion_detector('I am so sad about this')
        self.assertEqual(testcase_four['dominant_emotion'], 'sadness')
        testcase_five = emotion_detector('I am really afraid that this will happen')
        self.assertEqual(testcase_five['dominant_emotion'], 'fear')

unittest.main()