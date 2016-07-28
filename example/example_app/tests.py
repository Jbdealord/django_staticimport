from django.test import TestCase, Client


class SimpleTest(TestCase):

	def setUp(self):
		self.client = Client()

	def test_basic_request(self):
		response = self.client.get('/')
		print(response.content.decode('utf8'))
