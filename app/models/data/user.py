import uuid
from sqlalchemy import Column, String
from app.configuration.database import Base
from sqlalchemy.dialects.postgresql import UUID as UUIDType
from sqlalchemy.orm import relationship



class User(Base):
    __tablename__ = 'users'
    id = Column(UUIDType(as_uuid=True), primary_key=True,
                default=uuid.uuid4, index=True)
    name = Column(String, index=True)
    matricule = Column(String, index=True)
    email= Column(String, unique=True, index=True)
    password = Column(String, index=True)