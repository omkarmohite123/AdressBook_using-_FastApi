from pydantic import BaseModel


class User(BaseModel):
    FirstName: str
    LastName: str
    Pin:int
    state:str
    Latitude:int
    Longitude:int
