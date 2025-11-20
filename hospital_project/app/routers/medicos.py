from fastapi import APIRouter, Depends, HTTPException, status
from typing import List
from app import crud, schemas, database
from sqlalchemy.orm import Session

router = APIRouter()

@router.get("/", response_model=List[schemas.Medico])
def list_medicos(skip: int = 0, limit: int = 100, db: Session = Depends(database.get_db)):
    return crud.get_medicos(db, skip, limit)

@router.get("/{medico_id}", response_model=schemas.Medico)
def get_medico(medico_id: int, db: Session = Depends(database.get_db)):
    m = crud.get_medico(db, medico_id)
    if not m:
        raise HTTPException(status_code=404, detail="Medico no encontrado")
    return m

@router.post("/", response_model=schemas.Medico, status_code=status.HTTP_201_CREATED)
def create_medico(medico: schemas.MedicoCreate, db: Session = Depends(database.get_db)):
    return crud.create_medico(db, medico)

@router.put("/{medico_id}", response_model=schemas.Medico)
def update_medico(medico_id: int, medico: schemas.MedicoCreate, db: Session = Depends(database.get_db)):
    m = crud.get_medico(db, medico_id)
    if not m:
        raise HTTPException(status_code=404, detail="Medico no encontrado")
    for k,v in medico.dict().items():
        setattr(m, k, v)
    db.commit()
    db.refresh(m)
    return m

@router.delete("/{medico_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_medico(medico_id: int, db: Session = Depends(database.get_db)):
    m = crud.get_medico(db, medico_id)
    if not m:
        raise HTTPException(status_code=404, detail="Medico no encontrado")
    db.delete(m)
    db.commit()
    return
