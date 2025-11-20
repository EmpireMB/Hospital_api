# Hospital API (FastAPI)
Proyecto de ejemplo solicitado por el estudiante.
Contiene:
- API en FastAPI con CRUD para pacientes, medicos y citas.
- Script SQL para crear las tablas (sql/schema.sql).
- Dockerfile para crear la imagen y desplegar.
- Instrucciones rápidas:
    - Local: crear un virtualenv, instalar requirements.txt y ejecutar `uvicorn app.main:app --reload`
    - Docker: `docker build -t hospital-api .` y `docker run -p 8000:8000 hospital-api`
