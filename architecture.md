Smart Deal Tracker
       |
       v
   Tkinter GUI
       |
       v
    Flask API
       |
       v
  API Authentication
       |
       v
    API Routes
       |
       +------------------+
       |         |        |
       v         v        v
 Price Service  Storage  Report Service
       |         |        |
       v         v        v
  Scrapers    products   Report CSV
       |
       +----------------+
       |                |
       v                v
 BeautifulSoup       Selenium
       |
       v
  Email Service