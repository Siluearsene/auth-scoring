from datetime import timedelta
from typing import Annotated
from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from jwt import InvalidTokenError
import logfire
from app.configuration.config import AuthSettings
from app.exceptions.custom_exception import InactiveUserException, InvalidTokenException, UserNotFoundException
from app.services.user_service import UserService

auth_settings = AuthSettings()

router = APIRouter()


@router.post("/login")
def login(form_data: Annotated[OAuth2PasswordRequestForm, Depends()],  user_service: UserService = Depends(UserService)):
    """
    Route de connexion pour authentifier un utilisateur et générer des tokens d'accès.

    :param form_data: Formulaire de requête contenant les données d'authentification de l'utilisateur
    :param user_service: Service d'utilisateur pour gérer l'authentification
    :param session_service: Service de session pour créer et gérer les sessions utilisateur
    :return: Réponse de succès de connexion contenant les tokens d'accès et de rafraîchissement
    :raises HTTPException: Si l'authentification échoue
    """
    try:
        user = user_service.authenticate_user(
            matricule=form_data.username, password=form_data.password)     
        return user
    
    except HTTPException as e:
        logfire.error(
            f"Échec de la connexion pour l'utilisateur avec Matricule {form_data.username}: {e.detail}")
        raise e

