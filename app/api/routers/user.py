from typing import Annotated, List
from uuid import UUID
from fastapi import APIRouter, Depends, status
from app.models.data.user import User
from app.models.requests.user import UserInDB, UserResponse, UserUpdate, UserCreate
from app.services.user_service import UserService

router = APIRouter()    


@router.get("/", response_model=List[UserInDB], status_code=status.HTTP_200_OK)
def get_all_users(service: UserService = Depends(UserService)):
    """
    Récupère tous les utilisateurs.

    **Réponse**:
    - **200 OK**: Liste des utilisateurs.
    """
    return service.get_all_users()


@router.get("/{user_id}", response_model=UserInDB, status_code=status.HTTP_200_OK)
def get_user_by_id(user_id: UUID, service: UserService = Depends(UserService)):
    """
    Récupère un utilisateur par son identifiant.

    **Paramètres**:
    - `user_id` (UUID): Identifiant de l'utilisateur.

    **Réponse**:
    - **200 OK**: Détails de l'utilisateur.
    - **404 Not Found**: Utilisateur non trouvé.
    """
    return service.get_user_by_id(user_id)


@router.post("/", response_model=UserInDB, status_code=status.HTTP_201_CREATED)
def create_user(user: UserCreate, service: UserService = Depends(UserService)):
    """
    Crée un nouvel utilisateur.

    **Réponse**:
    - **201 Created**: Utilisateur créé avec succès.
    - **400 Bad Request**: Email déjà utilisé.
    """
    return service.create_user(user)


@router.put("/{user_id}", response_model=UserInDB, status_code=status.HTTP_200_OK)
def update_user(user_id: UUID, user: UserUpdate, service: UserService = Depends(UserService)):
    """
    Met à jour un utilisateur existant.

    **Paramètres**:
    - `user_id` (UUID): Identifiant de l'utilisateur.

    **Réponse**:
    - **200 OK**: Utilisateur mis à jour avec succès.
    - **404 Not Found**: Utilisateur non trouvé.
    """
    return service.update_user(user_id, user)


@router.delete("/{user_id}", status_code=status.HTTP_200_OK)
def delete_user(user_id: UUID, service: UserService = Depends(UserService)):
    """
    Supprime un utilisateur par son identifiant.

    **Paramètres**:
    - `user_id` (UUID): Identifiant de l'utilisateur.

    **Réponse**:
    - **200 OK**: Utilisateur supprimé avec succès.
    - **404 Not Found**: Utilisateur non trouvé.
    """
    is_deleted = service.delete_user(user_id)
    if is_deleted:
        return {"message": "Utilisateur supprimé avec succès"}


