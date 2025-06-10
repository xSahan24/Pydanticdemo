# Datenvalidierung mit Pydantic

Dies ist eine einfache Demo zur Datenvalidierung mit Pydantic und FastAPI.

## Starten der API

```bash
uvicorn app.main:app --reload
```

## Beispiel-Request

```json
POST /users/
{
  "name": "Anna",
  "age": 28,
  "email": "anna@example.com"
}
```

## Tests ausführen

```bash
pytest
```
