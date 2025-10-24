from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from utils import login

def test_login():
    driver = webdriver.Chrome()

    time.sleep(1)

    try:
        driver = login(driver)

        time.sleep(2)

        assert "/inventory.html" in driver.current_url, "No se redirigio correctamente al inventario"

        print("Login exitoso y validado correctamente")

    except Exception as e:
        print(f"Error en test_login: {e}")
        raise
    finally:
        driver.quit()

