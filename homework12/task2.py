
from atf.ui import *
from atf import *

class AuthOnline(Region):
    """ Класс для авторизации"""
    login_inp = TextField(By.CSS_SELECTOR, '[name="Login"]', 'логин')
    password_inp = TextField(By.CSS_SELECTOR, '[name="Password"]', 'пароль')


class Tasks_Online(Region):
    """ Описываем реестр Задачи/Входящие"""
    folder_indox = TextField(By.CSS_SELECTOR, '.controls-FilterEditors__list-item-title', 'папка "Входящие"')
    marker_indox = Element(By.CSS_SELECTOR, '.controls-ListView__itemV_marker.controls-Grid__row-cell__content_baseline_default', 'маркер')
    counter_tasks = TextField(By.CSS_SELECTOR, '[data-qa="controls-EditorList__mainCounter"]', 'счетчик задач')
    another_folder = TextField(By.CSS_SELECTOR, '[title="Другая папка"]', 'другая папка')
    plus_btn = Element(By.CSS_SELECTOR, "[data-name='sabyPage-addButton']", 'создать папку')
    folder_btn = Element(By.XPATH, '//*[text()="Папка"]', 'папка')
    folder_name_field = TextField(By.XPATH, '//*[@id="popup"]/div/div/div[2]/div/div[1]/div/div/input', 'поле ввода')
    save_btn = Element(By.XPATH, '//*[@id="popup"]/div/div/div[1]/div/div/div[2]/span', 'кнопка Сохранить')
    new_folder = TextField(By.XPATH, '//*[text()="Моя новая папка"]', 'новая папка')
    no_tasks = TextField(By.XPATH, '//*[text()="В этой папке нет задач"]', 'нет задач ')
    delete_btn = Element(By.XPATH, '//*[text()="Удалить папку"]', 'кнопка удаления папки')
    yes_btn = Element(By.CSS_SELECTOR, '[data-qa="controls-ConfirmationDialog__button-true"]', 'кнопка подтверждения ')


class Test(TestCaseUI):
    """ Прописываем логику теста с помощью последоватеного вызова методов"""
    def test(self):
        log('Перейти на страницу авторизации')
        sbis_site = self.config.get('SBIS_SITE')
        sbis_title = self.config.get('SBIS_TITLE')
        self.browser.open(sbis_site)

        log('Проверить адрес сайта и заголовок страницы')
        self.browser.should_be(UrlExact(sbis_site), TitleExact(sbis_title))

        log('Авторизоваться')
        user_login = self.config.get('USER_LOGIN')
        user_password = self.config.get('USER_PASSWORD')
        auth = AuthOnline(self.driver)
        auth.login_inp.type_in(user_login + Keys.ENTER).should_be(ExactText(user_login))
        auth.password_inp.type_in(user_password + Keys.ENTER).should_be(Not(Visible))

        log('Перейти в реестр Задачи на вкладку "В работе"')
        tasks_page = self.config.get('TASKS_PAGE')
        self.browser.open(tasks_page)

        log('Убедиться, что выделена папка "Входящие" и стоит маркер')
        tasks = Tasks_Online(self.driver)
        tasks.folder_indox.should_be(Visible), (ExactText("Входящие"))
        tasks.marker_indox.should_be(Visible)

        log('Убедиться, что папка не пустая (в реестре есть задачи)')
        tasks.counter_tasks.should_be(Visible)

        log('Перейти в другую папку, убедиться, что теперь она выделена, а со "Входящие" выделение снято')
        tasks.another_folder.click()
        tasks.marker_indox.should_be(Visible)

        log('Создать новую папку и перейти в неё')
        tasks.plus_btn.should_be(Visible).click()
        tasks.folder_btn.click()
        tasks.folder_name_field.should_be(Visible).click().type_in('Моя новая папка')
        tasks.save_btn.should_be(Visible).click()
        tasks.new_folder.should_be(Visible).click()

        log('Убедиться, что она пустая')
        tasks.no_tasks.should_be(Visible), (ExactText("В этой папке нет задач"))

        log('Удалить новую папку, проверить, что её нет в списке папок')
        tasks.new_folder.mouse_over().context_click()
        tasks.delete_btn.click()
        tasks.yes_btn.should_be(Visible).click()
        tasks.new_folder.should_not_be(Visible)












