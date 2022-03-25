
import threading
import random
from selenium.webdriver.common.by import By
from selenium import webdriver
import smtplib              
from email.mime.text      import MIMEText

#########################user information##################### You can add your information!
from_email = #from_email
to_email = #to_email
password = #password
##############################################################

########################for mailing###########################
def sendmail(new_items):
    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    s.login(from_email , password)
    img_list = ""
    for i in new_items:
        img_list = img_list + f"<img src=\"{str(i)}\">"
    msg = MIMEText(f'New Freitag Arrived! <br> {img_list} <br> <a href="https://www.freitag.ch/en/f14">GO TO FRIETAG</a>' ,_subtype='html', _charset='utf-8')
    msg['Subject'] = 'New Freitag Arrived!'
    s.sendmail(from_email, to_email, msg.as_string())
    s.quit()
###############################################################

#######################get new items###########################
def get_new_items():
    driver.refresh()
    try:
        driver.find_element(By.CSS_SELECTOR, 'body > div:nth-child(10) > div > div > div:nth-child(2) > a').click()
    except:
        pass
    new_items = []
    for item in driver.find_elements(By.CLASS_NAME,'w-full'):
        image_src = item.get_attribute('src')
        if image_src not in curr_items:
            new_items.append(image_src)
            curr_items.append(image_src)
    return new_items
###############################################################

######################call func################################
def call():
    new_items = get_new_items()
    print('called')
    if new_items:
        print('Something new!')
        sendmail(new_items)
    else:
        print('Nothing New')

    threading.Timer(random.uniform(30.0000000,60.0000000), call).start()
###################################################################


if __name__ == "__main__":

    options = webdriver.ChromeOptions()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    driver = webdriver.Chrome(options=options)
    url = 'https://www.freitag.ch/en/f14'
    driver.get(url)
    try:
        driver.find_element(By.CSS_SELECTOR, 'body > div:nth-child(10) > div > div > div:nth-child(2) > a').click()
    except:
        pass
    curr_items = []
    call()