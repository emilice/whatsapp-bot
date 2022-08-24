from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

options=webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-logging"])
driver=webdriver.Chrome( options=options)

driver.get(f"https://web.whatsapp.com")

def reps():
    print("Do you want to send more msg  to anyone")
    askUser=input("Press y for Yes and n for No : ")
    if (askUser == 'Y' or askUser == 'y'):
        msg()
    elif (askUser == 'N' or askUser == 'n'):
        print("Thank you see you soon")
        driver.quit()
    else:
        print("Please enter valid option :\n")
        reps() 

def msg():   
    name=input('\nEnter Grup/User Name: ')
    #msg_input=input('Enter your message to group/user: ')
    msg_input=f'Hi {name},\nSize daha sonra döneceğim'
    try:
        count_input=int(input('Enter the message count: '))
        timing_in_min = int(input("Enter the time in min after which you want to send your message: "))
        timing = (timing_in_min)*60

        user = driver.find_element(By.XPATH, '//span[@title = "{}"]'.format(name))
        user.click()
    except:
        msg()
    sleep(timing)
    text_input=driver.find_element(By.CLASS_NAME, 'p3_M1')

    #send button
    for i in range(0, count_input):
        text_input.send_keys(msg_input)
        driver.find_element(By.CLASS_NAME, 'tvf2evcx').click()
    reps()
msg()
