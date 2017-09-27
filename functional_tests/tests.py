from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import unittest


class NewVisitorTest(LiveServerTestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
 #       self.browser.implicitly_wait(0)

    def tearDown(self):
        self.browser.quit()

    def check_for_row_in_list_table(self, row_text):
        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertIn(row_text, [row.text for row in rows])      


    def test_can_start_a_list_and_retrieve_it_later(self):
        # Edith has heard about a cool new online to-do app. She goes
        # to check out its homepage
        self.browser.get(self.live_server_url)

        # at this point, the home.html is rendered in home_page  through the code
        # 'return render(request, 'home.html')'
        
        # print ('Self live server url:', self.live_server_url)

        # edith_list_url = self.browser.current_url
        # print ('Edith first current URL:', edith_list_url)

        time.sleep(2)

        # She notices the page title and header mention to-do lists
        self.assertIn('To-Do', self.browser.title)

        header_text = self.browser.find_element_by_tag_name('h1').text


        
        self.assertIn('To-Do', header_text)
        
        # She is invited to enter a to-do item straight away
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(
            inputbox.get_attribute('placeholder'),
            'Enter a to-do item'
        )       


        


        # She types "Buy peacock feathers" into a text box (Edith's hobby
        # is tying fly-fishing lures)


        inputbox.send_keys('Buy peacock feathers')

        # import time
        # time.sleep(10)



        # When she hits enter, the page updates, and now the page lists
        # "1: Buy peacock feathers" as an item in a to-do list


        inputbox.send_keys(Keys.ENTER)

        # Once user hits enter, home_page is still resolved and since it is
        # post action, redirect to list url, and then the list url is resolved to
        # view_list view, displaying the first item.
        
        time.sleep(2)

        edith_list_url = self.browser.current_url
        print ('Edith current URL:', edith_list_url)
        self.assertRegex(edith_list_url,'/lists/.+')
        self.check_for_row_in_list_table('1: Buy peacock feathers')
        

        # There is still a text box inviting her to add another itsm.  She
        # enters "Use peacock feathers to make a fly" (Edith is very methodical)


        inputbox = self.browser.find_element_by_id('id_new_item')

        # The lists url resolved to list.html is used for 2nd input.
        # The form-data is sent to the page specified in the action attribute "/"

        
        inputbox.send_keys('Use peacock feathers to make a fly')
        inputbox.send_keys(Keys.ENTER)


        time.sleep(2)
        
        edith_list_url = self.browser.current_url
        print ('Edith current URL:', edith_list_url)

       
        # The page updates again, and now shows both items on her list


        self.check_for_row_in_list_table('1: Buy peacock feathers')
        self.check_for_row_in_list_table('2: Use peacock feathers to make a fly')


        # Now a new user, Francis, comes along to the site.

        ## We use a new browser session to make sure that no information
        ## of Edith's is coming through from cookies etc
        self.browser.quit()
        self.browser = webdriver.Firefox()


        # Francis visits the home page.  There is no sign of Edith's
        # list
        self.browser.get(self.live_server_url)

        time.sleep(2)
        
        page_text = self.browser.find_element_by_tag_name('body').text
        self.assertNotIn('Buy peacock feathers', page_text)
        self.assertNotIn('make a fly', page_text)

        # Francis starts a new list by entering a new item. He
        # is less interesting than Edith ...
        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('Buy milk')
        inputbox.send_keys(Keys.ENTER)
        time.sleep(2)
        # Francis gets his own unique URL
        francis_list_url = self.browser.current_url
        print('Francis current URL:', francis_list_url)
        self.assertRegex(francis_list_url, '/lists/.+')
        self.assertNotEqual(francis_list_url, edith_list_url)

        # Again, there is no trace of Edith's list
        page_text = self.browser.find_element_by_tag_name('body').text
        self.assertNotIn('Buy peacock feathers', page_text)
        self.assertIn('Buy milk', page_text)

        # Satisfied, they both go back to sleep

        
        # Edith winders whether the site will remember her list.  Then she sees
        # that the site has generated a unique URL for her -- there is some
        # explanatory text to that effect.


        # self.fail('Finish the test!')


        # She visits that URL - her to-do list is still there.

        # Satisfied, she goes back to sleep


    def test_layout_and_styling(self):
        # Edith goes to the home page
        self.browser.get(self.live_server_url)
        self.browser.set_window_size(1024, 768)

        time.sleep(2)
        
        # She notices the input box is nicely centered
        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('testing\n')
        time.sleep(2)
        self.assertAlmostEqual(
            inputbox.location['x'] + inputbox.size['width'] / 2,
            512,
            delta=5
        )

        # She starts a new list and sees the input is nicely
        # centered there too
        #inputbox.send_keys('testing\n')
        #inputbox = self.browser.find_element_by_id('id_new_item')
        #self.assertAlmostEqual(
        #    inputbox.location['x'] + inputbox.size['width'] / 2,
        #    512,
        #    delta=5
        #)
       
        

if __name__ == '__main__':
    unittest.main(warnings='ignore')

