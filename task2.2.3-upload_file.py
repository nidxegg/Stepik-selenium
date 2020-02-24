'''
Открыть страницу http://suninjuly.github.io/file_input.html
Заполнить текстовые поля: имя, фамилия, email
Загрузить файл. Файл должен иметь расширение .txt и может быть пустым
Нажать кнопку "Submit".
'''
from selenium import webdriver
from os import path

browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/file_input.html")

for selector, keys in {'[name = "firstname"]':"Максим", '[name = "lastname"]':"Курбанов", '[name = "email"]':"ru@ru.ru", '[id = "file"]':path.join(path.dirname(__file__), 'test.txt')}.items():
    browser.find_element_by_css_selector(selector).send_keys(keys)
browser.find_element_by_css_selector(".btn").click()

