from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium import webdriver
import os
import sys
import platform

os.environ['DJANGO_LIVE_TEST_SERVER_ADDRESS'] = 'localhost:8001'


class FunctionalTest(StaticLiveServerTestCase):

    @classmethod
    def setUpClass(cls):
        for arg in sys.argv:
            if 'liveserver' in arg:
                cls.server_url = 'http://' + arg.split('=')[1]
                return
        super().setUpClass()
        cls.server_url = cls.live_server_url

    @classmethod
    def tearDownClass(cls):
        if cls.server_url == cls.live_server_url:
            super().tearDownClass()

    def setUp(self):
        if platform.system() == 'Windows':
            self.browser = webdriver.Chrome('c:\\WebDev\\chromedriver.exe')
        elif platform.system() == 'Darwin':
            self.browser = webdriver.Firefox()
        else:
            return False
        self.browser.implicitly_wait(10)

    def tearDown(self):
        self.browser.quit()

    def check_for_row_in_list_table(self, row_text):
        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertIn(row_text, [row.text for row in rows])
