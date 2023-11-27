# PyKP

Railway connection browser and planning system \
**GitHub repo:** `janymal/PyKP`

## Team composition

Jan Kot, Emil Gruszecki, Filip Łukasik

## Project goals

-   scraping data from `portalpasazera.pl` or `bilkom.pl`
-   the database of:
    -   stations and platforms
    -   railways
    -   trains
    -   schedules
-   web UI with a map of available connections
-   planning system:
    -   adding new connections
    -   collision detection
-   user accounts:
    -   permission management
    -   favorites
    -   per user plans (???)
-   technologies: Python, Django, Scrapy, PostgreSQL/MySQL, OpenStreetMap

## Work schedule

### First week

**End goal:** Working database populated with scraped data \
**Steps:**

-   Setting up the environment
-   Preparing the data scrapers
-   Establishing a connection with database
-   Populating the database

### Second week

**End goal:** Web UI prototype \
**Steps:**

-   Experimenting with OSM rendering
-   Putting points and lines on the map
-   Designing basic UI layout

### Third week

**End goal:** Working Django server \
**Steps:**

-   Connecting to the database
-   Serving the map prototype via Django server

### Fourth week

**End goal:** Working planning algorithm prototype \
**Steps:**

-   Designing and implementing the algorithm

### Fifth week

**End goal:** Almost final Web UI with working functionalities \
**Steps:**

-   Connecting individual components (frontend with backend)
-   Prototyping user handling
-   Prototyping user features
-   Finishing the UI design

### Sixth week

**End goal:** User authentication and features added to the UI \
**Steps:**

-   Creating and connecting the user accounts database table
-   Handling user authentication
-   Implementing the list of favorite routes, stations etc.

### Seventh week

**End goal:** Fully working application \
**Steps:**

-   Testing
-   Bugfix
-   Final touches
