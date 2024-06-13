from pydantic import BaseModel


class Animal(BaseModel):
    cats: int
    dogs: int

class Shelter(BaseModel):
    shelter_id: int
    name: str
    address: str
    animals: Animal