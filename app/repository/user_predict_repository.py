from datetime import datetime, timezone
from sqlalchemy.orm import Session
from fastapi import Depends
from app.configuration.database import get_db
from app.models.data.user_predict import UserPredict
from app.models.requests.user_predict import UserPredictRequest


class UserPredictRepository:
    def __init__(self, db: Session = Depends(get_db)):
        self.db = db

    def create_user_predict(self, user_predict: UserPredictRequest) -> UserPredict:
        db_user = UserPredict(**user_predict.model_dump()) 
        self.db.add(db_user)
        self.db.commit()
        self.db.refresh(db_user)
        return db_user
    