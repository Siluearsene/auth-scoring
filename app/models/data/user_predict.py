import uuid
from sqlalchemy import Column, String, Float, Integer
from app.configuration.database import Base
from sqlalchemy.dialects.postgresql import UUID as UUIDType

class UserPredict(Base):
    __tablename__ = 'users_predict'
    id = Column(UUIDType(as_uuid=True), primary_key=True, default=uuid.uuid4, index=True)
    name = Column(String, index=True)  # NOM
    montant_pret = Column(Float, index=True)  # MONTANT DU PRÊT
    anciennete_avant_pret = Column(Float, index=True)  # ANCIENNETÉ AVANT PRÊT
    age = Column(Integer, index=True)  # ÂGE
    nombre_enfants = Column(Integer, index=True)  # NOMBRE D’ENFANTS
    montant_encours = Column(Float, index=True)  # MONTANT ENCOURS
    nombre_de_credit = Column(Integer, index=True)  # NOMBRE DE CREDIT
    taux_interet = Column(Float, index=True)  # TAUX D’INTÉRÊT
    revenu = Column(Float, index=True)  # REVENU
    duree_pret = Column(Float, index=True)  # DURÉE DU PRÊT
    montant_pret_pour_annee = Column(Float, index=True)  # MONTANT PRÊT POUR L’ANNÉE
    reste_a_vivre = Column(Float, index=True)  # RESTE À VIVRE
    agence = Column(String, index=True)  # AGENCE
    genre = Column(String, index=True)  # GENRE
    secteur_activite = Column(String, index=True)  # SECTEUR D’ACTIVITÉ
    segment = Column(String, index=True)  # SEGMENT
