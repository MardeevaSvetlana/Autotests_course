from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from atf import *
from atf.ui import *
from atf import *


sbis_title = 'СБИС — экосистема для бизнеса: учет, управление и коммуникации'


class MainSbisRu(Region):
    tabs = CustomList(By.CSS_SELECTOR, '.sbisru-Header__menu-item', 'Вкладки')
    start_work = Button(By.CSS_SELECTOR, '.sbisru-Button--primary', 'Начать работу')


class AuthOnline(Region):
    login_inp = TextField(By.CSS_SELECTOR, '[name="Login"]', 'логин')
    password_inp = TextField(By.CSS_SELECTOR, '[name="Password"]', 'пароль')


class MainOnline(Region):
    news_title = CustomList(By.CSS_SELECTOR, '.feed-Title', 'Заголовки новостей')
    popup_menu = Element(By.CSS_SELECTOR, '[templatename="Controls/menu:Popup"', 'Меню')




class Test(TestCaseUI):

    def test(self):
        sbis_site = self.config.get('SBIS_SITE')
        self.browser.open(sbis_site)
        log('Проверить адрес сайта и заголовок страницы')
        self.browser.should_be(UrlExact(sbis_site), TitleExact(sbis_title))

        log('Проверить отображение четырех вкладок')
        sbis_ru = MainSbisRu(self.driver)
        sbis_ru.tabs.should_be(CountElements(4))
        assert_that(lambda: sbis_ru.tabs.count_elements, equal_to(4), 'Неверное количество табов', and_wait())

        log('Проверить текст, атрибут и видимость кнопки Начать работу')
        button_txt = 'Начать работу'
        sbis_ru.start_work.should_be(ExactText(button_txt), Attribute(title=button_txt))

        log('Перейти на страницу авторизации')
        self.browser.switch_to_new_window(sbis_ru.start_work.click)

        log('Проверить адрес сайта и заголовок страницы')
        self.browser.should_be(UrlContains('fix-online.sbis.ru'), TitleExact('Вход в личный кабинет'))

        log('Авторизоваться')
        user_login, user_password = 'lisa_alisa', 'qazwsx123'
        auth = AuthOnline(self.driver)
        auth.login_inp.type_in(user_login + Keys.ENTER).should_be(ExactText(user_login))
        auth.password_inp.type_in(user_password + Keys.ENTER).should_be(Not(Visible))

        log('Навести курсор на новость и сделать контекстный клик')
        main_online = MainOnline(self.driver)
        main_online.news_title.item(3).scroll_into_view().context_click()

        log('Проверить отображение контектсного меню')
        main_online.popup_menu.should_be(Visible)

        # assert_that(1, equal_to(2), 'Неверное кол-во')






