from selenium import webdriver
import time
import os

link = 'http://suninjuly.github.io/file_input.html'
browser = webdriver.Chrome()
browser.get(link)

try:
    first = browser.find_element_by_css_selector('div.form-group input:nth-child(2)')
    first.send_keys('test')
    last = browser.find_element_by_css_selector('div.form-group input:nth-child(4)')
    last.send_keys('test')
    email = browser.find_element_by_css_selector('div.form-group input:nth-child(6)')
    email.send_keys('test')
    element = browser.find_element_by_id('file')
    current_dir = os.path.abspath(os.path.dirname(__file__))  # получаем путь к директории текущего исполняемого файла
    file_path = os.path.join(current_dir, 'file.txt')  # добавляем к этому пути имя файла
    element.send_keys(file_path)
    button = browser.find_element_by_css_selector('button.btn')
    button.click()


finally:
    time.sleep(10)
    browser.quit()
