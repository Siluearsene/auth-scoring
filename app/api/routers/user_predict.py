from fastapi import APIRouter, Depends, status
import pickle
import pandas as pd
from sklearn.preprocessing import LabelEncoder, StandardScaler
from app.services.user_predict_service import UserServicePredict
from app.models.requests.user_predict import UserPredictRequest
from fastapi.responses import StreamingResponse
import io

router = APIRouter()

@router.post("/generate-excel/", status_code=status.HTTP_200_OK)
def generate_excel(user_predict: UserPredictRequest, user_service: UserServicePredict = Depends()):
    # Générer et sauvegarder le fichier Excel initial
    fichier_bytes = user_service.create_user_predict(user_predict)

    # Prepare the file for download
    # file_stream = io.BytesIO(fichier_bytes)

    # Return the file as a response
    # response = StreamingResponse(
    #     fichier_bytes,
    #     media_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
    #     headers={"Content-Disposition": "attachment; filename=fichier_test.xlsx"}
    # )
    # print("Données d'entrée: ", user_predict)

    # Load the Excel file into a DataFrame directly from the in-memory bytes
    X1 = pd.read_excel(fichier_bytes)

    # Separate numerical and categorical columns
    numerical_cols = X1.select_dtypes(include=['int64', 'float64']).columns
    categorical_cols = X1.select_dtypes(include=['object']).columns

    # Convert all categorical columns to strings
    X1[categorical_cols] = X1[categorical_cols].astype(str)

    # Separate numerical and categorical data
    data_numeri = X1[numerical_cols]
    data_cate = X1[categorical_cols]

    # Apply label encoding to categorical columns
    label_encoder = LabelEncoder()
    for column in data_cate.columns:
        data_cate[column] = label_encoder.fit_transform(data_cate[column])

    # Concatenate numerical and categorical columns
    data = pd.concat([data_numeri, data_cate], axis=1)

    # Swap columns 'Segment', 'Genre', 'Secteur_activité', and 'Reste_a_vivre'
    data['Segment'], data['Genre'] = data['Genre'].copy(), data['Segment'].copy()
    data['Genre'], data['Reste_a_vivre'] = data['Reste_a_vivre'].copy(), data['Genre'].copy()
    data['Secteur_activité'], data['Genre'] = data['Genre'].copy(), data['Secteur_activité'].copy()

    # List of new column names
    new_column_names = [
        'MONTANT_NOMINAL_DOSSIER', 'ANCIENNETE AVANT PRÊT ', 'Age ', 'Nombre d_enfant ', 
        'Montant_encours', 'Nombre de credit ', 'Taux interet ', 'revenu ', 'Durée_pret',
        'MONTANT_NOMINAL_DOSSIER_ANNEE', 'Segment', 'Agence', 
        'Secteur_activité', 'Reste_a_vivre ', 'Genre'
    ]

    # Rename columns in data
    data.columns = new_column_names

    # Standardize numerical columns
    scaler = StandardScaler()
    numeric_columns = data.select_dtypes(include=['float64', 'int64']).columns
    data[numeric_columns] = scaler.fit_transform(data[numeric_columns])

    # Try to load the model with exception handling
    try:
        filename = '/home/silue/Téléchargements/modelbest.sav'
        scoring = pickle.load(open(filename, 'rb'))
    except Exception as e:
        print(f"Failed to load the model: {e}")
        raise  # Re-raise the exception after logging

    # Predict values and probabilities
    Y_pred = scoring.predict(data)
    Y_Prob = scoring.predict_proba(data)[:, 1]

    # Add predictions and probabilities to data
    data['y_predict'] = Y_pred
    data['y_Prob'] = Y_Prob
    print(data['y_predict'], '================1')
    print(data['y_Prob'], '================2')

    probabilite = data['y_Prob']
    prediction = data['y_predict']

    # return probabilite,prediction
