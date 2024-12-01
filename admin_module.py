# 2.Класс `Admin`:
# Этот класс должен наследоваться от класса `User`.
# Добавь дополнительный атрибут уровня доступа, специфичный для администраторов ('admin').
# Класс должен также содержать методы `add_user` и `remove_user`,
# которые позволяют добавлять и удалять пользователей из списка
# (представь, что это просто список экземпляров `User`).
#

from user_module import User


class Admin(User):
    list_of_users = []

    def __init__(self, id, name, is_user, is_admin):
        super().__init__(id, name, is_user)
        self.is_admin = is_admin

    def get_is_admin(self):
        return self.is_admin

    @staticmethod
    def add_user(user):
        Admin.list_of_users.append(user)

    @staticmethod
    def remove_user(user):
        Admin.list_of_users.remove(user)
