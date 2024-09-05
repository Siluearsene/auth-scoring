from pydantic import BaseModel, Field
from uuid import UUID

class UserPredictRequest(BaseModel):
    id: UUID = Field(..., description="Unique identifier for the user")
    name: str = Field(..., min_length=2, max_length=50, description="Nom de l'utilisateur")
    montant_pret: float = Field(..., description="Montant du prêt")
    anciennete_avant_pret: float = Field(..., description="Ancienneté avant prêt en années")
    age: int = Field(..., description="Âge de l'utilisateur")
    nombre_enfants: int = Field(..., description="Nombre d'enfants")
    montant_encours: float = Field(..., description="Montant en cours")
    nombre_de_credit: int = Field(..., description="Nombre de crédits")
    taux_interet: float = Field(..., description="Taux d'intérêt")
    revenu: float = Field(..., description="Revenu de l'utilisateur")
    duree_pret: float = Field(..., description="Durée du prêt en mois")
    montant_pret_pour_annee: float = Field(..., description="Montant du prêt pour l'année")
    reste_a_vivre: float = Field(..., description="Reste à vivre")
    agence: str = Field(..., min_length=2, max_length=50, description="Nom de l'agence")
    genre: str = Field(..., min_length=1, max_length=20, description="Genre de l'utilisateur")
    secteur_activite: str = Field(..., min_length=2, max_length=50, description="Secteur d'activité")
    segment: str = Field(..., min_length=2, max_length=50, description="Segment de l'utilisateur")

    class Config:
        orm_mode = True
