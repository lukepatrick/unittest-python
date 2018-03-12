## Python Web Crawler
This project is a learning experiment to quickly design and implement a simple
web crawler in a language of choice. 

This was built demonstrating good practices with Python 3.x.

The goals for this simple app are:
- limited to one domain
- visit all pages within the domain
- not follow the links to external sites such as Google or Twitter.
- Output simple structured site map (any format)
	- showing links to other pages under the same domain
	- links to external URLs
	- links to static content such as images
	- for each respective page

## Setup

Assuming a Mac, use [Homebrew](https://brew.sh/) to install python3 if not already
set up

    $ brew install python3
    
Clone the repository to your machine.

    $ git clone https://github.com/lukepatrick/unittest-python.git
    
Enter directory and set up virtualenv

    $ cd unittest-python/webcrawler
    $ virtualenv env --no-site-packages --python=python3
    $ source env/bin/activate
    $ pip3 install -r requirements.txt
    
## Quick start

Run the app:

    $ python web_index.py http://www.google.com 4

Parameters: a valid URL to crawl and (optional) 'depth', the number of sublinks from
the base URL to follow before stopping. The default value is 5 if no value specified.

## Output



Each json array item is an object with the base url/link, all sublinks from that
location, any static-elements (currently images), and any third-party links



## Design
The project is built around a crawler package that could be imported to any application
use, whether a CLI app used in an example here or to pull into your Flask API
app, etc..

The crawler package is made up of a handful of utility methods that each are useful
on their own and ripe for refactoring for any process, design, etc.. improvements.

These utilities are 
	
- URL validator, always test when there is user input
- Parse HTML, get the HTML from a URL and extract the HTML to programmatically useful objects
- Link Processor, deconstruct and reconstruct URLs for comparison and tracking
- Get All Links, call Link Processor in a loop until all sublinks extracted from a site or a 'depth' reached


## Future
Where to take this project next
- Improve extraction of static elements
- Test more sites and gather more examples
- Improve for performance
- Test or design a better output format


## Test

Run the nose2 test framework. Depending on your environment, if you have multiple python
versions installed you may have to specify which python runs nose2. 

    $ nose2

If you're running both python2 and 3, try:

    $ python3 -m "nose2"
