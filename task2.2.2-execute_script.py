'''
Открыть страницу http://SunInJuly.github.io/execute_script.html.
Считать значение для переменной x.
Посчитать математическую функцию от x.
Проскроллить страницу вниз.
Ввести ответ в текстовое поле.
Выбрать checkbox "I'm the robot".
Переключить radiobutton "Robots rule!".
Нажать на кнопку "Submit".
'''
from selenium import webdriver
import math
import time


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


browser = webdriver.Chrome()
link = 'http://suninjuly.github.io/execute_script.html'
try:
    browser.get(link)
    x1 = browser.find_element_by_css_selector('#input_value').text
    y = calc(x1)
    browser.find_element_by_css_selector('#answer').send_keys(y)
    button = browser.find_element_by_css_selector('button[type="submit"]')
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    browser.find_element_by_css_selector('#robotCheckbox').click()
    browser.find_element_by_css_selector('#robotsRule').click()
    button.click()
    time.sleep(1)
    answer = browser.switch_to.alert.text
    print(answer.split()[-1])
finally:
    time.sleep(10)
    browser.quit()
