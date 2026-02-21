from google import genai
import os
from dotenv import load_dotenv

load_dotenv()
client = genai.Client(api_key=os.getenv("API_KEY"))


def ai_match_score(resume, jd):

    prompt = f"""
    You are an ATS system.

    Compare this resume and job description.

    Give ONLY a number between 0 and 100.

    Resume:
    {resume}

    Job:
    {jd}
    """

    res = client.models.generate_content(
        model="gemini-2.5-flash-lite",
        contents=prompt
    )

    return float(res.text.strip())