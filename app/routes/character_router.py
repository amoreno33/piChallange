from fastapi import APIRouter, Depends, HTTPException, status
from typing import List
from sqlalchemy.orm import Session
from app.models.character import Character
from app.schemas.character_schemas import Character_create, Character_info, Character_info_all
from app.services.character_services import create_character, delete_character, get_all_character, get_character, validation_schema_character

from config.config_db import get_db


router = APIRouter()


@router.get('/getAll', response_model=List[Character_info_all])
def route_character_getall(db: Session = Depends (get_db)):
    '''
    Deberá retornar la lista con todos los characters. Los datos de cada character
    deberán ser: --- Id, name, height, mass, birth_year, eye_color  ---
    Esta estructura de datos deberá ser validada al momento de retornarla.
    '''
    return get_all_character(db)


@router.get("/get/{character_id}", response_model=Character_info)
def route_character_get_one(character_id: int, db: Session = Depends (get_db)):
    '''
    Retornar characters buscados por su id
    Deberá retornar todos los datos de los character. Esta estructura de datos
    deberá ser validada al momento de retornarla.
    '''
    if validation_schema_character(db,character_id) is False:
        character = get_character(db, character_id)
    else:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                        detail="Id not exist")
    return character


@router.post("/add")
def route_character_add(new_character: Character_create, 
                        db: Session = Depends (get_db)):
    '''
    El nuevo character deberá cumplir las siguientes condiciones:
    ▪ Deberán existir todos los campos del character nuevo
    ▪ No puede tener valor nulo ninguno de los campos
    ▪ Se deberán respetar los tipos de campos
    ▪ El ítem no deberá existir (controlando por su id). Si el character ya
    existe deberá retornar un HTTP Code 400 – Bad Request con el detalle
    acorde al problema que se produjo.
    '''
    if validation_schema_character(db,new_character.id):
        data_db = create_character(db, new_character)
    else:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                        detail="Id already exist")
    return data_db


@router.delete("/delete/{character_id}")
def route_character_delete(character_id: int, db: Session = Depends (get_db)):
    '''
    Si el character existe se elimina y se deberá retornar un HTTP CODE 200 con
    un detalle acorde a la acción que se realizó
    o Si el character no existe deberá retornar un HTTP Code 400 – Bad Request con
    el detalle acorde al problema que se produjo.
    '''
    if validation_schema_character(db,character_id) is False:
        delete_character(db, character_id)
        raise HTTPException(status_code=status.HTTP_200_OK,
                        detail="Succesfull")
    else:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                        detail="Id not exist")