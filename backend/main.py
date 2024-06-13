# Make the pydantic model `Shelter` that will represent this data, then manually
# change this list to be a list[Shelter]. You don't need to write code to convert
# this list, just manually change it by hand.

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from schemas import Shelter, Animal


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
    ),
        Shelter(
        shelter_id=4,
        name="Bailey's Rescued Animals",
        address="25 Main St, St. George, UT 84770",
        animals={"cats": 0, "dogs": 0}
    )
]

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


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