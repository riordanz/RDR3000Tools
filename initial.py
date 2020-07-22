# from __future__ import print_function
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep
import sys
chrome_options = Options()
chrome_options.add_argument("--headless")

if sys.platform.startswith('win'):
	driver = webdriver.Chrome('chromedriver.exe', options = chrome_options)
else:
	driver = webdriver.Chrome('./chromedriver', options = chrome_options)
# driver.set_page_load_timeout(10)
driver.implicitly_wait(5)

def get(url):
	global driver
	driver.get(url)

def wait(jenis,element):
	global driver
	wait = WebDriverWait(driver, 300)

	if jenis.lower() == 'xpath':
		wait.until(EC.presence_of_element_located((
	By.XPATH, element)))
	elif jenis.lower() == 'name':
		wait.until(EC.presence_of_element_located((
	By.NAME, element)))
	elif jenis.lower() == 'id':
		wait.until(EC.presence_of_element_located((
	By.ID, element)))
	elif jenis.lower() == 'class':
		wait.until(EC.presence_of_element_located((
	By.CLASS_NAME, element)))
	elif jenis.lower() == 'css':
		wait.until(EC.presence_of_element_located((
	By.CSS_SELECTOR, element)))
	else:
		print("Error Wait Script !!!")
		exit()

def find(jenis,element):
	global driver
	if jenis.lower() == 'xpath':
		return driver.find_element_by_xpath(element)
	elif jenis.lower() == 'name':
		return driver.find_element_by_name(element)
	elif jenis.lower() == 'id':
		return driver.find_element_by_id(element)
	elif jenis.lower() == 'class':
		return driver.find_element_by_class_name(element)
	elif jenis.lower() == 'css':
		return driver.find_element_by_css_selector(element)
	else:
		print("Error Find Script !!!")
		exit()
def frame(name):
	driver.switch_to.frame(name)

def exec_js(jscode):
	driver.execute_script(jscode)

def close_driver():
	driver.close()