from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

def login(email, password):
	driver = webdriver.Firefox()
	driver.get("https://rose-hulman.campusdish.com/Commerce/Profile/Login.aspx")
	elem = driver.find_element_by_name("PropertiesToSet_UserName")
	elem.send_keys(email)
	elem = driver.find_element_by_name("PropertiesToSet_Password")
	elem.send_keys(password)
	elem.send_keys(Keys.RETURN)

	time.sleep(1)
	driver.get("https://rose-hulman.campusdish.com/Commerce/MyAccount.aspx")
	account_names = driver.find_elements_by_class_name("account-name")
	balances = driver.find_elements_by_class_name("balance")
	account_names_text = [x.text for x in account_names]
	balances_text = [x.text for x in balances]
	dictionary = dict(zip(account_names_text, balances_text))
	
	driver.close()	

	return dictionary