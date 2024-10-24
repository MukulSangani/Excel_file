from django.test import TestCase
from django.urls import reverse
from rest_framework import status

class UploadAPITest(TestCase):
    def test_upload_file(self):
        with open('C:/Users/admin/Downloads/Practical Task Python sheet (4).xlsx', 'rb') as file:
            response = self.client.post(reverse('upload-file'), {'file': file})
            self.assertEqual(response.status_code, status.HTTP_201_CREATED)
            self.assertEqual(response.data['message'], 'Data uploaded successfully!')
