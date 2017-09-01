from selenium import webdriver
import unittest

class NewVisitorTest(unittest.TestCase):

	def setUp(self):
		self.browser = webdriver.Firefox()

	def tearDown(self):
		self.browser.quit()

	def test_can_start_a_list_and_retrieve_it_later(self):
		# Edith has heard about a cool new online to-do app. She checks out the homepage
		self.browser.get('http://localhost:8000')

		# she notices the page title and header mention to-do lists
		self.assertIn('To-Do', self.browser.title)
		sef.fail('Finish the test!')

		# She is invited to enter a to-do item

		# She types "Buy peacock feathers" into a text box

		# When she hits enter, the page updates and has that item on the list

		# There is a text box inviting her to add another item. She adds another item

		# The page updates and shows both items now

		# The site has generated a unique URL for here

		# She visits the URL and her stuff is on there

		# The End


if __name__ == '__main__':
	unittest.main(warnings='ignore')

