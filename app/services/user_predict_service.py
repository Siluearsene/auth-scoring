import os
from openpyxl import Workbook
from fastapi import Depends
from app.repository.user_predict_repository import UserPredictRepository
from app.models.requests.user_predict import UserPredictRequest

class UserServicePredict:
    def __init__(self, user_predict_repo: UserPredictRepository = Depends(UserPredictRepository)):
        self.user_predict_repo = user_predict_repo
        
    def create_user_predict(self, user_predict_data: UserPredictRequest) -> str:
        # Définir le répertoire et le nom du fichier
        directory = "generated_files"
        filename = "user_predict.xlsx"
        file_path = os.path.join(directory, filename)

        # Créer le répertoire s'il n'existe pas
        if not os.path.exists(directory):
            os.makedirs(directory)

        # Créer un nouveau classeur Excel et sélectionner la feuille active
        wb = Workbook()
        ws = wb.active

        # Ajouter des en-têtes à la feuille de calcul
        headers = [
            "MONTANT_NOMINAL_DOSSIER", "ANCIENNETE AVANT PRÊT", "Age", "Nombre d_enfant", 
            "Montant_encours", "Nombre de credit", "Taux interet", "revenu", 
            "Durée_pret", "MONTANT_NOMINAL_DOSSIER_ANNEE", "Reste_a_vivre", 
            "Agence", "Genre", "Secteur_activité", "Segment"
        ]
        ws.append(headers)

        # Ajouter les données de l'utilisateur à la feuille de calcul
        ws.append([
            user_predict_data.montant_pret,
            user_predict_data.anciennete_avant_pret,
            user_predict_data.age,
            user_predict_data.nombre_enfants,
            user_predict_data.montant_encours,
            user_predict_data.nombre_de_credit,
            user_predict_data.taux_interet,
            user_predict_data.revenu,
            user_predict_data.duree_pret,
            user_predict_data.montant_pret_pour_annee,
            user_predict_data.reste_a_vivre,
            user_predict_data.agence,
            user_predict_data.genre,
            user_predict_data.secteur_activite,
            user_predict_data.segment,
        ])

        # Sauvegarder le fichier Excel dans le répertoire spécifié
        wb.save(file_path)

        # Retourner le chemin du fichier
        return file_path
