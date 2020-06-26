"""
    Модуль для парсинга OpenGraph
"""
import libxml2


class OpengraphParser:
    """
        Класс для парсинга Opengraph
        Пока знает только namespace og. Далее возможно расширение
        до twitter, vk и т.д.
    """
    PROTOCOL_TUPLE = ('og',)
    SEPARATOR = ':'

    def __init__(self, body: str):
        """
            Конструктор на вход принимает html content
        """
        self.body = body

    def _get_root(self, encoding='utf8'):
        parse_options = libxml2.HTML_PARSE_RECOVER + \
            libxml2.HTML_PARSE_NOERROR + \
            libxml2.HTML_PARSE_NOWARNING
        return libxml2.htmlReadDoc(self.body, '', encoding, parse_options)

    def get_data(self):
        """
            Метод получения данных Opengraph в виде словаря
        """
        root = self._get_root()
        result = {}
        for node in root.xpathEval('//meta'):
            ns_property = node.prop('property')
            content = node.prop('content')
            if not ns_property:
                continue
            ns_property_list = ns_property.split(OpengraphParser.SEPARATOR)
            protocol = ns_property_list[0]
            if protocol not in OpengraphParser.PROTOCOL_TUPLE:
                continue
            if protocol not in result:
                result[protocol] = {}
            dict_key = OpengraphParser.SEPARATOR.join(ns_property_list[1:])
            result[protocol][dict_key] = content
        return result
