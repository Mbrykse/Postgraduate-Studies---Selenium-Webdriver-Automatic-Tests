import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
import test_data
import locators


class SklepTestPlTest(unittest.TestCase):
    def setUp(self):
        """Test Preparation"""
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        #  Open MainPage
        self.driver.get("https://skleptest.pl/")

    def tearDown(self):
        """Test Finished"""
        sleep(3)
        self.driver.quit()

    def testContact1(self):
        """Contact Message Test - Incorrect E-mail -Excepted Result -> Error Message Appear"""
        sleep(2)
        # Press Button "Contact"
        contact_btn = self.driver.find_element(By.ID, "menu-item-108")
        contact_btn.click()
        # Add Value in Registration - Name
        name_input = self.driver.find_element(By.XPATH, locators.REGISTRATION_NAME_XPH)
        name_input.send_keys(test_data.NAME)
        # Add Value in Invalid E-mail
        invalid_email_input = self.driver.find_element(By.XPATH, locators.REGISTRATION_EMAIL_XPH)
        invalid_email_input.send_keys(test_data.INVALID_EMAIL)
        # Add Value - Subject
        subject_input = self.driver.find_element(By.XPATH, locators.SUBJECT_XPH)
        subject_input.send_keys(test_data.SUBJECT)
        # Add Value - You Message
        message_input = self.driver.find_element(By.XPATH, locators.MESSAGE_XPH)
        message_input.send_keys(test_data.MESSAGE)
        # Press Submit
        submit_btn = self.driver.find_element(By.XPATH, locators.SEND_MSG_XPH)
        submit_btn.click()

    def testContact2(self):
        """Contact Message Test - Correct Data -Excepted Result -> Message Send"""
        sleep(2)
        # Press Button "Contact"
        contact_btn = self.driver.find_element(By.ID, "menu-item-108")
        contact_btn.click()
        # Add Value in Registration - Name
        name_input = self.driver.find_element(By.XPATH, locators.REGISTRATION_NAME_XPH)
        name_input.send_keys(test_data.NAME)
        # Add Value in Invalid E-mail
        email_input = self.driver.find_element(By.XPATH, locators.REGISTRATION_EMAIL_XPH)
        email_input.send_keys(test_data.EMAIL)
        # Add Value - Subject
        subject_input = self.driver.find_element(By.XPATH, locators.SUBJECT_XPH)
        subject_input.send_keys(test_data.SUBJECT)
        # Add Value - You Message
        message_input = self.driver.find_element(By.XPATH, locators.MESSAGE_XPH)
        message_input.send_keys(test_data.MESSAGE)
        # Add Value - You Message
        submit_btn = self.driver.find_element(By.XPATH, locators.SEND_MSG_XPH)
        submit_btn.click()

    def testLogin(self):
        """Login Test - Without Registration - UserName / Password - Excepted Action - Access Denied - Site Give Us Error Message"""
        sleep(2)
        # Press Button "Account"
        account_btn = self.driver.find_element(By.XPATH, locators.ACCOUNT_XPH)
        account_btn.click()
        # Add Value in Login - Username
        username_input = self.driver.find_element(By.ID, 'username')
        username_input.send_keys(test_data.USERNAME)
        # Add Value in Password
        password_input = self.driver.find_element(By.ID, "password")
        password_input.send_keys(test_data.PASSWORD)
        # Press Submit Button
        submit_btn = self.driver.find_element(By.XPATH, locators.SUBMIT_XPH)
        submit_btn.click()
    
    def testRegistration1(self):
        """Registration Test - Correct E-mail / Weak Password - Excepted Action - Registration Not allowed - Site Give Us Error Message"""
        sleep(2)
        # Press Button "Account"
        account_btn = self.driver.find_element(By.XPATH, locators.ACCOUNT_XPH)
        account_btn.click()
        # Add Value in Registration - Email
        email_input = self.driver.find_element(By.ID, 'reg_email')
        email_input.send_keys(test_data.EMAIL)
        # Add Value in Password
        invalid_password_input = self.driver.find_element(By.ID, "reg_password")
        invalid_password_input.send_keys(test_data.INVALID_PASSWORD)
        # Press Submit Button
        submit_btn = self.driver.find_element(By.XPATH, locators.REGISTER_XPH)
        submit_btn.click()
    
    def testRegistration2(self):
        """Registration Test 2 - Incorrect E-mail / Strong Password - Excepted Action - Registration Not allowed - Site Give Us Error Message"""
        sleep(2)
        # Press Button "Account"
        account_btn = self.driver.find_element(By.XPATH, locators.ACCOUNT_XPH)
        account_btn.click()
        # Add Value in Registration - Email
        invalid_email_input = self.driver.find_element(By.ID, 'reg_email')
        invalid_email_input.send_keys(test_data.INVALID_EMAIL)
        # Add Value in Password
        password_input = self.driver.find_element(By.ID, "reg_password")
        password_input.send_keys(test_data.PASSWORD)
        # Press Submit Button
        submit_btn= self.driver.find_element(By.XPATH, locators.REGISTER_XPH)
        submit_btn.click()
    
    def testSubscribtion1(self):
        """Join to Newsteller Test - Correct Data """
        sleep(2)
        # Add Value in Newsteller Name
        correct_name_input = self.driver.find_element(By.ID, 'es_txt_name')
        correct_name_input.send_keys(test_data.NAME)
        # Add Value in Newsteller E-mail
        correct_emial_input = self.driver.find_element(By.ID, "es_txt_email")
        correct_emial_input.send_keys(test_data.EMAIL)
        # Press Submit Button
        subscribe_btn= self.driver.find_element(By.XPATH, locators.SUBSCRIBE_XPH)
        subscribe_btn.click()

    def testSubscribtion2(self):
        """Join to Newsteller Test - Numeric Name / Correct E-mail """
        sleep(2)
        # Add Value in Newsteller Name
        numeric_name_input = self.driver.find_element(By.ID, 'es_txt_name')
        numeric_name_input .send_keys(test_data.NUMERIC_VALUE)
        # Add Value in Newsteller E-mail
        correct_emial_input = self.driver.find_element(By.ID, "es_txt_email")
        correct_emial_input .send_keys(test_data.EMAIL)
        # Press Submit Button
        subscribe_btn = self.driver.find_element(By.XPATH, locators.SUBSCRIBE_XPH)
        subscribe_btn.click()

    def testSubscribtion3(self):
        """Join to Newsteller Test - Name / InCorrect E-mail """
        sleep(2)
        # Add Value in Newsteller Name
        correct_name_input = self.driver.find_element(By.ID, 'es_txt_name')
        correct_name_input.send_keys(test_data.NAME)
        # Add Value in Newsteller E-mail
        incorrect_emial_input = self.driver.find_element(By.ID, "es_txt_email")
        incorrect_emial_input.send_keys(test_data.INVALID_EMAIL)
        # Press Submit Button
        subscribe_btn = self.driver.find_element(By.XPATH, locators.SUBSCRIBE_XPH)
        subscribe_btn.click()

    def testComment1(self):
        """Add Comment to Article  - Comment Posted"""
        sleep(2)
        # Open Tag
        open_tag = self.driver.find_element(By.XPATH, locators.TAGS_XPH)
        open_tag.click()
        # Go to Recent Post 1
        go_to_recent_post = self.driver.find_element(By.XPATH, locators.POST_XPH)
        go_to_recent_post.click()
        sleep(2)
        # Add Comment
        comment_add= self.driver.find_element(By.ID, "comment")
        comment_add.send_keys(test_data.COMMENT)
        sleep(2)
        # Add User
        add_user = self.driver.find_element(By.ID, "author")
        add_user.send_keys(test_data.NAME)
        sleep(2)
        # Add Email
        add_correct_email = self.driver.find_element(By.ID, "email")
        add_correct_email.send_keys(test_data.EMAIL)
        sleep(2)
        # Add Website
        add_website = self.driver.find_element(By.ID, "url")
        add_website.send_keys(test_data.WEBSITE)
        sleep(2)
        # Save Details
        save_checkbox = self.driver.find_element(By.ID, "wp-comment-cookies-consent")
        save_checkbox.click()
        sleep(2)
        #Submit Comment
        submit_comment = self.driver.find_element(By.ID, "submit")
        submit_comment.click()

    def testComment2(self):
        """Add Comment to Article - Invalid Email - Comment Not Posted - Error Message Appear"""
        sleep(2)
        # Open Tag
        open_tag = self.driver.find_element(By.XPATH, locators.TAGS_XPH)
        open_tag.click()
        # Go to Recent Post 1
        go_to_recent_post = self.driver.find_element(By.XPATH, locators.POST_XPH)
        go_to_recent_post.click()
        sleep(2)
        # Add Comment
        comment_add= self.driver.find_element(By.ID, "comment")
        comment_add.send_keys(test_data.COMMENT)
        sleep(2)
        # Add User
        add_user = self.driver.find_element(By.ID, "author")
        add_user.send_keys(test_data.NAME)
        sleep(2)
        # Add Email
        add_incorrect_email = self.driver.find_element(By.ID, "email")
        add_incorrect_email.send_keys(test_data.INVALID_EMAIL)
        sleep(2)
        # Add Website
        add_website = self.driver.find_element(By.ID, "url")
        add_website.send_keys(test_data.WEBSITE)
        sleep(2)
        # Save Details
        save_checkbox = self.driver.find_element(By.ID, "wp-comment-cookies-consent")
        save_checkbox.click()
        sleep(2)
        #Submit Comment
        submit_comment = self.driver.find_element(By.ID, "submit")
        submit_comment.click()

    def testComment3(self):
        """Add Comment to Article - Name / NO Email / NO URL / NO SAVE - Comment Not Posted - Error Message"""
        sleep(2)
        # Open Tag
        open_tag = self.driver.find_element(By.XPATH, locators.TAGS_XPH)
        open_tag.click()
        # Go to Recent Post 1
        go_to_recent_post = self.driver.find_element(By.XPATH, locators.POST_XPH)
        go_to_recent_post.click()
        sleep(2)
        # Add Comment
        comment_add= self.driver.find_element(By.ID, "comment")
        comment_add.send_keys(test_data.COMMENT)
        sleep(2)
        # Add User
        add_user = self.driver.find_element(By.ID, "author")
        add_user.send_keys(test_data.NAME)
        sleep(2)
        #Submit Comment
        submit_comment = self.driver.find_element(By.ID, "submit")
        submit_comment.click()

    def testComment4(self):
        """Add Comment to Article - NO Name  / Email - Correct / NO URL / NO SAVE - Comment Not Posted - Error Message"""
        sleep(2)
        # Open Tag
        open_tag = self.driver.find_element(By.XPATH, locators.TAGS_XPH)
        open_tag.click()
        # Go to Recent Post 1
        go_to_recent_post = self.driver.find_element(By.XPATH, locators.POST_XPH)
        go_to_recent_post.click()
        sleep(2)
        # Add Comment
        comment_add= self.driver.find_element(By.ID, "comment")
        comment_add.send_keys(test_data.COMMENT)
        sleep(2)
        # Add Email
        add_correct_email = self.driver.find_element(By.ID, "email")
        add_correct_email.send_keys(test_data.EMAIL)
        sleep(2)
        #Submit Comment
        submit_comment = self.driver.find_element(By.ID, "submit")
        submit_comment.click()

if __name__ == "__main__":
    unittest.main()