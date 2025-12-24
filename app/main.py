from fastapi import FastAPI,HTTPException
from pydantic import BaseModel
import uvicorn
from data_interactor import Contact


class Contacts(BaseModel):
    first_name: str
    last_name: str
    phone_number: str


app = FastAPI()


@app.get("/contacts")
def get_all_contact():
    try:
        return Contact.get_all_contacts()
    except HTTPException as e:
        raise HTTPException (status_code= 400,
                                detail=f"you have an error: {e}")

@app.post("/contacts")
def create_new_contact(item: Contacts):
    try: 
        return {"message": f"new contact id: {Contact.create_contact(item.first_name, item.last_name, item.phone_number)}"}
    except HTTPException:
        raise HTTPException


@app.put("/contacts/{id}")
def update_existing_contact(id: int, item: Contacts):
    try:
        return {"success": Contact.update_contact(id, item.first_name, item.last_name, item.phone_number)}
    except HTTPException:
        raise HTTPException


@app.delete("/contacts/{id}")
def delete_existing_contact(id: int):
    try:
        Contact.delete_contact(id)
        return {"message": f"Contact {id} deleted"}
    except HTTPException:
        raise HTTPException

if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)
