from sqlalchemy.orm import Session
from app import models, schemas
from fastapi import HTTPException, status

# Medico
def get_medico(db: Session, medico_id: int):
    return db.query(models.Medico).filter(models.Medico.id==medico_id).first()

def get_medicos(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Medico).offset(skip).limit(limit).all()

def create_medico(db: Session, medico: schemas.MedicoCreate):
    db_med = models.Medico(**medico.dict())
    db.add(db_med)
    db.commit()
    db.refresh(db_med)
    return db_med

# Paciente
def get_paciente(db: Session, paciente_id: int):
    return db.query(models.Paciente).filter(models.Paciente.id==paciente_id).first()

def get_pacientes(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Paciente).offset(skip).limit(limit).all()

def create_paciente(db: Session, paciente: schemas.PacienteCreate):
    db_p = models.Paciente(**paciente.dict())
    db.add(db_p)
    db.commit()
    db.refresh(db_p)
    return db_p

# Cita
def get_cita(db: Session, cita_id: int):
    return db.query(models.Cita).filter(models.Cita.id==cita_id).first()

def get_citas(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Cita).offset(skip).limit(limit).all()

def create_cita(db: Session, cita: schemas.CitaCreate, db_session: Session):
    # validar existencia paciente y medico
    paciente = get_paciente(db_session, cita.paciente_id)
    medico = get_medico(db_session, cita.medico_id)
    if not paciente or not medico:
        raise HTTPException(status_code=400, detail="Paciente o médico no existen")
    db_c = models.Cita(**cita.dict())
    db.add(db_c)
    db.commit()
    db.refresh(db_c)
    return db_c
