# API - Hospital (FastAPI)

## Base URL
`/api/v1`

## Recursos principales
- `/pacientes`
- `/medicos`
- `/citas`

---
## Endpoints (resumen)

### Pacientes
- `GET /api/v1/pacientes` -> lista pacientes
- `GET /api/v1/pacientes/{id}` -> obtener paciente
- `POST /api/v1/pacientes` -> crear paciente
    - Payload: { "nombre": "Juan", "fecha_nacimiento": "1990-01-01", "telefono": "1234", "email": "a@a.com" }
    - Respuesta 201: objeto paciente creado
- `PUT /api/v1/pacientes/{id}` -> actualizar paciente
- `DELETE /api/v1/pacientes/{id}` -> eliminar paciente

### Medicos
- `GET /api/v1/medicos`
- `GET /api/v1/medicos/{id}`
- `POST /api/v1/medicos`
    - Payload: { "nombre": "Dra. Ana", "especialidad": "Cardiologia", "email": "ana@h.org" }
- `PUT /api/v1/medicos/{id}`
- `DELETE /api/v1/medicos/{id}`

### Citas
- `GET /api/v1/citas`
- `GET /api/v1/citas/{id}`
- `POST /api/v1/citas`
    - Payload: { "paciente_id": 1, "medico_id": 2, "fecha": "2025-11-20T09:30:00", "motivo": "Consulta" }
    - Validaciones: paciente y medico existen, fecha en formato ISO
- `PUT /api/v1/citas/{id}` -> actualizar (estado, fecha, motivo)
- `DELETE /api/v1/citas/{id}`

---
## Códigos HTTP (uso sugerido)
- 200 OK -> operaciones GET/PUT exitosas
- 201 Created -> POST exitoso
- 204 No Content -> DELETE exitoso
- 400 Bad Request -> validación fallida
- 404 Not Found -> recurso no existe
- 409 Conflict -> email duplicado u otra violación única

---
## Ejemplos de respuestas (objeto paciente)
{
  "id": 1,
  "nombre": "Juan Perez",
  "fecha_nacimiento": "1990-01-01",
  "telefono": "98765432",
  "email": "juan@ejemplo.com"
}

