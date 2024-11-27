
# 1.Класс `User*:
# Этот класс должен инкапсулировать данные о пользователе:
# ID, имя и уровень доступа ('user' для обычных сотрудников).
#

class User():

    list_of_users = []
    def __init__(self, id, name, is_user=True):
        self.__id = id
        self.name = name
        self.is_user = is_user

    def get_id(self):
        return self.id

    def set_id(self, value):
        self.id = value

    def get_is_user(self):
        return self.get_is_user

