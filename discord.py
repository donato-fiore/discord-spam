import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

print("[1] Bee Movie Script")
print("[2] Never Gonna Give You Up")
print("[3] Shrek Movie Script")
print("[4] Africa Lyrics")
print("[5] Rappin for Jesus")
print("[6] bbboob, bbgif, bbass")
script = input("Choose Spam Method: ")

driverpath="/bin/chromedriver"
driver = webdriver.Chrome(driverpath)
driver.get('https://discord.com/login')

time.sleep(5)
emailogin = driver.find_element_by_xpath('//*[@id="app-mount"]/div[2]/div/div[2]/div/div/form/div/div/div[1]/div[3]/div[1]/div/input')
emailogin.send_keys('EMAIL')

passlogin = driver.find_element_by_xpath('//*[@id="app-mount"]/div[2]/div/div[2]/div/div/form/div/div/div[1]/div[3]/div[2]/div/input')
passlogin.send_keys('PASSWORD')

driver.find_element_by_xpath('//*[@id="app-mount"]/div[2]/div/div[2]/div/div/form/div/div/div[1]/div[3]/button[2]').click()

channel = str('https://discord.com/channels/711349040469508147/712189660528640040')

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
elif script == "6":
    f = open('scripts/bb.txt', 'r')
    channel = str('https://discord.com/channels/711349040469508147/711350457792200797')

time.sleep(25)
driver.get(channel)
time.sleep(5)

time.sleep(30)
elem = driver.find_element_by_xpath('//*[@id="app-mount"]/div[2]/div/div[2]/div/div/div/div[2]/div[2]/div/main/form/div/div/div/div/div[3]/div[1]')

TypeError = False

for line in f:
    try:
        actions = ActionChains(driver)
        actions.send_keys(line, Keys.ENTER)
        actions.perform()
        print("[+] Message sent: %s" % line)
    except BaseException:
        print("[!] Message not sent: %s" % line)
