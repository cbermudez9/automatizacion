import time
from selenium.webdriver.common.by import By

def primer(driver):
    usname = driver.find_element(By.ID, "user-name")
    usname.send_keys("standard_user")
    time.sleep(2)

    passw = driver.find_element(By.ID, "password")
    passw.send_keys("secret_sauce")
    time.sleep(2)

    login = driver.find_element(By.ID, "login-button")
    login.click()
    time.sleep(5)

    add = driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack")
    add.click()
    time.sleep(5)

    shoping = driver.find_element(By.ID, "shopping_cart_container")
    shoping.click()
    time.sleep(5)

    chko = driver.find_element(By.ID, "checkout")
    chko.click()
    time.sleep(5)

    fname = driver.find_element(By.ID, "first-name")
    fname.send_keys("Carlos")
    time.sleep(2)

    lname = driver.find_element(By.ID, "last-name")
    lname.send_keys("Rojas")
    time.sleep(2)

    ema = driver.find_element(By.ID, "postal-code")
    ema.send_keys("55600")
    time.sleep(2)

    cont = driver.find_element(By.ID, "continue")
    cont.click()
    time.sleep(3)

    fin = driver.find_element(By.ID, "finish")
    fin.click()
    time.sleep(3)

    bck = driver.find_element(By.ID, "back-to-products")
    bck.click()
    time.sleep(2)

    burg = driver.find_element(By.ID, "react-burger-menu-btn")
    burg.click()
    time.sleep(2)

    logout = driver.find_element(By.ID, "logout_sidebar_link")
    logout.click()
    time.sleep(5)
    driver.close()

