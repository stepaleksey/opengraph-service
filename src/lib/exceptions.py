"""
    Модуль для хранения собственных исключений
"""


class ResponseWrongCodeException(Exception):
    """
        Специальный класс исключения, который описывает, что ответ
        при попытке скачивания был не 200
    """
    def __init__(self, message:str, code:int):

        super().__init__(message)
        self.code = code
