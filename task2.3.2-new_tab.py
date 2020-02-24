'''
Открыть страницу http://suninjuly.github.io/redirect_accept.html
Нажать на кнопку
Переключиться на новую вкладку
Пройти капчу для робота и получить число-ответ
'''
from selenium import webdriver
import time, math
options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")
browser = webdriver.Chrome(options=options)
try:
    link = "http://suninjuly.github.io/redirect_accept.html"
    browser.get(link)
    button = browser.find_element_by_class_name("trollface")
    button.click()
    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)
    x = int(browser.find_element_by_id('input_value').text)
    input1 = browser.find_element_by_id("answer")
    input1.send_keys(str(math.log(abs(12*math.sin(x)))))
    button = browser.find_element_by_class_name("btn")
    button.click()
    alert = browser.switch_to_alert()
    print(alert.text)
    alert.accept()
finally:
    time.sleep(5)
    browser.quit()