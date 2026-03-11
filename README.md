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