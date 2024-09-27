# Insurance Information Extraction from Legal Clauses

This repository is designed to extract insurance-related information from legal clauses using AI techniques. Specifically, it employs gpt-4o and chain-of-thought prompting to accurately and efficiently extract the necessary information. The gpt-4o model is utilized in JSON mode to format results in the expected manner.

## Prerequisites

To run this project locally, you will need:
1. An OpenAI API key.
2. Required libraries installed via the provided requirements file.

## Setup Instructions

### Step 1: Obtain OpenAI API Key
You must have an OpenAI API key to access GPT-4o. If you don't have one, you can request it from OpenAI's website.

### Step 2: Create keep_api_key.py
Save keep_api_key.py with the following content
API_KEY = "your-open-ai-key"


### Step 3: Install Required Libraries
Run the following command in your terminal to install all necessary dependencies:

py -m pip install -r requirements.txt

### Step 4: Use Ciba Exercise Notebook
Use the Ciba exercise notebook (Ciba exercise.ipynb) provided in the repository to execute extract_insurance_info() function, which can be found in utils.py, and extract insurance information.
Relevant data can be found in _clauses - clauses.csv_

## Access Endpoint
You can use Postman to test the Azure Function endpoint.
Here is the URL to access the endpoint: https://funcapp-clauseciba.azurewebsites.net/api/clauseciba_func?code=KitK0fOm2MM9EizkVkQtzexVjCB6Zi6qemp-SfgwoDs1AzFubvrX6Q%3D%3D&clause=

Refer to the image below for an example input:
![image](https://github.com/user-attachments/assets/2bb0a899-c96a-4547-b49a-994cbd219c05)


## Productionizing

A few things to consider to move this project to production:

1. **Data Storage:**
   - Store the extracted data in a datalake such as Azure Blob Storage.

2. **Security:**
   - Use Azure Key Vault to securely manage and store sensitive information, including your OpenAI API key.
   - Utilize Azure OpenAI Service for enhanced security features.

3. **Error Handling:**
   - Implement comprehensive error handling to manage potential disruptions and ensure smooth operation.
  
4. **Context Window**
   - Add summarization in the event of context window limitation

### Areas for Improvement

#### Guide Rails and Edge Cases
- Consider adding guide rails to improve accuracy and robustness.
- Evaluate and address potential edge cases to enhance extraction performance.
#### To Validate Results

##### Steps

1. **Convert JSON Output to DataFrame**
    - Transform the JSON output received from gpt-4o into a DataFrame for easier manipulation and analysis.

2. **Get Relevant Columns from Original Dataset**
    - Extract the necessary columns from the original dataset that correspond to the information extracted by gpt-4o.

3. **Align Column Names**
    - Ensure that the columns in both the extracted DataFrame and the original dataset have identical names. This facilitates direct comparison and validation.

4. **Standardize Columns**
    - Standardize the data in the columns for consistency. For example, some dollar amounts may include a '$' symbol while others do not.
