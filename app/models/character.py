from config.config_db import Base
from sqlalchemy import Column,Integer,String




class Character(Base):
     __tablename__ = 'Character'
     Id =  Column(Integer, autoincrement=True, primary_key=True, index=True)
     CharacterId = Column(Integer)
     CharacterName = Column(String)
     CharacterHeight = Column(Integer)
     CharacterMass = Column(Integer)
     CharacterHairColor = Column(String)
     CharacterSkinColor = Column(String)
     CharacterEyeColor = Column(String)
     CharacterBirthYear = Column(Integer)