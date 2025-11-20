from fastapi import APIRouter, Depends, HTTPException, status
from typing import List
from app import crud, schemas, database
from sqlalchemy.orm import Session

router = APIRouter()

@router.get("/", response_model=List[schemas.Paciente])
def list_pacientes(skip: int = 0, limit: int = 100, db: Session = Depends(database.get_db)):
    return crud.get_pacientes(db, skip, limit)

@router.get("/{paciente_id}", response_model=schemas.Paciente)
def get_paciente(paciente_id: int, db: Session = Depends(database.get_db)):
    p = crud.get_paciente(db, paciente_id)
    if not p:
        raise HTTPException(status_code=404, detail="Paciente no encontrado")
    return p

@router.post("/", response_model=schemas.Paciente, status_code=status.HTTP_201_CREATED)
def create_paciente(paciente: schemas.PacienteCreate, db: Session = Depends(database.get_db)):
    return crud.create_paciente(db, paciente)

@router.put("/{paciente_id}", response_model=schemas.Paciente)
def update_paciente(paciente_id: int, paciente: schemas.PacienteCreate, db: Session = Depends(database.get_db)):
    p = crud.get_paciente(db, paciente_id)
    if not p:
        raise HTTPException(status_code=404, detail="Paciente no encontrado")
    for k,v in paciente.dict().items():
        setattr(p, k, v)
    db.commit()
    db.refresh(p)
    return p

@router.delete("/{paciente_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_paciente(paciente_id: int, db: Session = Depends(database.get_db)):
    p = crud.get_paciente(db, paciente_id)
    if not p:
        raise HTTPException(status_code=404, detail="Paciente no encontrado")
    db.delete(p)
    db.commit()
    return
