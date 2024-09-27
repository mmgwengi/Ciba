from openai import OpenAI
import os
import sys

dir_path = os.path.dirname(os.path.realpath('utils.py'))
sys.path.insert(0, dir_path)

import keep_api_key


OPENAI_API_KEY  = ""
model="gpt-4o"
client = OpenAI(api_key=keep_api_key.API_KEY)

# OPENAI_API_KEY  = "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"
# model="gpt-4o"
# client = OpenAI(api_key=OPENAI_API_KEY)



def extract_attributes(clause_in):
    prompt = (
        f"give the '{clause_in}' please infer if the following is covered, General Liability Insurance,"
        "Automobile Liability Insurance, Workers' Compensation Insurance, Professional Liability Insurance, or any other insurance."
        "If there is no insurance related information in clause_in the response should be 'did not find any insurance info'\n\n"
        
        "Format the response as a JSON object with the following structure:\n"
        "{\n"
        "    \"insurance_requirements\": {\n"
        "        \"general_liability\": {\n"
        "            \"coverage_required\": \"Yes\",\n"
        "            \"each_occurrence_limit\": \"1000000\",\n"
        "            \"aggregate_limit\": \"2000000\",\n"
        "            \"conditional_coverage\": \"true\"\n"
        "        },\n"
        "        \"automobile_liability\": {\n"
        "            \"coverage_required\": \"Yes\",\n"
        "            \"each_occurrence_limit\": \"1000000\",\n"
        "            \"aggregate_limit\": \"null\",\n"
        "            \"conditional_coverage\": \"false\"\n"
        "        },\n"
        "        \"workers_compensation\": {\n"
        "            \"coverage_required\": \"Yes\",\n"
        "            \"each_occurrence_limit\": \"null\",\n"
        "            \"aggregate_limit\": \"null\",\n"
        "            \"conditional_coverage\": \"false\"\n"
        "        },\n"
        "        \"professional_liability\": {\n"
        "            \"coverage_required\": \"false\",\n"
        "            \"each_occurrence_limit\": \"null\",\n"
        "            \"aggregate_limit\": \"null\",\n"
        "            \"conditional_coverage\": \"false\"\n"
        "        }\n"
        "    },\n"
        "    \"additional_insured\": [\n"
        "        {\n"
        "            \"entity_name\": \"ABC Company\",\n"
        "            \"type_of_coverage\": \"General Liability\"\n"
        "        }\n"
        "    ]\n"
        "}\n"
    )

    completion = client.chat.completions.create(
        model=model,
        messages=[{"role": "user", "content": prompt}],
        response_format={"type": "json_object"},
    )
    
    return completion.choices[0].message.content