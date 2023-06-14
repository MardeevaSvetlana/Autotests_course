# Перейти на https://sbis.ru/
# Перейти в раздел "Контакты"
# Найти баннер Тензор, кликнуть по нему
# Перейти на https://tensor.ru/
# Проверить, что есть блок новости "Сила в людях"
# Перейдите в этом блоке в "Подробнее" и убедитесь, что открывается https://tensor.ru/about
# Для сдачи задания пришлите код и запись с экрана прохождения теста


from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()


try:
    print('Перейти на https://sbis.ru/')
    sbis_site = 'https://sbis.ru/'
    sbis_title = 'СБИС — экосистема для бизнеса: учет, управление и коммуникации'
    driver.get(sbis_site)
    sleep(1)  # ждем загрузки

    print('Проверить адрес сайта и заголовок страницы')
    assert driver.current_url == sbis_site, 'Неверный адрес сайта'
    assert driver.title == sbis_title, 'Неверный заголовок сайта'

    print('Проверить текст, атрибут и видимость кнопки "Контакты"')
    button_txt = 'Контакты'
    contact_btn = driver.find_element(By.XPATH, '//*[text()="Контакты"]')
    assert contact_btn.is_displayed(), 'Элемент не отображается'
    assert contact_btn.text == button_txt
    assert contact_btn.get_attribute('text') == button_txt

    print('Перейти на страницу "Контакты"')
    contact_btn.click()
    driver.switch_to.window(driver.window_handles[0])
    sleep(3)  # ожидаем загрузки
    assert 'https://sbis.ru/contacts' in driver.current_url, 'Неверный URL'

    print('Проверить атрибут и видимость баннера "Тензор"')
    tensor_txt = 'Тензор'
    tensor_btn = driver.find_element(By.CSS_SELECTOR, '[title="tensor.ru"]')
    assert tensor_btn.get_attribute('title') == 'tensor.ru'
    assert tensor_btn.is_displayed(), 'Элемент не отображается'

    print('Перейти на https://tensor.ru/, проверить URL')
    tensor_btn.click()
    sleep(3)  # ожидаем загрузки
    driver.switch_to.window(driver.window_handles[1])
    assert driver.current_url == 'https://tensor.ru/', 'Неверный URL'

    print('Проверить, что есть блок новости "Сила в людях"')
    header_news_txt= 'Сила в людях'
    header_news_btn = driver.find_element(By.XPATH, '//*[text()="Сила в людях"]')
    property(header_news_btn.location_once_scrolled_into_view)  # скролл до элемента
    assert header_news_btn.text == header_news_txt
    assert header_news_btn.is_displayed(), "Элемент не отображается"

    print('Найти ссылку "Подробнее", проверить видимость и текст ссылки ')
    more_link_txt = 'Подробнее'
    more_link_btn = driver.find_element(By.CSS_SELECTOR, '.tensor_ru-Index__card-text [href="/about"]')
    assert more_link_btn.is_displayed(), 'Элемент не отображается'
    assert more_link_btn.text == more_link_txt, 'Неверная ссылка'

    print('Перейти в "Подробнее", убедиться, что открывается https://tensor.ru/about')
    more_link_btn.click()
    sleep(3)  # ожидаем загрузки
    assert driver.current_url == 'https://tensor.ru/about', 'Неверный URL'

    print('Test passed successfully')

finally:
    driver.quit()
