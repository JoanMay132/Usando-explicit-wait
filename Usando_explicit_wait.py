'''Hasta que no cargue un componente la página va a comenzar tu automatización. Tu decides en donde lo quieres continuar
    EXPLICIT WAIT'''


import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import WebDriverWait #selenium
from selenium.webdriver.support import expected_conditions as EC #Declaramos una condicion para continuar la automatización

class usando_unittest(unittest.TestCase):
    def setUp(self):
        self.driver= webdriver.Chrome(executable_path=r"D:\Descargas\chromedriver_win32\chromedriver.exe")

    def test_usando_Explicit_Wait(self):
        driver=self.driver
        driver.get("https://www.google.com")
        try:                                            #Haciendo un ciclo
            element= WebDriverWait(driver, 10).until(  #carga elemento y haz 10 intentos
                EC.presence_of_element_located((By.NAME,"q")) #se cargue localizado con el nombre q (GOOGLE ID) hasta que lo encuentre
            )
        finally:                                        #importante cerrar el driver
            driver.quit()

if __name__=='__main__':
    unittest.main()