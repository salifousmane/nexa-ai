import json

from app.services.openai_service import generate_ai_response


PATH_SYSTEM_PROMPT = """
Tu es Nexa AI, un architecte de parcours d'évolution.

À partir d'un diagnostic utilisateur,
crée un parcours personnalisé et progressif.

Le parcours doit contenir :

- objectif_final
- duree_totale_estimee
- etapes
- conseil_personnalise
- prochaine_action

Chaque étape doit contenir :

- numero
- titre
- objectif
- duree
- competences
- actions

Le parcours doit être réaliste,
adapté au niveau utilisateur,
et orienté vers la pratique.
"""


def generate_learning_path(
    diagnostic: dict
) -> dict:
    """
    Génère un parcours personnalisé
    à partir du diagnostic IA.
    """

    user_message = json.dumps(
        diagnostic,
        ensure_ascii=False
    )

    response = generate_ai_response(
        PATH_SYSTEM_PROMPT,
        user_message
    )

    try:
        return json.loads(response)

    except json.JSONDecodeError:
        return {
            "error": "La réponse IA n'est pas un JSON valide",
            "raw_response": response
        }
