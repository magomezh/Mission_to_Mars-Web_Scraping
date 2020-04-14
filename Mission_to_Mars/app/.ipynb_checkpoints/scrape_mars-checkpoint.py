from splinter import Browser
from bs4 import BeautifulSoup
import pandas as pd
import datetime as dt
from urllib.parse import urlsplit
import time
import re


def scrape_all():

    # Initiate headless driver for deployment
    browser = Browser("chrome", executable_path="chromedriver", headless=True)
    news_title, news_paragraph = mars_news(browser)

    # Run all scraping functions and store in dictionary.
    data = {
        "news_title": news_title,
        "news_paragraph": news_paragraph,
        "featured_image": featured_image(browser),
        "hemispheres": hemispheres(browser),
        "weather": twitter_weather(browser),
        "facts": mars_facts(),
        "last_modified": dt.datetime.now()
    }

    # Stop webdriver and return data
    browser.quit()
    return data


def mars_news(browser):
    url = "https://mars.nasa.gov/news/"
    browser.visit(url)

    # Optional delay for loading the page, getting first item in the list
    browser.is_element_present_by_css("ul.item_list li.slide", wait_time=2)

    html = browser.html
    t_soup = BeautifulSoup(html, 'html.parser')

    try:
        slide_element = t_soup.select_one('ul.item_list li.slide')
        news_title = slide_element.find('div', class_='content_title').get_text()
        news_p= slide_element.find('div', class_='article_teaser_body').get_text()

    except AttributeError:
        return None, None

    return news_title, news_p



def featured_image(browser):
    url = "https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"
    browser.visit(url)

    # Obtain base url
    base_url = "{0.scheme}://{0.netloc}/".format(urlsplit(url))
    
    # Find the 'Full Image' button, and use .click() method to access
    browser.is_element_present_by_text('FULL IMAGE', wait_time=0.5)
    fi_elem = browser.links.find_by_partial_text('FULL IMAGE')
    fi_elem.click()
    
    # Find 'more info' button and .click()
    mi_elem = browser.click_link_by_partial_text('more info')

    # Parse the resulting html with soup
    html = browser.html
    i_soup = BeautifulSoup(html, 'html.parser')

    # Find the relative image url
    img_url = i_soup.find("img", class_="main_image")["src"]
    
    # Use the base url to create an absolute url
    full_img_url = base_url + img_url
    
    return full_img_url

#hello

def hemispheres(browser):

    h_url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    browser.visit(h_url)

    # Click the link, find the sample anchor, return the href
    image_urls = []

    # First, get a list of all of the hemispheres
    links = browser.find_by_css("a.product-item h3")

    # Next, loop through those links, click the link, find the sample anchor, return the href
    for i in range(len(links)):
        hemisphere = {}
    
        # We have to find the elements on each loop to avoid a stale element exception
        browser.find_by_css("a.product-item h3")[i].click()
    
        # Next, we find the Sample image anchor tag and extract the href
        sample_elem = browser.find_link_by_text('Sample').first
        hemisphere['img_url'] = sample_elem['href']
    
        # Get Hemisphere title
        hemisphere['title'] = browser.find_by_css("h2.title").text
    
        # Append hemisphere object to list
        image_urls.append(hemisphere)
    
        # Finally, we navigate backwards
        browser.back()
        
    return image_urls


def twitter_weather(browser):
    t_url = 'https://twitter.com/marswxreport?lang=en'
    browser.visit(t_url)

    time.sleep(5)

    html = browser.html
    w_soup = BeautifulSoup(html, 'html.parser')

    # re.compile(pattern, repl, string):
    pattern = re.compile(r'sol')
    m_weather = w_soup.find('span', text=pattern).text
    

    return m_weather


def mars_facts():
    try:
        mars_df = pd.read_html('https://space-facts.com/mars/')[0]
    except BaseException:
        return None

    mars_df.columns=['Information', 'Value']
    mars_df.set_index('Information', inplace=True)

    # Add some bootstrap styling to <table>
    return mars_df.to_html(classes="table table-striped")




if __name__ == "__main__":

    # If running as script, print scraped data
    print(scrape_all())
