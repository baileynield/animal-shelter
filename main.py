# Make the pydantic model `Shelter` that will represent this data, then manually
# change this list to be a list[Shelter]. You don't need to write code to convert
# this list, just manually change it by hand.

from fastapi import FastAPI

from schemas import Shelter, Animal

app = FastAPI()

shelters: list[Shelter] = [
    Shelter(
        shelter_id=1,
        name="St. George Animal Shelter",
        address="605 Waterworks Dr, St. George, UT 84770",
        animals={"cats": 13, "dogs": 15}
    ),
    Shelter(
        shelter_id=2,
        name="St. George Paws",
        address="1125 W 1130 N, St. George, UT 84770",
        animals={"cats": 12, "dogs": 9}
    ),
    Shelter(
        shelter_id=3,
        name="Animal Rescue Team",
        address="1838 W 1020 N Ste. B, St. George, UT 84770",
        animals={"cats": 4, "dogs": 7}
    )
]


@app.get("/shelters")
async def get_shelters() -> list[Shelter]:
    return shelters

@app.post("/shelters")
async def create_shelter(shelter: Shelter) -> None:
    shelters.append(shelter)

@app.put("/shelter/{shelter_id}")
async def update_shelters(shelter_id: int, updated_shelter: Shelter) -> None:
    for i, shelter in enumerate(shelters):
        if shelter.shelter_id == shelter_id:
            shelters[i] = updated_shelter
            return

@app.delete("/shelters/{shelter_id}")
async def delete_items(shelter_id: int) -> None:
    for i, shelter in enumerate(shelters):
        if shelter.shelter_id == shelter_id:
            shelters.pop(i)
            return