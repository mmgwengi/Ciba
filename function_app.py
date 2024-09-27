import azure.functions as func
import os
import sys
import logging
from openai import OpenAI

dir_path = os.path.dirname(os.path.realpath('utils.py'))
sys.path.insert(0, dir_path)


import utils
import keep_api_key

app = func.FunctionApp(http_auth_level=func.AuthLevel.FUNCTION)

@app.route(route="clauseciba_func")
def clauseciba_func(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    name = req.params.get('name')
    if not name:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            name = req_body.get('name')

    if name:
        return func.HttpResponse(f"{utils.extract_attributes(name)}")
    else:
        return func.HttpResponse(
             "something",
             status_code=200
        )