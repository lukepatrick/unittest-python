import logging
import urllib.request as urlreq
from urllib.parse import urlparse
import urltools
from lxml import html
import requests
import json


class crawler(object):
    
    def __init__(self, url=""):
        self.url = url
        self.log = logging.getLogger(__name__)
        self.domain = []
        self.third_party = []
        self.web_crawl_index = []

    def valid_url(self, url):
        """Validate the URL

        Args:
            url

        Returns:
            Boolean
        """
        if not url:
            return False


        try:
            request = urlreq.Request(url)
            response = urlreq.urlopen(request)
            # response valid
            return True
        except:
            # The url wasn't valid
            self.log.info("URL {} not valid or no Internet Connection".format(url))
            return False

    def parse_html(self, url):
        """Get URL and parse HTML to a usable tree

        Args:
            url

        Returns:
            tree object of HTML elements
        """
        if not self.valid_url(url):
            raise Exception("URL {} not valid or no Internet Connection".format(url))
        # Get Page
        page = requests.get(url)
        # Get HTML
        tree = html.fromstring(page.content)

        #XPath query for links
        links = tree.xpath('//a/@href')
        #Xpath query for static elements images
        images = tree.xpath('//img/@src')



        return links, images
    
    
    def process_links(self, url):
        """Process links in an website, organize links as same domain or 3rd party
        
        Args:
            url
           
        Returns:
            modifies class objects
        """

        links, images = self.parse_html(url=url)

        # parse the input url for a base domain
        my_domain_parsed = urltools.parse(url)
        my_domain_string = my_domain_parsed.domain + "." + my_domain_parsed.tld

        # {"link":url,
        # "sublinks": links,
        # "static-elements": images,
        #  "third-party": url}
        link_object = {}

        link_object["link"] = url
        link_object["sublinks"] = []
        link_object["static-elements"] = images
        link_object["third-party"] = []

        for link in links:
            parsed = urltools.parse(str(link))
            domain_string = parsed.domain + "." + parsed.tld
            if not parsed.path.startswith("#"):
                # skip all anchor links
                if domain_string == my_domain_string:
                    # compare domains, assuming subdomain does not matter for 'uniqueness'
                    subdomain = parsed.subdomain + "." if parsed.subdomain else ''
                    urlstring = parsed.scheme + "://" + subdomain + parsed.domain\
                                + "." + parsed.tld + parsed.path
                    if not urlstring in link_object["sublinks"]:
                        # sublinks is a relative unique list of links
                        link_object["sublinks"].append(urlstring)
                    if not urlstring in self.domain:
                        # self domain is global unique list of links
                        self.domain.append(urlstring)
                elif parsed.domain == '':
                    # handle relative path URL's, assume they belong to base domain of input url
                    path = parsed.path if parsed.path.startswith("/") else "/" + parsed.path
                    urlstring = my_domain_parsed.scheme + "://" + my_domain_parsed.subdomain + "." + \
                                my_domain_parsed.domain + "." + my_domain_parsed.tld + path
                    if not urlstring in link_object["sublinks"]:
                        # sublinks is a relative unique list of links
                        link_object["sublinks"].append(urlstring)
                    if not urlstring in self.domain:
                        # self domain is global unique list of links
                        self.domain.append(urlstring)
                else:
                    # handle non-matching domains, assume all third-party
                    subdomain = parsed.subdomain + "." if parsed.subdomain else ''
                    urlstring = parsed.scheme + "://" + subdomain + parsed.domain \
                                + "." + parsed.tld + parsed.path
                    if not urlstring in link_object["third-party"]:
                        # third-party is a relative unique list of links
                        link_object["third-party"].append(urlstring)
                    if not urlstring in self.third_party:
                        # self third party is global unique list of links
                        self.third_party.append(urlstring)

        self.web_crawl_index.append(link_object)

    def get_all_links(self, url, depth=5):
        """Loop over all links possible
            The only way a 'new' link gets added is if I haven't seen it yet
            loop over self.domain until no more links are added

        Args:
            url

        Returns:
            list
        """

        self.process_links(url)
        counter = 0

        for link in self.domain:
            self.process_links(link)
            counter += 1
            # let's stop at some point, this can go on for awhile if not properly handled
            if counter > depth:
                break

        print(json.dumps(self.web_crawl_index, indent=2)
)