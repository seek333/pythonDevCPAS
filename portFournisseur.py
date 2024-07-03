from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import xml.etree.ElementTree as ET
import json
import csv


varLogin = varPass = 'admin'
page = 1

driver = webdriver.Firefox()
driver.get("http://10.102.124.219")
time.sleep(1)

# inject le login
elem = driver.find_element_by_id("login_username")
elem.send_keys(varLogin)
time.sleep(1)

# inject le mot de passe
elem = driver.find_element_by_id("login_password")
elem.send_keys(varPass)
time.sleep(1)

# appuie sur le submit
driver.find_element_by_xpath("//*[@id='login_lbl_btn_enter']").click()
time.sleep(1)

urlPage = "http://10.102.124.219/events.xml?event_size=30&event_page_nb=" + str(page)
driver.get(urlPage)
nbrTotal = ET.fromstring(driver.page_source).find('FOOTER').get('total_items')
time.sleep(1)

with open('data.csv', 'w', newline='') as csvfile:
    spamwriter = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)

    # boucle de recuperation
    for i in range(int(int(nbrTotal) / 30)):
        urlPage = "http://10.102.124.219/events.xml?event_size=30&event_page_nb=" + str(page)
        driver.get(urlPage)
        pg = driver.page_source
        root = ET.fromstring(pg)
        for event in root.findall('EVENT'):
            print(event.get('time'), event.get('snd_obj_label'))
            spamwriter.writerow([event.get('time'), event.get('snd_obj_label')])
        page += 1
        time.sleep(2)

driver.close()
