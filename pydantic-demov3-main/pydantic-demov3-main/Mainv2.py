from pydantic import BaseModel, EmailStr, ValidationError, field_validator
import ipywidgets as widgets
from IPython.display import display, clear_output

# Benutzer-Datenmodell mit Validierung
class User(BaseModel):
    name: str
    age: int
    email: EmailStr

    @field_validator("name")
    def check_name(cls, v):
        if not v.replace(" ", "").isalpha():
            raise ValueError("Name darf nur Buchstaben und Leerzeichen enthalten.")
        return v

    @field_validator("age")
    def check_age(cls, v):
        if not 18 <= v <= 110:
            raise ValueError("Alter muss zwischen 18 und 110 liegen.")
        return v

    @field_validator("email")
    def check_email_domain(cls, v):
        allowed_domains = {"gmail.com", "yahoo.com", "outlook.com", "hotmail.com", "web.de", "gmx.de"}
        domain = v.split("@")[-1]
        if domain not in allowed_domains:
            raise ValueError(f"Nur offizielle Anbieter erlaubt: {', '.join(sorted(allowed_domains))}")
        return v

# Eingabe-Widgets erstellen
name_input = widgets.Text(description="Name:")
age_input = widgets.Text(description="Alter:")
email_input = widgets.Text(description="Email:")
output = widgets.Output()

# Validierungsfunktion
def validate_data(change):
    with output:
        clear_output()

        # Rohdaten sammeln
        data = {
            "name": name_input.value.strip(),
            "age": age_input.value.strip(),
            "email": email_input.value.strip(),
        }

        # Alterswert prüfen
        if not data["age"].isdigit():
            print("Fehler:\nAlter muss eine Zahl sein.")
            return

        # Alter in Integer umwandeln
        data["age"] = int(data["age"])

        # Validierung mit Pydantic
        try:
            user = User(**data)
            print(" Gültige Benutzerdaten:")
            print(user)
        except (ValidationError, ValueError) as e:
            print(" Fehler:")
            print(e)

# Events registrieren
name_input.observe(validate_data, names='value')
age_input.observe(validate_data, names='value')
email_input.observe(validate_data, names='value')

# UI anzeigen
display(name_input, age_input, email_input, output)

# Initial prüfen
validate_data(None)
