# NASA - Mission To Mars 


## Purpose

Built web application to scrape several websites, gathering Mars' latest information. 

Information to be extracted:
    - Latest Mars News from [NASA Mars News Site](https://mars.nasa.gov/news/)
    - Featured Mars Image from JPL Mars Space Images [JPL Mars Space](https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars)
    - Current Weather on Mars from [Mars Weather twitter Account](https://twitter.com/marswxreport?lang=en)
    - Mars Facts - from [Mars Facts webpage](https://space-facts.com/mars/)
    - Mars Hemispheres images from [USGS Astrogeology site](https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars)

## Tools Used
Python, Pandas, Flask, Splinter, MongoDB, PyMongo, HTML, Bootstrap, Jupyter Notebook

## Methodoloy

- Scraped the[NASA Mars News Site](https://mars.nasa.gov/news/), and collected the latest News Title and Paragraph Information. 
- Visited the url for [JPL Featured Space Image](https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars), and used splinter to navigate the site and find the full image url for the current Featured Mars Image. 
- Visited the [Mars Weather twitter Account](https://twitter.com/marswxreport?lang=en), and scraped the latest weather tweet from the page. 
- Visited the [Mars Facts webpage](https://space-facts.com/mars/) and use Pandas to scrape the table containing facts about the planet (i.e. Diameter, Mass, etc.) 
- Visited the [USGS Astrogeology site](https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars) to obtain high resolution images for each of Mar's hemispheres.
- scrape_mars.py 
    - Created a function called scrape that executes all of the scraping code, and returns one Python dictionary containing all of the scraped data.
- app.py
    - Created a route called /scrape that imports scrape_mars.py script and call the scrape function.
    - Created a root route / that will query the Mongo database and pass the mars data into an HTML template to display the data.
- index.html 
    - Created to hold the mars data dictionary, and to display all of the data in the appropriate HTML elements.
- On the top heading of the HTML main page clicking the "Scrape New Data" button will scrape all the data, and render the information. 

## Webpage Images

![Mission to Mars](Mission_to_Mars/Images/Mission_to_mars.png)

![Mission to Mars](Mission_to_Mars/Images/Mars_images.png)



