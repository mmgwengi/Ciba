from openai import OpenAI
import os
import sys

dir_path = os.path.dirname(os.path.realpath('utils.py'))
sys.path.insert(0, dir_path)

import keep_api_key



model="gpt-4o"
client = OpenAI(api_key=keep_api_key.API_KEY)


def extract_insurance_info(clause_in):
    prompt = (
        f"Given the following clause: '{clause_in}', please perform the following tasks:"

        "1. Determine if any of the following insurance types are covered:"
            "- General Liability Insurance"
            "- Automobile Liability Insurance"
            "- Workers' Compensation Insurance"
            "- Professional Liability Insurance"

        "2. For each insurance type covered, extract the following information:"
            "- Coverage limit for each occurrence"
            "- Total amount covered"

        "3. Check if there is a person or entity added to an insurance policy, and if so, extract the following:"
            "- Name of the person or entity"
            "- Type of insurance they are added to"

        "If there is no such information in 'clause_in', respond with 'None' for the extracted information. \n\n"
        
        "Format the response as a JSON object with the following structure:\n"
        "{\n"
        "    \"insurance_requirements\": {\n"
        "        \"general_liability\": {\n"
        "            \"coverage_required\": \"Yes\",\n"
        "            \"each_occurrence_limit\": \"1000000\",\n"
        "            \"aggregate_limit\": \"2000000\",\n"
        "            \"conditional_coverage\": \"Yes\"\n"
        "        },\n"
        "        \"automobile_liability\": {\n"
        "            \"coverage_required\": \"Yes\",\n"
        "            \"each_occurrence_limit\": \"1000000\",\n"
        "            \"aggregate_limit\": \"null\",\n"
        "            \"conditional_coverage\": \"No\"\n"
        "        },\n"
        "        \"workers_compensation\": {\n"
        "            \"coverage_required\": \"Yes\",\n"
        "            \"each_occurrence_limit\": \"null\",\n"
        "            \"aggregate_limit\": \"null\",\n"
        "            \"conditional_coverage\": \"No\"\n"
        "        },\n"
        "        \"professional_liability\": {\n"
        "            \"coverage_required\": \"No\",\n"
        "            \"each_occurrence_limit\": \"null\",\n"
        "            \"aggregate_limit\": \"null\",\n"
        "            \"conditional_coverage\": \"Yes\"\n"
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