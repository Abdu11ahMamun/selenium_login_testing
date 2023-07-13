import time
import unittest
from selenium import webdriver

class GoogleTestCase(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Chrome()  # Change to Chrome driver
        self.addCleanup(self.browser.quit)

    def test_page_title(self):
        self.browser.get('http://192.168.1.154:8080/beftn/faces/login.xhtml')

        # Delay for 10 seconds
        time.sleep(10)

        # Fill in the login form
        username_input = self.browser.find_element('xpath', '//*[@id="j_idt13"]/table[2]/tbody/tr[2]/td/input')
        password_input = self.browser.find_element('xpath', '//*[@id="j_idt13:masked-password"]')
        submit_button = self.browser.find_element('xpath', '//*[@id="j_idt13"]/table[2]/tfoot/tr/td/input')

        username_input.send_keys('ictshams')
        password_input.send_keys('a')
        submit_button.click()
        time.sleep(5)


        # Verify the URL after login
        expected_url = 'http://192.168.1.154:8080/beftn/faces/index.xhtml'
        if self.browser.current_url == expected_url:
            print("Success: Login Successful!")
        else:
            self.assertIn('Login', self.browser.title)

if __name__ == '__main__':
    unittest.main(verbosity=2)
