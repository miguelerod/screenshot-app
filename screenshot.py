import sys

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from os import path, mkdir


exec_path = "./chromedriver.exe"

list_path = input("Insert the path for the file where the URL's are: ")
if(not path.isfile(list_path)):
    print("The provided path is not file please try again with a valid path.")
    sys.exit(1)
    
if(not path.exists(list_path)):
    print("The provided path is not valid, please try again with a valid path.")
    sys.exit(1)

try:
    with open(list_path, 'r') as urls_file:
        urls = urls_file.read().split('\n')
except OSError:
    print ("Could not read from %s, please try again" % list_path)
    sys.exit(1)

folder_path = input("Insert the path of the folder where the screenshots will be saved: ")
if(path.isfile(folder_path)):
    print("The provided path is a file please try again with a valid path.")
    sys.exit(1)
    
if((not path.exists(folder_path))):
    try:
        mkdir(folder_path)
    except IOError:
        print ("Creation of the directory %s failed, please try again" % folder_path)
        sys.exit(1)

wd_options = Options()
wd_options.add_argument("--disable-notifications")
wd_options.add_argument("--disable-infobars")
wd_options.add_argument("--mute-audio")
driver = webdriver.Chrome(
	executable_path=exec_path, options=wd_options)  

for url in urls:
    print(f"Getting {url}")
    driver.get(url)
    filename = "".join(x for x in url if x.isalnum())
    print(f"Saving screenshot as {folder_path}/{filename}.png")
    driver.save_screenshot(f"{folder_path}/{filename}.png")
driver.close()
