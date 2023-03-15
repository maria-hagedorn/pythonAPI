from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional
import json

app = FastAPI()

class Person(BaseModel):
    id: Optional[int] = None
    name: str
    age: int
    gender: str

with open('people.json', 'r') as f:
    people = json.load(f)

@app.get('/person/{p_id}')
def get_person(p_id: int):
    person = [p for p in people if p['id'] == p_id]
    return person[0] if len(person) > 0 else {}

@app.get("/")
def get_all():
    return people


@app.post("/addperson", status_code=201)
def create_person(person: Person):
    p_id = max([p['id'] for p in people]) + 1
    newPerson = {
        "id": p_id,
        "name": person.name,
        "age": person.age,
        "gender": person.gender
    }
    
    people.append(newPerson)

    with open('people.json', 'w') as f:
        json.dump(people, f, indent=2)

    return newPerson


@app.put("/updateperson", status_code=204)
def updatePerson(person: Person):
    newValues = {
        "id": person.id,
        "name": person.name,
        "age": person.age,
        "gender": person.gender
    }

    persons = [p for p in people if p['id'] == person.id]
    if(len(persons) > 0):
        people.remove(persons[0])
        people.append(newValues)

        with open('people.json', 'w') as f:
            json.dump(people, f, indent=2)

        return people
    else:
        return HTTPException(status_code=404, detail=f"Person with id {person.id} does not exist.")

@app.delete("/deleteperson/{p_id}")
def deletePerson(p_id: int):
    person = [p for p in people if p['id'] == p_id]

    if(len(person) > 0):
        people.remove(person[0])

        with open('people.json', 'w') as f:
            json.dump(people, f, indent=2)

        return people
    else:
        return HTTPException(status_code=404, detail=f"Person with id {person.id} does not exist.")

    
