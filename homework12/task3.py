from atf.ui import *
from atf import *


class AuthOnline(Region):
    login_inp = TextField(By.CSS_SELECTOR, '[name="Login"]', 'логин')
    password_inp = TextField(By.CSS_SELECTOR, '[name="Password"]', 'пароль')


class TaskOnline(Region):
    executor_field = Element(By.CSS_SELECTOR, '.controls-SelectedCollection__item__caption-wrapper', 'поле "Исполнитель"')
    description_field = Element(By.CSS_SELECTOR, '[name="editorWrapper"]', 'поле "Описание"')
    author_field = Element(By.CSS_SELECTOR, '.edo3-Sticker__mainRow-container.edo3-Sticker--withoutPhoto', 'поле "Автор"')
    date_field = Element(By.CSS_SELECTOR, '.edo3-DateNumber', 'Поле " Дата и Номер')


class Test(TestCaseUI):
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

        log('Открыть эталонную задачу по прямой ссылке в новой вкладке браузера')
        my_task = self.config.get('MY TASK')
        self.browser.open(my_task)

        log('Убедиться, что в заголовке вкладки отображаются эталонные значения даты и номера ')
        self.browser.should_be(TitleExact('Задача №3 от 26.06.23'))

        log('Проверить, что поля: Исполнитель, дата, номер, описание и автор отображаются с эталонными значениями')
        executor = TaskOnline(self.driver)
        executor.executor_field.should_be(ExactText('Восточный Б.'))
        description = TaskOnline(self.driver)
        description.description_field.should_be(ExactText('Убрать танк из ворот цирка. Срочно!'))
        author = TaskOnline(self.driver)
        author.author_field.should_be(ExactText('Лисичкина А.А.'))
        date = TaskOnline(self.driver)
        date.date_field.should_be(ExactText('26 июн, пн'))
        


















