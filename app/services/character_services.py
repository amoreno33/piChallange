from fastapi import HTTPException, status
from app.models.character import Character
from app.schemas.character_schemas import Character_create, Character_info, Character_info_all
from typing import List




def create_character(db, new_data: Character_create):
    '''
    Create a new character
    '''
    new_character = Character(
                    CharacterName = new_data.name,
                    CharacterHeight = new_data.height,
                    CharacterMass = new_data.mass,
                    CharacterHairColor = new_data.hair_color,
                    CharacterSkinColor = new_data.skin_color,
                    CharacterEyeColor = new_data.eye_color,
                    CharacterBirthYear = new_data.birth_year
                    )
    db.add(new_character)
    db.commit()
    db.refresh(new_character)
    return new_character

def get_all_character(db):
    '''
    GET ALL characters
    '''

    characters_items: List[Character]  = db.query(Character).all()
    character_db = []
    if characters_items is not None:
        for character in characters_items:
            new_character = Character_info_all(
                id=character.Id,
                name= character.CharacterName,
                height=  character.CharacterHeight,
                mass= character.CharacterMass,
                birth_year= character.CharacterBirthYear,
                eye_color= character.CharacterEyeColor
            )
            character_db.append(new_character)
        return character_db
    else:
        raise HTTPException(status_code=status.HTTP_400_INTERNAL_SERVER_ERROR,
                detail=f"Error: No hay datos")


def get_character(db, character_id):
    '''
    GET a character
    '''
    character_db = db.query(Character).filter(Character.Id == character_id).first()
    if character_db is not None:
        character = Character_info(
              id= character_db.id,
              name= character_db.CharacterName,
              height=  character_db.CharacterHeight,
              mass= character_db.CharacterMass,
              birth_year= character_db.CharacterBirthYear,
              eye_color= character_db.CharacterEyeColor
            ) 
        return character
    else:
        raise HTTPException(status_code=status.HTTP_402_INTERNAL_SERVER_ERROR,
                    detail=f"Error: Error al intentar obtener character")
    

def delete_character(db, character_id):
    '''
    Delete a character
    '''
    if character_id is not None:
        try:
            db.query(Character).filter(Character.Id == character_id).delete()
            db.commit()
        except:
            raise HTTPException(status_code=status.HTTP_402_INTERNAL_SERVER_ERROR,
                    detail=f"Error: Error al intentar eliminar character")
    else:
        raise HTTPException(status_code=status.HTTP_400_INTERNAL_SERVER_ERROR,
                    detail=f"Error: Id erroneo")

def validation_schema_character(db, character_id):
    '''
    Función que valida que el id no se repita.
    '''
    character_id_db = db.query(Character.Id).filter(Character.Id == character_id).first()
    if character_id_db is None:
        return True
    else:
        return False
    