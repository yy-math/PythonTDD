from selenium import webdriver
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
		self.fail('Finish the test!')

		# he is invited to enter a to do item straight away

		# tom types "buy milk" into a text box

		# when he hits enter the page updates and now lists
		# "1. buy milk" as an item in a to-do list

		# there is still a text box inviting tom to add another item
		# tom enters "make tea with milk"

		# the page updates again and now shows both items on list

		# tom sees the site has generated a unique URL for him
		# there is some explanatory text to that effect

		# tom visits his URL, the to do list is still there

		# satisfied, tom takes a nap	

if __name__ == '__main__':
	unittest.main(warnings='ignore')