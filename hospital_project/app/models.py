from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Text
from sqlalchemy.orm import relationship
from app.database import Base

class Medico(Base):
    __tablename__ = "medico"
    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, nullable=False)
    especialidad = Column(String, nullable=False)
    email = Column(String, unique=True, index=True)

    citas = relationship("Cita", back_populates="medico")

class Paciente(Base):
    __tablename__ = "paciente"
    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, nullable=False)
    fecha_nacimiento = Column(String)
    telefono = Column(String)
    email = Column(String, unique=True, index=True)

    citas = relationship("Cita", back_populates="paciente")

class Cita(Base):
    __tablename__ = "cita"
    id = Column(Integer, primary_key=True, index=True)
    paciente_id = Column(Integer, ForeignKey("paciente.id"), nullable=False)
    medico_id = Column(Integer, ForeignKey("medico.id"), nullable=False)
    fecha = Column(String, nullable=False)
    motivo = Column(Text)
    estado = Column(String, default="programada")

    paciente = relationship("Paciente", back_populates="citas")
    medico = relationship("Medico", back_populates="citas")
