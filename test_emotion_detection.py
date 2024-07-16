from EmotionDetection.emotion_detection import emotion_detector
import unittest
class TestEmotionDection(unittest.TestCase):
    def test_emotion_detector(self):

        result_1 = emotion_detector('I am glad this happened')
        self.assertEqual(result_1['label'], 'joy')

        result_2 = emotion_detector('I am really mad about this')
        self.assertEqual(result_2['label'], 'anger')

        result_3 = emotion_detector('I feel disgusted just hearing about this')
        self.assertEqual(result_3['label'], 'disgust')

        result_4 = emotion_detector('I am so sad about this')
        self.assertEqual(result_4['label'], 'sadness')

        result_5 = emotion_detector('I am really afraid that this will happen')
        self.assertEqual(result_5['label'], 'fear')
    unittest.main()
    


    

