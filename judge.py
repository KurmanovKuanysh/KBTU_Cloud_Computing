import json
import os
from pathlib import Path

from dotenv import load_dotenv
import google.generativeai as genai

BASE_DIR = Path(__file__).resolve().parent

load_dotenv(BASE_DIR / ".env")

PRD_FILE = BASE_DIR / "prd.txt"
AGENT_FILE = BASE_DIR / "agent.txt"
BAD_CODE_FILE = BASE_DIR / "code_submission.py"
GOOD_CODE_FILE = BASE_DIR / "code_submission_good.py"
BAD_OUTPUT_FILE = BASE_DIR / "output.json"
GOOD_OUTPUT_FILE = BASE_DIR / "output_good.json"


def read_text_file(path: Path) -> str:
    with open(path, "r", encoding="utf-8") as f:
        return f.read()


def build_prompt(agent_text: str, prd_text: str, code_text: str) -> str:
    return f"""{agent_text}

PRD:
{prd_text}

Code Submission:
{code_text}
"""


def save_json_response(raw_text: str, output_path: Path) -> None:
    data = json.loads(raw_text)
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)


def generate_report(prompt: str, output_path: Path) -> None:
    api_key = os.getenv("GEMINI_API_KEY")

    if not api_key:
        raise ValueError("GEMINI_API_KEY not found in .env file")

    genai.configure(api_key=api_key)
    model = genai.GenerativeModel("gemini-1.5-flash")

    response = model.generate_content(prompt)
    save_json_response(response.text, output_path)


def main() -> None:
    agent_text = read_text_file(AGENT_FILE)
    prd_text = read_text_file(PRD_FILE)

    bad_code = read_text_file(BAD_CODE_FILE)
    good_code = read_text_file(GOOD_CODE_FILE)

    bad_prompt = build_prompt(agent_text, prd_text, bad_code)
    good_prompt = build_prompt(agent_text, prd_text, good_code)

    generate_report(bad_prompt, BAD_OUTPUT_FILE)
    generate_report(good_prompt, GOOD_OUTPUT_FILE)

    print("Reports generated successfully:")
    print(f"- {BAD_OUTPUT_FILE.name}")
    print(f"- {GOOD_OUTPUT_FILE.name}")


if __name__ == "__main__":
    main()