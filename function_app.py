import azure.functions as func
import os
import sys
import logging
from openai import OpenAI

dir_path = os.path.dirname(os.path.realpath('utils.py'))
sys.path.insert(0, dir_path)

# from utils import extract_attributes
import utils
# import api_key


OPENAI_API_KEY  = ""
model="gpt-4o"
client = OpenAI(api_key=OPENAI_API_KEY)
# client = OpenAI(api_key=api_key.API_KEY)
# model = utils.get_model()


# def extract_attributes(clause_in):

#     prompt = (
#         f"give the '{clause_in}' please infer if the following is covered, General Liability Insurance,"
#         "Automobile Liability Insurance, Workers' Compensation Insurance, Professional Liability Insurance, or any other insurance."
#         "If there is no insurance related information in clause_in the response should be 'did not find any insurance info'\n\n"
        
#         "Format the response as a JSON object with the following structure:\n"
#         "{\n"
#         "    \"insurance_requirements\": {\n"
#         "        \"general_liability\": {\n"
#         "            \"coverage_required\": \"Yes\",\n"
#         "            \"each_occurrence_limit\": \"1000000\",\n"
#         "            \"aggregate_limit\": \"2000000\",\n"
#         "            \"conditional_coverage\": \"true\"\n"
#         "        },\n"
#         "        \"automobile_liability\": {\n"
#         "            \"coverage_required\": \"Yes\",\n"
#         "            \"each_occurrence_limit\": \"1000000\",\n"
#         "            \"aggregate_limit\": \"null\",\n"
#         "            \"conditional_coverage\": \"false\"\n"
#         "        },\n"
#         "        \"workers_compensation\": {\n"
#         "            \"coverage_required\": \"Yes\",\n"
#         "            \"each_occurrence_limit\": \"null\",\n"
#         "            \"aggregate_limit\": \"null\",\n"
#         "            \"conditional_coverage\": \"false\"\n"
#         "        },\n"
#         "        \"professional_liability\": {\n"
#         "            \"coverage_required\": \"false\",\n"
#         "            \"each_occurrence_limit\": \"null\",\n"
#         "            \"aggregate_limit\": \"null\",\n"
#         "            \"conditional_coverage\": \"false\"\n"
#         "        }\n"
#         "    },\n"
#         "    \"additional_insured\": [\n"
#         "        {\n"
#         "            \"entity_name\": \"ABC Company\",\n"
#         "            \"type_of_coverage\": \"General Liability\"\n"
#         "        }\n"
#         "    ]\n"
#         "}\n"
#     )

#     completion = client.chat.completions.create(
#         model=model,
#         messages=[{"role": "user", "content": prompt}],
#         response_format={"type": "json_object"},
#     )
    
#     return completion.choices[0].message.content

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