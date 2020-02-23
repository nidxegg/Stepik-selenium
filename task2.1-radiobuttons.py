'''
Открыть страницу http://suninjuly.github.io/math.html.
Считать значение для переменной x.
Посчитать математическую функцию от x (код для этого приведён ниже).
Ввести ответ в текстовое поле.
Отметить checkbox "I'm the robot".
Выбрать radiobutton "Robots rule!".
Нажать на кнопку Submit.
'''

from selenium import webdriver
import time 
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = " http://suninjuly.github.io/math.html"

try: 
    link = "http://suninjuly.github.io/math.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element_by_xpath('//*[@id="input_value"]')
    x = x_element.text
    y = calc(x)
    input1 = browser.find_element_by_xpath('//*[@id="answer"]')
    input1.send_keys(y)  
    option2 = browser.find_element_by_css_selector(".form-check-label")
    option2.click()
    option1 = browser.find_element_by_xpath('//*[text()="Robots rule"]')
    option1.click()
    
    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()