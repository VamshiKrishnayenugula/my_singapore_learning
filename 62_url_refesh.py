import time 
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# url to open and refresh

url = "https://chat.openai.com/"

#installs web driver for chrome

driver= webdriver.Chrome(service = Service(ChromeDriverManager().install()))

driver.get(url)

#waiting time before refresh

time.sleep(10)
driver.refresh()


"""Did you know that you can refresh a URL using Python? 
Usually, to refresh a page, we have to do it manually. However, 
we can automate the process with just a few lines of code. We 
will use the selenium module for this. Install the following:
pip install selenium
pip install webdriver-manager
Now, let’s write the code. I am using the Chrome web browser, 
so I will need Chrome dependencies. If you are using another 
browser, you will need to install a driver for that browser. So, 
we need the URL link of the website that we want to open. The 
time is the number of seconds we want to wait before refreshing 
the page. The code will automatically refresh the page once the 
waiting time is over."""