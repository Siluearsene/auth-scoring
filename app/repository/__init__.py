from sqlalchemy.orm import Session as SQLAlchemySession
from fastapi import Depends, HTTPException, status
from uuid import UUID
from datetime import datetime, timezone
from app.models.data.session import Session as SessionModel
from app.configuration.database import get_db

class SessionRepository:
    def __init__(self, db: SQLAlchemySession = Depends(get_db)):
        """
        Initialise le repository avec une session SQLAlchemy.
        
        :param db: Session SQLAlchemy
        """
        self.db = db

    def get_session(self, session_id: UUID):
        """
        Récupère une session par son identifiant.
        
        :param session_id: Identifiant de la session
        :return: La session trouvée
        :raises HTTPException: Si la session n'est pas trouvée
        """
        db_session = self.db.query(SessionModel).filter(SessionModel.id == session_id).first()
        if not db_session:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Session not found")
        return db_session

    def delete_session(self, session_id: UUID):
        """
        Supprime une session par son identifiant.
        
        :param session_id: Identifiant de la session
        :return: True si la session est supprimée, sinon False
        """
        db_session = self.get_session(session_id)
        if db_session:
            self.db.delete(db_session)
            self.db.commit()
            return True
        return False

    def get_sessions_by_user(self, user_id: UUID):
        """
        Récupère toutes les sessions pour un utilisateur donné.
        
        :param user_id: Identifiant de l'utilisateur
        :return: Liste des sessions de l'utilisateur
        """
        return self.db.query(SessionModel).filter(SessionModel.user_id == user_id).all()
