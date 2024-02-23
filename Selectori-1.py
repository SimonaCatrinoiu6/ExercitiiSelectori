import time

from selenium import webdriver
from selenium.webdriver.common.by import By

try:
    chrome = webdriver.Chrome()  # Obtinem driver-ul Edge din selenium
    # print(type(chrome))
    # Accesam pagina formeProject
    chrome.get("https://formy-project.herokuapp.com/form")
    # Pauzam executia programului pentru 3 secunde
    time.sleep(3)
    # Indentificam campul First Name si il completam
    chrome.find_element(By.ID,"first-name").send_keys("Rares")
    # time.sleep(3)
    # Indentificam campul Last Name si il completam
    chrome.find_element(By.ID,"last-name").send_keys("Seresanu")
    # Folosim metoda find elements pentru a recupera toate campurile/elementele cu clasa form-control
    elements = chrome.find_elements(By.CLASS_NAME,"form-control")
    print(type(elements))
    print(len(elements))
    #print(elements[2].get_attribute("placeholder"))
    # Folosim Send Keys ca sa completam campul job title cu valoarea Tester
    elements[2].send_keys("Tester")
    # Identificam si dam click pe Butonul de Submit folosind Link Text
    chrome.find_element(By.LINK_TEXT,"Submit").click()
    # Maximizam fereastra Driver-ului
    chrome.maximize_window()
    time.sleep(2)
    # Navigam inapoi
    chrome.back()
    time.sleep(2)
    # Identificam si dam click pe Butonul de Submit folosind Partial Link Text
    chrome.find_element(By.PARTIAL_LINK_TEXT,"Subm").click()
    time.sleep(3)
finally:
    # Eliberam driver-ul.
    chrome.quit()
