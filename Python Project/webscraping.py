from selenium import webdriver 
from selenium.webdriver.common.action_chains import ActionChains 
  
# Make browser open in background 
options = webdriver.ChromeOptions() 
options.add_argument('headless') 
  
# Create the webdriver object 
browser = webdriver.Chrome( 
    executable_path="C:\chromedriver_win32\chromedriver.exe",  
  options=options) 
  
# Obtain the Google Map URL 
url = []
# Initialize variables and declare it 0 
i = 0
  
# Create a loop for obtaining data from URLs 
for i in range(len(url)): 
  
    # Open the Google Map URL 
    browser.get(url[i]) 
  
    # Obtain the title of that place 
    title = browser.find_element_by_class_name( 
        "x3AX1-LfntMc-header-title-title") 
    print(i+1, "-", title.text) 
  
    # Obtain the ratings of that place 
    stars = browser.find_element_by_class_name("aMPvhf-fI6EEc-KVuj8d") 
    print("The stars of restaurant are:", stars.text) 
    print("\n") 