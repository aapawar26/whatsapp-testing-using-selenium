from selenium import webdriver
driver = webdriver.Chrome()

driver.get('https://web.whatsapp.com/')

name = input("Name : ")
user = driver.find_element_by_xpath('//span[@title = "{}"]'.format(name))
user.click()

message = input("Message : ")


count = int(input("Count : "))

for i in range(count):
	msgbox = driver.find_element_by_class_name('_13mgZ')
	msgbox.send_keys(message)
	send = driver.find_element_by_class_name('_3M-N-') 
	send.click()	

