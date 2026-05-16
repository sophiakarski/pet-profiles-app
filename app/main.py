from pets import pets
from fastapi import FastAPI

app = FastAPI()

@app.get("/pets")
def add_pet():
    leila = pets.Pet("Leila", 6, "cat", "female")
    ali = pets.Pet("Ali", 4, "dog", "male")
    return {"Pet" : [leila, ali]}

# @app.get("/pets/{pet_name}")
# def get_pet(pet_name: str):
#     leila = pets.Pet("Leila", 6, "cat", "female")
#     ali = pets.Pet("Ali", 4, "dog", "male")
#     if pet_name == "Leila":
#         return {"Pet" : leila}
#     elif pet_name == "Ali":
#         return {"Pet" : ali}
#     else:
#         return {"Error" : "Pet not found"}

# @app.post("/pets")
# def create_pet(pet: pets.Pet):
#     return {"Pet" : pet}