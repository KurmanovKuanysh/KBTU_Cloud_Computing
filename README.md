# TSIS 2 — Judge Agent

This project implements a Judge Agent that evaluates Python code against a Product Requirements Document (PRD).

## Project Files

- `prd.txt` — product requirements
- `agent.txt` — judge agent instructions
- `code_submission.py` — intentionally incomplete code sample
- `code_submission_good.py` — corrected code sample
- `judge.py` — Python script that sends the PRD and code to Gemini
- `output.json` — compliance report for the incomplete code
- `output_good.json` — compliance report for the corrected code
- `screenshots` - folder containing screenshots of the code submission
- `compliance_report` - containing screenshots of the compliance report

## Objective

The goal is to compare a PRD with submitted code and generate a strict JSON compliance report.

## JSON Output Schema

```json
{
  "compliance_score": 0-100,
  "status": "PASS/FAIL",
  "audit_log": [
    {
      "requirement": "string",
      "met": true,
      "comment": "string"
    }
  ],
  "security_check": "Safe/Unsafe"
}

# Judge Agent – AI Evaluation Project

## About the Project
Judge Agent is a simple AI project that 
checks if a Python code file matches the 
requirements from a PRD. Instead of checking 
everything manually, the program reads the requirement
file and the code file, sends them to the AI model,
and gets a result in JSON format. The result shows
the score, PASS or FAIL status, comments for each
requirement, and a basic security check.


## Technologies Used
- Python
- Gemini API
- Text files
- JSON
- dotenv

## How It Works
First, the program reads the PRD file and the code submission file.  
Then it sends both files to the AI model with a prompt.  
After that, the AI compares the code with the requirements and returns a JSON report.  
The report shows which requirements are met and which are not.

## How to Run
Install the libraries:

```bash
pip install python-dotenv google-generativeai
сreate a .env file and add your API key:

GEMINI_API_KEY=your_api_key_here