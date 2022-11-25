from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import WebDriverException
from selenium.common.exceptions import NoSuchWindowException
from selenium.common.exceptions import TimeoutException
import time 

with open("Usernames_Passwords.txt", 'r') as f:
     data = f.readlines()

browser = webdriver.Firefox()

# Opening the website
browser.get('https://todo-list-login.firebaseapp.com/#!')
if browser.title == "Todo App":
	print("Browser Title correct")

#assertEqual("Todo App", browser.title):
#assert "Todo App" in browser.title


WebDriverWait(browser, 5).until(EC.presence_of_element_located((By.CLASS_NAME,"btn-github")))

# Find the if already sign in
def checkiflogin():
	try:
		elem = browser.find_element(By.CLASS_NAME,"btn-github")
		if elem.is_displayed():
			WebDriverWait(browser, 2).until(EC.presence_of_element_located((By.CLASS_NAME,"btn-github")))
			browser.find_element(By.CLASS_NAME,"btn-github").click()
			browser.implicitly_wait(2)
			if len(browser.window_handles) > 1:
				main_window = browser.window_handles[0]
				login = browser.window_handles[1]
				browser.switch_to.window(login)

				#Check for Login and password text box
				try:
					elem = browser.find_element(By.CLASS_NAME,"js-login-field")
					if elem.is_displayed():
						WebDriverWait(browser, 4).until(EC.presence_of_element_located((By.CLASS_NAME,"js-login-field")))
						WebDriverWait(browser, 4).until(EC.visibility_of_element_located((By.CLASS_NAME,"js-login-field")))
						browser.find_element(By.CLASS_NAME,"js-login-field").send_keys(data[0][9:-1])
						WebDriverWait(browser, 1).until(EC.presence_of_element_located((By.CLASS_NAME,"js-password-field")))
						WebDriverWait(browser, 1).until(EC.visibility_of_element_located((By.CLASS_NAME,"js-password-field")))
						browser.find_element(By.CLASS_NAME,"js-password-field").send_keys(data[1][9:-1])
						browser.find_element(By.CLASS_NAME,"js-sign-in-button").click()
				except (NoSuchElementException, NoSuchWindowException, WebDriverException, TimeoutException):
					pass

				#Check if authorize request is required
				try:
					elem = browser.find_element(By.CLASS_NAME,"btn-primary")
					if elem.is_displayed():
						WebDriverWait(browser, 5).until(EC.visibility_of_element_located((By.CLASS_NAME,"btn-primary")))
						WebDriverWait(browser, 2).until(EC.element_to_be_clickable((By.CLASS_NAME,"btn-primary")))
						browser.find_element(By.CLASS_NAME,"btn-primary").click()
				except (NoSuchElementException, NoSuchWindowException, WebDriverException):
					pass

			browser.switch_to.window(main_window)
	except NoSuchElementException:
		pass

def enterrandomstring():
	WebDriverWait(browser, 5).until(EC.visibility_of_element_located((By.XPATH,"/html/body/ng-view/div/div[2]/div[1]/input")))
	WebDriverWait(browser, 1).until(EC.element_to_be_clickable((By.XPATH,"/html/body/ng-view/div/div[2]/div[2]/button")))
	browser.find_element(By.XPATH,"/html/body/ng-view/div/div[2]/div[1]/input").send_keys("Il24STrhua")
	browser.find_element(By.XPATH,"/html/body/ng-view/div/div[2]/div[2]/button").click()
	browser.find_element(By.XPATH,"/html/body/ng-view/div/div[2]/div[1]/input").send_keys("GxKB5fzUQZ")
	browser.find_element(By.XPATH,"/html/body/ng-view/div/div[2]/div[2]/button").click()
	browser.find_element(By.XPATH,"/html/body/ng-view/div/div[2]/div[1]/input").send_keys("eaM7k2eit6")
	browser.find_element(By.XPATH,"/html/body/ng-view/div/div[2]/div[2]/button").click()
	browser.find_element(By.XPATH,"/html/body/ng-view/div/div[2]/div[1]/input").send_keys("Nib3dIkfSB")
	browser.find_element(By.XPATH,"/html/body/ng-view/div/div[2]/div[2]/button").click()
	browser.find_element(By.XPATH,"/html/body/ng-view/div/div[2]/div[1]/input").send_keys("Ue6J39E07K")
	browser.find_element(By.XPATH,"/html/body/ng-view/div/div[2]/div[2]/button").click()
	WebDriverWait(browser, 5).until(EC.visibility_of_element_located((By.XPATH,"/html/body/ng-view/div/nav/div/div/a")))
	WebDriverWait(browser, 1).until(EC.element_to_be_clickable((By.XPATH,"/html/body/ng-view/div/nav/div/div/a")))
	browser.find_element(By.XPATH,"/html/body/ng-view/div/nav/div/div/a").click()
	
def deleteallrandomstring():
	WebDriverWait(browser, 5).until(EC.visibility_of_element_located((By.CSS_SELECTOR,"button.btn:nth-child(1)")))
	try:
		while browser.find_element(By.CSS_SELECTOR,"li.list-group-item:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(5) > button:nth-child(1)").is_displayed():
			browser.find_element(By.CSS_SELECTOR,"li.list-group-item:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(5) > button:nth-child(1)").click()
	except NoSuchElementException:
		pass
	WebDriverWait(browser, 5).until(EC.visibility_of_element_located((By.XPATH,"/html/body/ng-view/div/nav/div/div/a")))
	WebDriverWait(browser, 1).until(EC.element_to_be_clickable((By.XPATH,"/html/body/ng-view/div/nav/div/div/a")))
	browser.find_element(By.XPATH,"/html/body/ng-view/div/nav/div/div/a").click()

# Click sign in github
checkiflogin()

# Add List 1-10 with random strings
count=1
while count <= 10:
	WebDriverWait(browser, 5).until(EC.presence_of_element_located((By.CLASS_NAME,"btn-success")))
	browser.find_element(By.XPATH,"/html/body/ng-view/div/div[2]/div[1]/input").send_keys(f"{count}")
	browser.find_element(By.CLASS_NAME,"btn-success").click()
	WebDriverWait(browser, 5).until(EC.visibility_of_element_located((By.XPATH,f"/html/body/ng-view/div/div[3]/div/ul/li[{count}]/div/div[1]/a")))
	WebDriverWait(browser, 2).until(EC.element_to_be_clickable((By.XPATH,f"/html/body/ng-view/div/div[3]/div/ul/li[{count}]/div/div[1]/a")))
	browser.find_element(By.XPATH,f"/html/body/ng-view/div/div[3]/div/ul/li[{count}]/div/div[1]/a").click()
	enterrandomstring()
	checkiflogin()
	count+=1
	
# Logout
WebDriverWait(browser, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR,"button.btn:nth-child(2)")))
browser.find_element(By.CSS_SELECTOR,"button.btn:nth-child(2)").click()

# Click sign in github
checkiflogin()

# Delete List 5-10 and all random strings
count2=10
while count2 >= 5:
	WebDriverWait(browser, 5).until(EC.element_to_be_clickable((By.XPATH,f"/html/body/ng-view/div/div[3]/div/ul/li[{count2}]/div/div[1]/a")))
	browser.find_element(By.XPATH,f"/html/body/ng-view/div/div[3]/div/ul/li[{count2}]/div/div[1]/a").click()
	deleteallrandomstring()
	checkiflogin()
	WebDriverWait(browser, 5).until(EC.element_to_be_clickable((By.XPATH,f"/html/body/ng-view/div/div[3]/div/ul/li[{count2}]/div/div[2]/button")))
	browser.find_element(By.XPATH,f"/html/body/ng-view/div/div[3]/div/ul/li[{count2}]/div/div[2]/button").click()
	count2 -= 1
	
# Logout
WebDriverWait(browser, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR,"button.btn:nth-child(2)")))
browser.find_element(By.CSS_SELECTOR,"button.btn:nth-child(2)").click()
browser.implicitly_wait(4) # seconds
browser.quit()
print("Testing completed")