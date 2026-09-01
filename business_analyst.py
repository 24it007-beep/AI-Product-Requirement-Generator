import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)


def analyze_business_idea(idea):

    prompt = f"""
You are an expert Business Analyst.

Analyze the following business idea:

{idea}

Provide:

1. Problem Statement
2. Target Users
3. Business Goals
4. Key Features

Give a clear and structured response.
Do not use Markdown tables.
Use simple headings and bullet points only.
"""

    completion = client.chat.completions.create(
        model="openai/gpt-oss-20b",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0.7,
        max_completion_tokens=1000
    )

    return completion.choices[0].message.content