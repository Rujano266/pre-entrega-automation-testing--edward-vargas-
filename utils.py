from selenium.webdriver.common.by import By


def login(driver):
    
    #Realiza el proceso de login en la página de Sauce Demo
    
    driver.get("https://www.saucedemo.com/")

    #Indicamos datos de usuario, contraseña y login

    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()
    return driver
        
