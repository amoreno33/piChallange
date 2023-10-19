# IMPORTS -------------------------------------------------------------
from pydantic import BaseModel



class Character_create(BaseModel):
    id:int
    name : str
    height :int
    mass : int
    hair_color : str
    skin_color : str
    eye_color : str
    birth_year : int


class Character_info_all(BaseModel):
    id:int
    name : str
    height :int
    mass : int
    birth_year : int
    eye_color : str


class Character_info(BaseModel):
    id:int
    name : str
    height :int
    mass : int
    birth_year : int
    eye_color : str