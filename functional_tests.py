from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest

class NewVisitorTest(unittest.TestCase):

	def setUp(self):
		self.browser = webdriver.Firefox()
		self.browser.implicitly_wait(3)

	def tearDown(self):
		self.browser.quit()

	def test_can_start_a_list_and_retrieve_it_later(self):
		# tom has heard about a cool new to-do app
		# he goes to check out its homepage
		self.browser.get('http://localhost:8000')

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

		table = self.browser.find_element_by_id('id_list_table')
		rows = table.find_elements_by_tag_name('tr')
		self.assertIn('1: buy milk', [row.text for row in rows])

		# there is still a text box inviting tom to add another item
		# tom enters "make tea with milk"
		inputbox = self.browser.find_element_by_id('id_new_item')
		inputbox.send_keys('make tea with milk')
		inputbox.send_keys(Keys.ENTER)

		# the page updates again and now shows both items on list
		table = self.browser.find_element_by_id('id_list_table')
		rows = table.find_elements_by_tag_name('tr')
		self.assertIn('1: buy milk', [row.text for row in rows])
		self.assertIn('2: make tea with milk', [row.text for row in rows]) 

		# tom sees the site has generated a unique URL for him
		# there is some explanatory text to that effect
		self.fail('Finish the test!')

		# tom visits his URL, the to do list is still there

		# satisfied, tom takes a nap	

if __name__ == '__main__':
	unittest.main(warnings='ignore')
