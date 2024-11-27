# 2.Класс `Admin`:
# Этот класс должен наследоваться от класса `User`.
# Добавь дополнительный атрибут уровня доступа, специфичный для администраторов ('admin').
# Класс должен также содержать методы `add_user` и `remove_user`,
# которые позволяют добавлять и удалять пользователей из списка (представь, что это просто список экземпляров `User`).
#

import User
class Admin(User):
    def __init__(self, ID, name, level_of_access, is_admin = True):
        super().__init__(ID, name, level_of_access)
        self.is_admin = is_admin

    def get_is_admin(self):
        return self.is_admin

    def add_user(user):
        User.list_o
