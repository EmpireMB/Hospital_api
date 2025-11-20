from fastapi import FastAPI
from app import database, models
from app.routers import pacientes, medicos, citas

models.Base.metadata.create_all(bind=database.engine)

app = FastAPI(title="Hospital API", version="1.0")

app.include_router(pacientes.router, prefix="/api/v1/pacientes", tags=["Pacientes"])
app.include_router(medicos.router, prefix="/api/v1/medicos", tags=["Medicos"])
app.include_router(citas.router, prefix="/api/v1/citas", tags=["Citas"])

@app.get("/api/v1/health")
def health():
    return {"status": "ok"}
