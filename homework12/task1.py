from atf.ui import *
from atf import *


class AuthOnline(Region):
    login_inp = TextField(By.CSS_SELECTOR, '[name="Login"]', 'логин')
    password_inp = TextField(By.CSS_SELECTOR, '[name="Password"]', 'пароль')


class ContactsOnline(Region):
    search_field = TextField(By.CSS_SELECTOR, '.sabyPage-MainLayout__search input', 'строка поиска адресанта')
    msg_field = TextField(By.CSS_SELECTOR, '.textEditor_Viewer__Paragraph', 'поле для ввода текста сообщения')
    send_msg_btn = Element(By.CSS_SELECTOR, '[title="Ответить в последний диалог"]', 'кнопка отправки сообщения')
    del_msg_icon = Element(By.CSS_SELECTOR, '.controls-BaseButton.controls-Button_ghost_xl',
                           'кнопка удаления сообщения')


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

        log('Перейти в реестр Контакты')
        contacts_page = self.config.get('CONTACTS_PAGE')
        contacts_title = self.config.get('CONTACTS_TITLE')
        self.browser.open(contacts_page)

        log('Проверить адрес сайта и заголовок страницы')
        self.browser.should_be(UrlExact(contacts_page), TitleExact(contacts_title))

        log("Отправить сообщение самому себе")
        search = ContactsOnline(self.driver)

        msg = ContactsOnline(self.driver)
        send_msg = ContactsOnline(self.driver)
        search.search_field.type_in('Лисичкина Алиса' + Keys.ENTER, clear_txt=False).should_be\
            (ExactText('Лисичкина Алиса'))
        msg.msg_field.type_in('Привет', clear_txt=False)
        send_msg.send_msg_btn.click()

        log("Убедиться в том, что сообщение появилось в реестре")
        msg.msg_field.element('span').should_be(ExactText('Привет'))

        log('Удалить сообщение и убедиться в том, что удалили')
        del_btn = ContactsOnline(self.driver)
        msg.msg_field.click()
        del_btn.del_msg_icon.click()
        msg.msg_field.element('span').should_not_be(ExactText('Привет'))








