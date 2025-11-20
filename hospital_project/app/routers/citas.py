from fastapi import APIRouter, Depends, HTTPException, status
from typing import List
from app import crud, schemas, database
from sqlalchemy.orm import Session

router = APIRouter()

@router.get("/", response_model=List[schemas.Cita])
def list_citas(skip: int = 0, limit: int = 100, db: Session = Depends(database.get_db)):
    return crud.get_citas(db, skip, limit)

@router.get("/{cita_id}", response_model=schemas.Cita)
def get_cita(cita_id: int, db: Session = Depends(database.get_db)):
    c = crud.get_cita(db, cita_id)
    if not c:
        raise HTTPException(status_code=404, detail="Cita no encontrada")
    return c

@router.post("/", response_model=schemas.Cita, status_code=status.HTTP_201_CREATED)
def create_cita(cita: schemas.CitaCreate, db: Session = Depends(database.get_db)):
    return crud.create_cita(cita=cita, db=db, db_session=db)

@router.put("/{cita_id}", response_model=schemas.Cita)
def update_cita(cita_id: int, cita: schemas.CitaCreate, db: Session = Depends(database.get_db)):
    c = crud.get_cita(db, cita_id)
    if not c:
        raise HTTPException(status_code=404, detail="Cita no encontrada")
    for k,v in cita.dict().items():
        setattr(c, k, v)
    db.commit()
    db.refresh(c)
    return c

@router.delete("/{cita_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_cita(cita_id: int, db: Session = Depends(database.get_db)):
    c = crud.get_cita(db, cita_id)
    if not c:
        raise HTTPException(status_code=404, detail="Cita no encontrada")
    db.delete(c)
    db.commit()
    return
