from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils import login

def test_inventory():
    driver = webdriver.Chrome()

    time.sleep(1)

    try:
        driver = login(driver)

        time.sleep(2)

        #Agregar al carrito el primer producto
        driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()

        #Validar que el carrito tenga 1 item, esperamos a que el elemento sea visible
        badge = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "shopping_cart_badge")))
        assert badge.text == "1"

        #Accedemos a la pagina de el carrito clickeando el icono
        driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()

        time.sleep(2)

        #Verificamos que item aparece en el carrito
        assert "Sauce Labs Backpack" in driver.page_source, "El producto no se encontro en el carrito"

    except Exception as e:
        print(f"Error en test_inventory_page: {e}")
        raise
    finally:
        driver.quit()

       