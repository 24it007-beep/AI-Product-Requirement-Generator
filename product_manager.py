import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)


def create_product_requirements(business_analysis):

    prompt = f"""
You are an expert Product Manager.

Based on the following business analysis:

{business_analysis}

Create a Product Requirements Document.

Include:

1. Product Overview
2. User Stories
3. Functional Requirements
4. Non-Functional Requirements
5. Acceptance Criteria
6. Risks

Give a clear and structured response.

Do not use Markdown formatting.
Do not use # or **.
Do not create tables.
Use simple headings, numbered lists, and bullet points only.
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
        max_completion_tokens=1500
    )

    return completion.choices[0].message.content