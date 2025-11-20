from pydantic import BaseModel, EmailStr
from typing import Optional

class MedicoBase(BaseModel):
    nombre: str
    especialidad: str
    email: Optional[EmailStr] = None

class MedicoCreate(MedicoBase):
    pass

class Medico(MedicoBase):
    id: int
    class Config:
        orm_mode = True

class PacienteBase(BaseModel):
    nombre: str
    fecha_nacimiento: Optional[str] = None
    telefono: Optional[str] = None
    email: Optional[EmailStr] = None

class PacienteCreate(PacienteBase):
    pass

class Paciente(PacienteBase):
    id: int
    class Config:
        orm_mode = True

class CitaBase(BaseModel):
    paciente_id: int
    medico_id: int
    fecha: str
    motivo: Optional[str] = None
    estado: Optional[str] = "programada"

class CitaCreate(CitaBase):
    pass

class Cita(CitaBase):
    id: int
    class Config:
        orm_mode = True
