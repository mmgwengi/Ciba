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

@app.route(route="clauseciba_func", methods=["GET", "POST"])
def clauseciba_func(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    clause = str(req.params.get('clause'))
    if not clause:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            clause = req_body.get('clause')

    if clause:
        return func.HttpResponse(f"{utils.extract_insurance_info(clause)}")
    else:
        return func.HttpResponse(
             "Missing required parameters. 'clause' is required.",
            status_code=400
        )
