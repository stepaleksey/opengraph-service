"""
    Точка входа в приложение от gunicorn
"""

import logging

import sys
import traceback

from parser.opengraph import OpengraphParser

from flask import Flask, jsonify, request

from lib.web import Downloader
from lib.exceptions import ResponseWrongCodeException


app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False


@app.route('/')
def index():
    """
        Базовый route принимает на вход параметр url,
        скачивает и пытается распарсить og заголовки
    """
    url = request.args.get('url', '')
    try:
        (code, content) = Downloader.read(url)
        if code != 200:
            raise ResponseWrongCodeException("Wrong code", code)
        parser = OpengraphParser(content)
        result_data = {
            'error': 0,
            'data': parser.get_data()
        }

    except ResponseWrongCodeException as response_exception:
        error_to_log(response_exception)
        result_data = {
            'error': 1,
        }

    except (Exception, ValueError):
        exc_type, exc_value, exc_traceback = sys.exc_info()
        traceback_string = traceback.format_exception(
            exc_type, exc_value, exc_traceback)
        error_to_log(traceback_string)

        result_data = {
            'error': 1,
        }
    return jsonify(result_data)


def error_to_log(description: str):
    """
        Логгируем ошибку(берем path, параметры и описание ошибки)
    """
    logging.error("PATH-%s-PARAMETERS-%s-%s",
                  request.path, request.args, description)


if __name__ == '__main__':
    app.run(host='0.0.0.0')
