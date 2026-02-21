import os
from dotenv import load_dotenv
from google import genai

load_dotenv()
# Configure client with API Key
client = genai.Client(
    api_key=os.getenv("API_KEY")  # Or put key directly (not recommended)
)


def get_feedback(resume_text, jd_text):

    prompt = f"""
    You are an HR expert.

    Compare this resume with the job description.

    1. Give match analysis
    2. List missing skills
    3. Suggest improvements
    4. Recommend keywords
    5. Finally create the template resume

    Resume:
    {resume_text}

    Job Description:
    {jd_text}    
    """

    response = client.models.generate_content(
        model="gemini-2.5-flash-lite",
        contents=prompt
    )

    return response.text