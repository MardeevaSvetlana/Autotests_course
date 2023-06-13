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
    assert contact_btn.text == button_txt
    assert contact_btn.get_attribute('text') == button_txt
    assert contact_btn.is_displayed(), 'Элемент не отображается'

    print('Перейти на страницу "Контакты"')
    contact_btn.click()
    driver.switch_to.window(driver.window_handles[0])

    print('Проверить URL и заголовок страницы')
    assert 'https://sbis.ru/contacts' in driver.current_url, 'Неверный URL'
    assert driver.title == 'СБИС Контакты — Новосибирская область', 'Неверный заголовок страницы'

    print('Проверить атрибут и видимость баннера "Тензор"')
    tensor_txt = 'Тензор'
    tensor_btn = driver.find_element(By.CSS_SELECTOR, '[title="tensor.ru"]')
    assert tensor_btn.get_attribute('title') == 'tensor.ru'
    assert tensor_btn.is_displayed(), 'Элемент не отображается'

    print('Перейти на https://tensor.ru/, проверить URL')
    tensor_btn.click()
    driver.switch_to.window(driver.window_handles[1])
    assert driver.current_url == 'https://tensor.ru/', 'Неверный URL'

    print('Проверить, что есть блок новости "Сила в людях"')
    header_news_txt= 'Сила в людях'
    header_news_btn = driver.find_element(By.XPATH, '//*[text()="Сила в людях"]')
    driver.execute_script("arguments[0].scrollIntoView(true);", header_news_btn)  # Скролл до элемента
    assert header_news_btn.text == header_news_txt
    assert header_news_btn.is_displayed(), 'Элемент не отображается'

    print('Найти ссылку "Подробнее", проверить видимость и текст ссылки ')
    more_link_txt = 'Подробнее'
    more_link_btn = driver.find_element(By.CSS_SELECTOR, '.tensor_ru-Index__card-text [href="/about"]')
    assert more_link_btn.text == more_link_txt, 'Неверная ссылка'
    assert more_link_btn.is_displayed(), 'Элемент не отображается'

    print('Перейти в "Подробнее", убедиться, что открывается https://tensor.ru/about')
    more_link_btn.click()
    assert driver.current_url == 'https://tensor.ru/about', 'Неверный URL'

    print('Test passed successfully')

finally:
    driver.quit()
