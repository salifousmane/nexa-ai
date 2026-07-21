from pydantic import BaseModel
from typing import List, Optional


# -----------------------------
# Diagnostic IA
# -----------------------------

class DiagnosticRequest(BaseModel):
    situation: str
    domain: str
    objectives: str
    current_skills: List[str]
    experience_level: str


class SkillRecommendation(BaseModel):
    name: str
    priority: str
    reason: str


class DiagnosticResponse(BaseModel):
    resume_profil: str

    forces: List[str]

    lacunes_identifiees: List[str]

    competences_prioritaires: List[SkillRecommendation]

    opportunites_evolution: List[str]

    recommandations: List[str]

    premiere_action: str



# -----------------------------
# Parcours personnalisé
# -----------------------------

class LearningStep(BaseModel):
    numero: int
    titre: str
    objectif: str
    duree: str
    competences: List[str]
    actions: List[str]


class LearningPathResponse(BaseModel):
    objectif_final: str

    duree_totale_estimee: str

    etapes: List[LearningStep]

    conseil_personnalise: str

    prochaine_action: str



# -----------------------------
# Mentor IA Chat
# -----------------------------

class ChatRequest(BaseModel):
    message: str
    user_id: Optional[int] = None


class ChatResponse(BaseModel):
    response: str