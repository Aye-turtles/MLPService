from fastapi import FastAPI
from pydantic import BaseModel

from DownloadFile import download_csv_from_github
from evaluate_file import evaluate
from fastapi.middleware.cors import CORSMiddleware

REPO_PATH = "https://raw.githubusercontent.com/Aye-turtles/records/refs/heads/main/uploads/"
STORAGE_PATH = "./files/"
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Permite cualquier origen
    allow_credentials=True,  # Si necesitas manejar cookies o autenticación
    allow_methods=["*"],  # Permite todos los métodos HTTP (GET, POST, PUT, etc.)
    allow_headers=["*"],  # Permite todas las cabeceras
)
@app.get("/")
async def root():
    return {"message": "It's working"}


# Esquema para obtener archivo de records de Nido
class Nest(BaseModel):
    assignedID: str
    sensorAssignedID: str


# Ruta para descargar un archivo CSV desde GitHub
@app.post("/evaluate-behavior/")
def evaluate_behavior(nest: Nest):
    records_file_name = nest.assignedID + "-" + nest.sensorAssignedID + ".csv"
    record_path = REPO_PATH + records_file_name
    download_csv_from_github(record_path, STORAGE_PATH)

    result = evaluate(STORAGE_PATH + records_file_name)
    if result >= 75:
        return {"clas": 1, "result": result}
    return {"clas": 0, "result": result}
