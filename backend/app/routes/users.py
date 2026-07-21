from fastapi import APIRouter

from app.schemas.user_schema import (
    UserCreate,
    UserLogin
)


router = APIRouter()


@router.post("/register")
def register_user(
    user: UserCreate
):
    """
    Création d'un utilisateur.
    
    Version MVP :
    structure de base.
    La connexion réelle à la base sera ajoutée
    avec la couche authentification.
    """

    return {
        "message": "Utilisateur créé",
        "email": user.email
    }


@router.post("/login")
def login_user(
    user: UserLogin
):
    """
    Connexion utilisateur.
    """

    return {
        "message": "Connexion réussie",
        "email": user.email
    }


@router.get("/{user_id}")
def get_user(
    user_id: int
):
    """
    Récupération d'un profil utilisateur.
    """

    return {
        "user_id": user_id
    }
