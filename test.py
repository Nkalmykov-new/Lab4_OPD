from main import app
import unittest
class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        app.testing = True
        self.app = app.test_client()
    def test_home(self):
        result = self.app.get('/')
        self.assertEqual(result.status_code, 200)
    def test_form(self):
        result = self.app.get('/')
        assert b"Submit" in result.data

    def test_file(self):
        result = self.app.get('/')
        assert b"file" in result.data

    def test_txt_file(self):  # тестируем функцию, которая отвечает за обработку .txt файлов
        test = app.test_client(self)
        with open('1.txt', 'rb') as f:
            response = test.post('/find_word', content_type='multipart/form-data', data={'file': f})
        self.assertIn('Самое часто встречаемое слово "3"',response.data.decode())