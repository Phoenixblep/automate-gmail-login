from selenium import webdriver
import time
import pandas
import csv
from selenium.webdriver.common.keys import Keys
from save_data import adding_data

def main_loop():
    # Open Chrome
    driver = webdriver.Chrome()

    # Maximize The Windows
    driver.maximize_window()

    # Delete All Cookies
    driver.delete_all_cookies()

    # Navigate To Gmail
    driver.get("https://www.gmail.com")

    # Identify The User Email Prompt And Enter The Account Credentials
    driver.find_element_by_id("identifierId").send_keys(open_data._user)
    time.sleep(2)

    # Clicking The Next Button
    driver.find_element_by_xpath('//*[@id="identifierNext"]/div/button/div[2]').click()
    time.sleep(3)

    # Identify The User Password Prompt And Enter The Account Credentials
    driver.find_element_by_name("password").send_keys(open_data._pass)
    time.sleep(3)

    # Clicking The Next Button
    driver.find_element_by_xpath('//*[@id="passwordNext"]/div/button/div[2]').click()
    time.sleep(3)

    # Close The Browser
    driver.close()

with open('credentials.csv') as csvfile:
    data_file = csv.reader(csvfile, delimiter=',')
    next(data_file)
    for data in data_file:
        _data = {
                "_user": data[0],
                "_pass": data[1]
            }
print(_data)
read = pandas.read_csv("credentials.csv")
data_status = read.empty
print(data_status)
try:
    if data_status == False:
        print("[>] Excecuting")

        #main_loop()
        login_status = "[>] Successful"
    else:
        adding_data()
        login_status = "[>] Unsuccessful"

except KeyboardInterrupt:
    print("\n[>] Killing The Program.")
except:
    print("\n[>] An Error Occurred.")