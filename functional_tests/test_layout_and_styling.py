from .base import FunctionalTest
import time
from selenium.webdriver.common.keys import Keys



class LayoutAndStylingTest(FunctionalTest):

    def test_layout_and_styling(self):
        # Edith goes to the home page
        self.browser.get(self.server_url)
        self.browser.set_window_size(1024, 768)
        
        # She notices the input box is nicely centered
        inputbox = self.get_item_input_box()
        inputbox.send_keys('testing\n')
        inputbox.send_keys(Keys.ENTER)
        self.wait_for_row_in_list_table('1: testing')
 #       time.sleep(2)
        inputbox = self.get_item_input_box()
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


    
 
