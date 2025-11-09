import unittest
from unittest.mock import patch, MagicMock

from projects.rekognition_image_label_detection.src import main as rk_main


class TestDetectLabels(unittest.TestCase):
    @patch('projects.rekognition_image_label_detection.src.main.boto3')
    def test_detect_labels_returns_count(self, mock_boto3):
        # Setup mock rekognition client
        mock_client = MagicMock()
        mock_client.detect_labels.return_value = {
            'Labels': [
                {'Name': 'Dog', 'Confidence': 99.0, 'Instances': [], 'Parents': []}
            ]
        }
        mock_boto3.client.return_value = mock_client

        count = rk_main.detect_labels('photo.jpg', 'some-bucket')
        self.assertEqual(count, 1)


if __name__ == '__main__':
    unittest.main()
