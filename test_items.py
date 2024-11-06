from selenium.webdriver.common.by import By

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_should_see_button_add_to_basket(browser):
    """
    Для первой проверки необходимо:
     - Выполнить к командной строке(терминале): 'pytest --language=es test_items.py'
    Для второй проверки необходимо:
     - добавить строку 'time.sleep(30)' сразу после строки 'browser.get(link)'
     - добавить импорт модуля time 'import time'
     - Выполнить к командной строке(терминале): 'pytest --language=fr test_items.py'
    """
    browser.get(link)
    button = browser.find_elements(By.CSS_SELECTOR, ".btn-add-to-basket")
    assert len(button) > 0, "The button 'Add to basket' is not displayed on the page"
