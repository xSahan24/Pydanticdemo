from pydantic import BaseModel, EmailStr, ValidationError

class User(BaseModel):
    name: str
    age: int
    email: EmailStr

def main():
    user_data_valid = {
        "name": "Max Mustermann",
        "age": 30,
        "email": "max@example.com"
    }

    user_data_invalid = {
        "name": "Anna",
        "age": "zwanzig",
        "email": "nicht-email"
    }

    print("Valid user data:")
    try:
        user = User(**user_data_valid)
        print(user)
    except ValidationError as e:
        print("Fehler:", e)

    print("\nInvalid user data:")
    try:
        user = User(**user_data_invalid)
        print(user)
    except ValidationError as e:
        print("Fehler:", e)

if __name__ == "__main__":
    main()
