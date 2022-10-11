from selenium import webdriver
from selenium.webdriver.common.keys import Keys

ID="(YOUR ID HERE)"
PASSWORD="(YOUR PASSWORD HERE)"

path="/chromedriver"
driver=webdriver.Chrome(executable_path=path)

driver.get("https://pict.ethdigitalcampus.com/PICT/")

#Login Page
login_id=driver.find_element_by_name("loginid")
login_id.send_keys(ID)                                #Filling id
password=driver.find_element_by_name("password")
password.send_keys(PASSWORD)                          #Filling password
password.send_keys(Keys.ENTER)                        #Click enter to go on next page

#On second page
dashboard=driver.find_element_by_link_text("Dashboard")
dashboard.click()

#On third page
 profile=driver.find_element_by_xpath('/html/body/table/tbody/tr/td/table/tbody/tr[4]/td/style="margin-left:10"/b/font/a')
 profile.click()
