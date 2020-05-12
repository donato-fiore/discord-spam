from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys

print("[1] Bee Movie Script")
print("[2] Never Gonna Give You Up")
print("[3] Shrek Movie Script")
print("[4] Africa Lyrics")
print("[5] Rappin for Jesus")
script = input("Choose Spam Method: ")

driverpath="/bin/chromedriver"
driver = webdriver.Chrome(driverpath)
driver.get('https://discord.com/login')

time.sleep(5)
emailogin = driver.find_element_by_xpath('//*[@id="app-mount"]/div[2]/div/div[2]/div/div/form/div/div/div[1]/div[3]/div[1]/div/input')
emailogin.send_keys('donato.v.fiore@gmail.com')

passlogin = driver.find_element_by_xpath('//*[@id="app-mount"]/div[2]/div/div[2]/div/div/form/div/div/div[1]/div[3]/div[2]/div/input')
passlogin.send_keys('DahQGgHcyk5842K')

driver.find_element_by_xpath('//*[@id="app-mount"]/div[2]/div/div[2]/div/div/form/div/div/div[1]/div[3]/button[2]').click()
time.sleep(25)
driver.find_element_by_xpath('//*[@id="app-mount"]/div[2]/div/div[2]/div/div/div/div[2]/div[1]/nav/div[2]/div/div/a[3]/div/div[2]/div[1]/div').click()

if script == "1":
    f = open('scripts/beemovie.txt', 'r')
elif script == "2":
    f = open('scripts/nevergonna.txt', 'r')
elif script == "3":
    print("No Shrek Script yet")
elif script == "4":
    f = open('scripts/africa.txt', 'r')
elif script == "5":
    f = open('scripts/jesus.txt', 'r')

elem = driver.find_element_by_xpath('//*[@id="app-mount"]/div[2]/div/div[2]/div/div/div/div[2]/div[2]/div[2]/main/form/div/div/div/div[3]/div[2]')

TypeError = False
for line in f:
    try:
        elem = driver.find_element_by_xpath('//*[@id="app-mount"]/div[2]/div/div[2]/div/div/div/div[2]/div[2]/div[2]/main/form/div/div/div/div[3]/div[2]')
        elem.send_keys(line)
        driver.find_element_by_xpath('//*[@id="app-mount"]/div[2]/div/div[2]/div/div/div/div[2]/div[2]/div[2]/main/form/div/div/div/div[3]/div[2]').send_keys(Keys.ENTER)
        time.sleep(2.5)
        print("[+] Message sent: %s" % line)
    except BaseException:
        print("[!] Message not sent: %s" % line)
        break;      