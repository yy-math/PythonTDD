from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest
from django.test import LiveServerTestCase

class NewVisitorTest(LiveServerTestCase):

	def setUp(self):
		self.browser = webdriver.Firefox()
		self.browser.implicitly_wait(3)

	def tearDown(self):
		self.browser.quit()

	def check_for_row_in_list_table(self, row_text):
		table = self.browser.find_element_by_id('id_list_table')
		rows = table.find_elements_by_tag_name('tr')
		self.assertIn(row_text, [row.text for row in rows])

	def test_can_start_a_list_and_retrieve_it_later(self):
		# tom has heard about a cool new to-do app
		# he goes to check out its homepage
		self.browser.get(self.live_server_url)

		# he notices the page tite and header mentions to-do lists
		self.assertIn('To-Do', self.browser.title)
		header_text = self.browser.find_element_by_tag_name('h1').text
		self.assertIn('To-Do', header_text)

		# he is invited to enter a to do item straight away
		inputbox = self.browser.find_element_by_id('id_new_item')
		self.assertEqual(
			inputbox.get_attribute('placeholder'),
			'Enter a to-do item'
		)

		# tom types "buy milk" into a text box
		inputbox.send_keys('buy milk')

		# when he hits enter the page updates and now lists
		# "1. buy milk" as an item in a to-do list
		inputbox.send_keys(Keys.ENTER)
		tom_list_url = self.browser.current_url
		self.assertRegex(tom_list_url, '/lists/.+')
		self.check_for_row_in_list_table('1: buy milk')

		# there is still a text box inviting tom to add another item
		# tom enters "make tea with milk"
		inputbox = self.browser.find_element_by_id('id_new_item')
		inputbox.send_keys('make tea with milk')
		inputbox.send_keys(Keys.ENTER)

		# the page updates again and now shows both items on list
		self.check_for_row_in_list_table('1: buy milk')
		self.check_for_row_in_list_table('2: make tea with milk') 


		# now a new user, monica comes along to the site

		# we use a new browser session to make sure that none of tom's
		# information is comes through from cookies etc
		self.browser.quit()
		self.browser= webdriver.Firefox()

		# monica visits the home page. there is no sign of tom's list
		self.browser.get(self.live_server_url)
		page_text = self.browser.find_element_by_tag_name('body').text
		self.assertNotIn('buy milk', page_text)
		self.assertNotIn('make tea with milk', page_text)

		# monica starts a new list by entering a new item
		inputbox = self.browser.find_element_by_id('id_new_item')
		inputbox.send_keys('make friends')
		inputbox.send_keys(Keys.ENTER)
	
		# monica gets her own unique URL
		monicas_list_url = self.browser.current_url
		self.assertRegex(monicas_list_url, '/lists/.+')
		self.assertself.assertNotEqual(monicas_list_url, tom_list_url)

		# again, there is no trace of tom's list
		page_text = self.browser.findelement_by_tag_name('body').text
		self.assertNotIn('buy milk', page_text)
		self.assertIn('make friends', page_text)

		# satisfied, both tom and monica go to sleep
