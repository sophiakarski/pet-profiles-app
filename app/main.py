from pets import pets
from fastapi import FastAPI

app = FastAPI()

@app.get("/pets")
def add_pet():
    leila = pets.Pet("Leila", 6, "cat", "female")
    ali = pets.Pet("Ali", 4, "dog", "male")
    return {"Pet" : [leila, ali]}