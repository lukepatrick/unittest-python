import unittest

from .context import crawler


class CrawlerTestCase(unittest.TestCase):
    def setUp(self):
        self.myCrawler = crawler.crawler.crawler()

    def tearDown(self):
        self.myCrawler = None

    def test_valid_url(self):
        url = "http://www.google.com"

        response = None
        response = self.myCrawler.valid_url(url=url)
        self.assertIsNotNone(response)
        self.assertTrue(response)

    def test_valid_url_bad(self):
        url = "AAABBBBDDD"

        response = None
        response = self.myCrawler.valid_url(url=url)
        self.assertIsNotNone(response)
        self.assertFalse(response)

    def test_parse_html(self):
        url = "http://www.google.com"

        links = None
        images = None
        links, images = self.myCrawler.parse_html(url=url)
        self.assertIsNotNone(links)
        self.assertIsNotNone(images)
        self.assertGreater(len(links), 0)
        self.assertGreater(len(images), 0)

    def test_process_links(self):
        url = "http://www.charter.com/"

        self.myCrawler.process_links(url=url)
        self.assertIsNotNone(self.myCrawler.domain)
        self.assertGreater(len(self.myCrawler.domain), 0)

    def test_get_all_links(self):
        url = "http://www.charter.com/"

        self.myCrawler.get_all_links(url=url)
        self.assertIsNotNone(self.myCrawler.domain)
        self.assertGreater(len(self.myCrawler.domain), 0)

    def test_get_all_links_depth(self):
        url = "http://www.charter.com/"

        self.myCrawler.get_all_links(url=url, depth=1)
        self.assertIsNotNone(self.myCrawler.domain)
        self.assertGreater(len(self.myCrawler.domain), 0)

    def test_get_all_links_bad(self):
        with self.assertRaises(Exception) as context:
            url = "AAABBCCC"
            self.myCrawler.get_all_links(url=url, depth=1)

        self.assertTrue("not valid" in str(context.exception))



if __name__ == '__main__':
    unittest.main()


