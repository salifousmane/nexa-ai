import os
from openai import OpenAI


client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)


def generate_ai_response(
    system_prompt: str,
    user_message: str
) -> str:
    """
    Envoie une demande au modèle OpenAI
    et retourne la réponse générée.
    """

    response = client.chat.completions.create(
        model="gpt-5.6",
        messages=[
            {
                "role": "system",
                "content": system_prompt
            },
            {
                "role": "user",
                "content": user_message
            }
        ],
        temperature=0.7
    )

    return response.choices[0].message.content