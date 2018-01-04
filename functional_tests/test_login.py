from contextlib import contextmanager
import os
import poplib
import re
import time
from django.core import mail
from selenium.webdriver.common.keys import Keys


from .base import FunctionalTest

#TEST_EMAIL = 'edith@example.com'
#TEST_EMAIL = 'mkwokdjango@gmail.com'
SUBJECT = 'Your login link for Superlists'

class loginTest(FunctionalTest):

    def test_can_get_email_link_to_log_in(self):
        # Edith goes to the awesome superlists site
        # and notices a "Log in" section in the navbar for the first time
        # It's telling her to enter her email address, so she does
        if self.staging_server:
            #test_email = 'kwokyukming@yahoo.com'
            #test_email = 'mkwokdjango@gmail.com'
            test_email = os.environ['TEST_EMAIL']
        else:
            #test_email = 'edith@example.com'
            test_email = os.environ['TEST_EMAIL']
            
        self.browser.get(self.live_server_url)
        print(' current live server url', self.live_server_url)
        #self.browser.find_element_by_name('email').send_keys(TEST_EMAIL)
        self.browser.find_element_by_name('email').send_keys(test_email)
        self.browser.find_element_by_name('email').send_keys(Keys.ENTER)

        # A message appears telling her an email has been sent
        self.wait_for(lambda: self.assertIn(
            'Check your email',
            self.browser.find_element_by_tag_name('body').text
        ))


        # She checks her email and finds a message
        #email = mail.outbox[0]
        #self.assertIn(TEST_EMAIL, email.to)
        #self.assertEqual(email.subject, SUBJECT)
        print('test_email: ', test_email)
        body = self.wait_for_email(test_email, SUBJECT)

        # It has a url link in it
        #self.assertIn('Use this link to log in', email.body)
        #url_search = re.search(r'http://.+/.+$', email.body)
        self.assertIn('Use this link to log in', body)
        url_search = re.search(r'http://.+/.+$', body)
        if not url_search:
            failstr = 'Could not find url in email body:\n{}'
            #self.fail(failstr.format(email.body))
            self.fail(failstr.format(body))
        url = url_search.group(0)
        self.assertIn(self.live_server_url, url)

        # She clicks it
        self.browser.get(url)

        # She is logged in!
        #self.wait_to_be_logged_in(email=TEST_EMAIL)
        self.wait_to_be_logged_in(email=test_email)

        # NOw she logs out
        self.browser.find_element_by_link_text('Log out').click()

        # She is logged out
        #self.wait_to_be_logged_out(email=TEST_EMAIL)
        self.wait_to_be_logged_out(email=test_email)



    @contextmanager
    def pop_inbox(self, test_email):
        try:
            inbox = poplib.POP3_SSL(os.environ['TEST_POP_SERVER'])
            inbox.user(test_email)
            inbox.pass_(os.environ['TEST_PASSWORD'])
            yield inbox
    
        finally:
            inbox.quit()

        
    def wait_for_email(self, test_email, subject):
        #if not self.staging_server:
        #    print('no staging server')
        #    email = mail.outbox[0]
        #    self.assertIn(test_email, email.to)
        #    self.assertEqual(email.subject, subject)
        #    return email.body

        last_count = 0
        start = time.time()

        subjectstr = 'Subject: {}'
        print('hello ..hello hello hello.')
        while time.time() - start < 60:
            with self.pop_inbox(test_email) as inbox:
                count, _ = inbox.stat()
                if count != last_count:
                    for i in range(count, last_count, -1):
                        _, lines, __ = inbox.retr(i)
                        lines = [l.decode('utf8') for l in lines]
                        if subjectstr.format(subject) in lines:
                            inbox.dele(i)
                            return '\n'.join(lines)
                    last_count = count
            time.sleep(5)

                        
                    
                    
 

'''
        email_id = None
        start = time.time()
        inbox = poplib.POP3_SSL('pop.mail.yahoo.com')
        #inbox = poplib.POP3_SSL('pop.gmail.com')
        try:
            print('yahoo pwd: ', os.environ['YAHOO_PASSWORD'])
            print('test email: ', test_email)
            inbox.user(test_email)
            inbox.pass_(os.environ['YAHOO_PASSWORD'])
            #inbox.pass_(os.environ['EMAIL_PASSWORD'])
            print('gmail pwd: ', os.environ['EMAIL_PASSWORD'])
            subjectstr = 'Subject: {}'
            print('hello 1')
            while time.time() - start < 60:
                print('hello 2')
                # get 10 newest messages
                count, _ = inbox.stat()
                print('count: ', count)
                for i in reversed(range(max(1, count - 10), count + 1)):
                    print('getting msg', i)
                    _, lines, __ = inbox.retr(i)
                    lines = [l.decode('utf8') for l in lines]
                    #print(lines)
                    if subjectstr.format(subject) in lines:
                        email_id = i
                        body = '\n'.join(lines)
                        print('hello 3')
                        return body
                time.sleep(5)
                print(' hello \n')

        finally:
            if email_id:
                inbox.dele(email_id)
            inbox.quit()

                
'''
                         

                      
        
