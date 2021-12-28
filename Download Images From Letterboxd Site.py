import time
import math
import urllib.request
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# For Navigating to right page
def navigate(CurrentPage,DestinationPage):
    while(CurrentPage!=DestinationPage):
        if(CurrentPage<DestinationPage):
            WebDriverWait(driver,10).until(EC.presence_of_element_located((By.CLASS_NAME,"next"))).click()
            print("Gone to next page")
            CurrentPage+=1
        else:
            WebDriverWait(driver,10).until(EC.presence_of_element_located((By.CLASS_NAME,"previous"))).click()
            print("Gone to previous page")
            CurrentPage-=1
    return CurrentPage

if(__name__ == "__main__"):
    # Opening Website
    driver = webdriver.Chrome('/home/aakkiieezz/Downloaded Drivers/chromedriver') 
    driver.get('https://letterboxd.com/sign-in/')
    driver.find_element_by_id("signin-username").send_keys("AkashKadole")
    driver.find_element_by_id("signin-password").send_keys("Movies")
    driver.find_element_by_class_name("button-container").click()

    time.sleep(2)

    # Navigate to home page
    WebDriverWait(driver,10).until(EC.presence_of_element_located((By.LINK_TEXT,"FILMS"))).click()
    WebDriverWait(driver,10).until(EC.presence_of_element_located((By.LINK_TEXT,"MORE"))).click()
    WebDriverWait(driver,10).until(EC.presence_of_element_located((By.LINK_TEXT,"Large"))).click()
    driver.maximize_window()

    # For Downloading Images
    flag='yes'
    CurrentPage=1
    while(flag=='yes'):
        MoviesFrom=int(input("Download From : "))
        MoviesUpto=int(input("Download Upto : "))
        CurrentPage=navigate(CurrentPage , math.ceil(MoviesFrom/18))

        # For getting url of next image
        for movie in range(MoviesFrom,MoviesUpto+1):
            pic=movie%18
            if(not pic):
                pic=18
            img_xpath='//*[@id="films-browser-list-container"]/ul/li[' + str(pic) + ']/div/div/img'
            img=WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,img_xpath)))
            url=img.get_attribute('srcset')
            headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.183 Safari/537.36'}
            req=urllib.request.Request(url=url[:-3],headers=headers)
            g=urllib.request.urlopen(req)
            img_name='Page-' + str("{:02d}".format(CurrentPage)) + ' Pic-' + str("{:02d}".format(pic)) + '.jpg'

            # For saving the image
            with open(img_name,'b+w') as f:
                f.write(g.read())
                print("Movie image ",movie," done")

            # For going to next page
            if(not(pic%18) and movie!=864):
                CurrentPage=CurrentPage+1
                linkText=WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.CLASS_NAME,"next")))
                driver.execute_script("arguments[0].click();",linkText)
                print("Gone to next page")

        flag=input("Do You Want To Download Again ? : ")