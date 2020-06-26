"""
    Модуль для работы с web
"""

import requests


class Downloader:
    """
        Класс делающий get запрос
        Пока рыба может будет расширяться со скачиванием
        контента различного типа
    """
    @staticmethod
    def read(url: str):
        """
            Делает запрос по url, возвращает код ответа сервера и text
        """
        response = requests.get(url)
        code = response.status_code
        res_content = response.text
        return (code, res_content)
