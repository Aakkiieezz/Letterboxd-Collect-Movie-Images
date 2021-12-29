import time
import math
import requests
from PIL import Image
from io import BytesIO
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
    time.sleep(2)
    driver.find_element_by_id("signin-username").send_keys("YourUserName")
    driver.find_element_by_id("signin-password").send_keys("YourPassword")
    driver.find_element_by_class_name("button-container").click()

    time.sleep(2)

    # Navigate to home page
    WebDriverWait(driver,10).until(EC.presence_of_element_located((By.LINK_TEXT,"FILMS"))).click()
    WebDriverWait(driver,10).until(EC.presence_of_element_located((By.LINK_TEXT,"MORE"))).click()
    WebDriverWait(driver,10).until(EC.presence_of_element_located((By.LINK_TEXT,"Large"))).click()
    MoviesFrom=int(input("SET PROPERLY"))
    driver.maximize_window()
     
    # For Downloading Images
    MoviesFrom=int(input("Download From : "))
    MoviesUpto=int(input("Download Upto : "))
    TotalMovies=(MoviesUpto-MoviesFrom)+1
    Movie_columns=int(input("How many movie images you want in a row ? : "))
    Margin=int(input("Margin Pixel Size ? : "))
    Movie_rows=math.ceil(TotalMovies/Movie_columns)
    Movies_inserted_in_row=0
    BackgroundImage=Image.new(mode='RGB',size=((Movie_columns*(300+Margin))+Margin,(Movie_rows*(450+Margin))+Margin),color=(12,44,68))
    Insert_x_Cordinate=Margin
    Insert_y_Cordinate=Margin
    print("Created an background image of size ",BackgroundImage.size)
    CurrentPage=1
    CurrentPage=navigate(CurrentPage,math.ceil(MoviesFrom/18))

    # For getting url of next image
    for movie in range(MoviesFrom,MoviesUpto+1):
        pic=movie%18
        if(not pic):
            pic=18
        img_xpath='//*[@id="films-browser-list-container"]/ul/li[' + str(pic) + ']/div/div/img'
        img_path=WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,img_xpath)))
        img_url=img_path.get_attribute('srcset')

        # For pasting the image in the final image
        response=requests.get(img_url)
        img=Image.open(BytesIO(response.content))
        BackgroundImage.paste(img,(Insert_x_Cordinate,Insert_y_Cordinate))
        print("Movie image ",movie," done")
        Movies_inserted_in_row+=1
        Insert_x_Cordinate+=300+Margin
        if(Movies_inserted_in_row==Movie_columns):
            Insert_x_Cordinate=Margin
            Insert_y_Cordinate+=450+Margin
            Movies_inserted_in_row=0

        # For going to next page
        if(not(pic%18) and movie!=865):
            CurrentPage=CurrentPage+1
            linkText=WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.CLASS_NAME,"next")))
            driver.execute_script("arguments[0].click();",linkText)
            print("Gone to next page")
        
    BackgroundImage.save('FINAL.jpg')
