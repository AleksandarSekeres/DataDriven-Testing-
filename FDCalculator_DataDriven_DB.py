import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import Select
import mysql.connector


serv_obj=Service("C:\Drivers\chromedriver_win32\chromedriver.exe")
driver=webdriver.Chrome(service=serv_obj)
driver.implicitly_wait(10)

driver.get("https://www.moneycontrol.com/fixed-income/calculator/state-bank-of-india-sbi/fixed-deposit-calculator-SBI-BSB001.html")
driver.maximize_window()

try:
	con=mysql.connector.connect(host="localhost", port=3306, user="root", passwd="root", database="mydb")
	curs=con.cursor()
	curs.execute("select * from caldata")

	for row in curs:

		#reading data from excel
		pric=row[0]
		rateofinterest=row[1]
		per1= row[2]
		per2= row[3]
		fre= row[4]
		exp_mvalue= row[5]

		# passing data to the app
		driver.find_element(By.XPATH,"//input[@id='principal']").send_keys(pric)
		driver.find_element(By.XPATH,"//input[@id='interest']").send_keys(rateofinterest)
		driver.find_element(By.XPATH,"//input[@id='tenure']").send_keys(per1)
		perioddrp=Select(driver.find_element(By.XPATH,"//select[@id='tenurePeriod']"))

		#validation
		if float(exp_mvalue)== float(act_mvalue):
			print("test passed")
		
		else:
			print("test failed")
		
		driver.find_element(By.XPATH,"//*[@id='fdMatVal']/div[2]/a[2]/img").click()
		time.sleep(2)
	con.close()
except:
	print("connection unsuccesfull)"
driver.close()
