import unittest
import os
import sys
import types
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from main import google_search, scrap_company, list_all_urls, twitter_company_search

class TestGoogleSearch(unittest.TestCase):
    '''test to check tht company_name provided is a string'''
    def test_company_name_is_a_string(self):
        q =  'walmart'
        self.assertIsInstance(google_search(q), str)

    def test_scrap_company(self):
        '''test to check that results of urls are list'''
        url = 'https://movit.co.ug/'
        self.assertIsInstance(scrap_company(url), list)

    def test_list_all_urls(self):
        '''test to list all urls from search'''
        results = """
            <h2>The target Attribute</h2>
                <a href="https://www.twitter.com" target="_blank">Visit our HTML tutorial!</a>
                <a href = "info@cafejavas.co.ug"
                <a href='https://t.co/'</a>
                <a class="a-no-hover-decoration" href="https://twitter.com/MovitProductsUg?ref_src=twsrc%5Egoogle%7Ctwcamp%5Eserp%7Ctwgr%5Eauthor" ping="/url?sa=t&amp;source=web&amp;rct=j&amp;
                url=https://twitter.com/MovitProductsUg%3Fref_src%3Dtwsrc%255Egoogle%257Ctwcamp%255Eserp%257Ctwgr%255Eauthor&amp;ved=2ahUKEwiRzpuFvfHwAhVITBoKHRdFCUUQ6F56BAgCEAI&amp;cshid=1622380378317895"><br><h3 class="NsiYH">Movit (@MovitProductsUg) · Twitter</h3><div class="V0XQK"><cite class="ellip iUh30">https://twitter.com/MovitProductsUg</cite></div></a>
                <p>If you set the target attribute to "_blank", the link will open in a new browser window or tab.</p>
                        """
        self.assertIsInstance(list_all_urls(results), types.GeneratorType)

    def test_twitter_company_search(self):
        '''test to get twitter url using regex'''
        results = """
        
                        """
        self.assertIsInstance(twitter_company_search(results), string)




if __name__ == '__main__':
    unittest.main()