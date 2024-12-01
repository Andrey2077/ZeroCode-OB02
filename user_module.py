
# 1.Класс `User*:
# Этот класс должен инкапсулировать данные о пользователе:
# ID, имя и уровень доступа ('user' для обычных сотрудников).
#

class User:

    def __init__(self, id, name, is_user):
        self.__id = id
        self.__name = name
        self.__is_user = is_user

    def get_id(self):
        return self.__id

    def get_name(self):
        return self.__name

    def set_id(self, value):
        self.__id = value

    def get_is_user(self):
        return self.__is_user

