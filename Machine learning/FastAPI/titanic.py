# api.py

from fastapi import FastAPI
from pydantic import BaseModel, Field, computed_field
from typing import Annotated,Literal
import pickle
import pandas as pd

# Load model and encoders
with open("titanic_model.pkl", "rb") as f:
    model = pickle.load(f)

with open("label_encoders.pkl", "rb") as f:
    encoders = pickle.load(f)

app = FastAPI(title="Titanic Survival Prediction API")

# ['Pclass', 'Sex', 'Age', 'SibSp', 'Parch', 'Fare', 'Embarked']
# Define input schema
class Passenger(BaseModel):
    Pclass: Annotated[int, Field(...,gt = 1, ls = 4, description="Passanger Class")]
    Sex: Annotated[Literal['male','female'], Field(..., description="Gender of the user")]  # 'male' or 'female'
    Age: Annotated[int, Field(..., gt = 0, lt = 120,description="Age of the Passenger")]
    SibSp: Annotated[int, Field(..., gt = 0, lt = 120,description="SibSp of the user")]
    Parch: Annotated[float, Field(...,description="Parch of the passenger")]
    Fare: Annotated[int, Field(...,description="Fare of the Passenger")]
    Embarked: Annotated[Literal["S","C","Q"], Field(..., description="Age of the user")]

@app.post("/predict")
def predict_survival(passenger: Passenger):
    # Encode categorical fields
    sex_encoded = encoders['Sex'].transform([passenger.Sex])[0]
    embarked_encoded = encoders['Embarked'].transform([passenger.Embarked])[0]

    # Create input DataFrame
    input_df = pd.DataFrame([{
        "Pclass": passenger.Pclass,
        "Sex": sex_encoded,
        "Age": passenger.Age,
        "SibSp": passenger.SibSp,
        "Parch": passenger.Parch,
        "Fare": passenger.Fare,
        "Embarked": embarked_encoded
    }])

    # Predict
    prediction = model.predict(input_df)[0]
    return {"survived": int(prediction)}
