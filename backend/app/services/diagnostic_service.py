import json

from app.services.openai_service import generate_ai_response


DIAGNOSTIC_SYSTEM_PROMPT = """
Tu es Nexa AI, un conseiller intelligent spécialisé
dans l'évolution des compétences.

Analyse le profil utilisateur et retourne un diagnostic
structuré en JSON.

Le résultat doit contenir :

- resume_profil
- forces
- lacunes_identifiees
- competences_prioritaires
- opportunites_evolution
- recommandations
- premiere_action

Ne donne pas de garantie.
Reste réaliste et personnalisé.
"""


def create_diagnostic(user_data: dict) -> dict:
    """
    Génère un diagnostic personnalisé
    à partir des informations utilisateur.
    """

    user_message = json.dumps(
        user_data,
        ensure_ascii=False
    )

    response = generate_ai_response(
        DIAGNOSTIC_SYSTEM_PROMPT,
        user_message
    )

    try:
        return json.loads(response)

    except json.JSONDecodeError:
        return {
            "error": "La réponse IA n'est pas un JSON valide",
            "raw_response": response
        }