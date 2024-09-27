# Insurance Information Extraction from Legal Clauses

This repository is designed to extract insurance-related information from legal clauses using AI techniques. Specifically, it employs GPT-4o and chain-of-thought prompting to accurately and efficiently extract the necessary information. The gpt-4o model is utilized in JSON mode to format results in the expected manner.

## Prerequisites

To run this project locally, you will need:
1. An OpenAI API key.
2. Required libraries installed via the provided requirements file.

## Setup Instructions

### Step 1: Obtain OpenAI API Key
You must have an OpenAI API key to access GPT-4o. If you don't have one, you can request it from OpenAI's website.

### Step 2: Install Required Libraries
Run the following command in your terminal to install all necessary dependencies:

py -m pip install -r requirements.txt

### Step 3: Use Ciba Exercise Notebook
Use the Ciba exercise notebook provided in the repository to execute the function and extract insurance information.

## Productionizing

A few things to consider to move this project to production:

1. **Data Storage:**
   - Store the extracted data in a datalake such as Azure Blob Storage.

2. **Security:**
   - Use Azure Key Vault to securely manage and store sensitive information, including your OpenAI API key.
   - Utilize Azure OpenAI Service for enhanced security features.

3. **Error Handling:**
   - Implement comprehensive error handling to manage potential disruptions and ensure smooth operation.

## Areas for Improvement

### Guide Rails and Edge Cases
- Consider adding guide rails to improve accuracy and robustness.
- Evaluate and address potential edge cases to enhance extraction performance.
