"""
    Модуль для тестирования OpengraphParser
"""

from parser.opengraph import OpengraphParser


def test_opengraph():
    """
        Метод для тестирования простого контента
    """
    body = """
    <html>
    <head>
        <meta property="og:type" content="website">
        <meta property="og:site_name" content="Название сайта">
        <meta property="og:title" content="Заголовок">
        <meta property="og:description" content="Описание.">
        <meta property="og:url" content="http://example.com/page.html">
        <meta property="og:locale" content="ru_RU">
        <meta property="og:image" content="http://example.com/img.jpg">
        <meta property="og:image:width" content="968">
        <meta property="og:image:height" content="504">
    </head>
    """
    parser = OpengraphParser(body)
    parsed_data = parser.get_data()
    assert parsed_data['og']['type'] == 'website'
    assert parsed_data['og']['image:width'] == '968'
