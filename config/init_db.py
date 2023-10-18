
# inicializacion, creacion y carga de datos por defecto en la BD.
from app.models import character


def db_global_init(engine):
    character.Base.metadata.create_all(bind=engine)