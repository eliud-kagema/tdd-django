from django.test import TestCase
from selenium import webdriver

class FunctionalTestCase(TestCase):

    def setUp(self):
        self.browser = webdriver.Chrome('C:/Users/eliud.kagema/Downloads/chromedriver_win32/chromedriver.exe')

    def test_there_is_homepage(self):
        self.browser.get('http://localhost:8000')
        self.assertIn('Enter Hash Here', self.browser.page_source)

    def test_hash_of_hello(self):
        self.browser.get('http://localhost:8000')
        text = self.browser.find_element_by_id('id_text')
        text.send_keys('hello')
        self.browser.find_element_by_name('submit').click()


    def tearDown(self):
        self.browser.quit()





