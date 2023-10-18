from fastapi import FastAPI
from app.routes.router import router
import config.init_db as init_db
from config.config_db import engine
import os


app = FastAPI(title="Challenge Python",
              description="API documentation",
              version="0.0.0",
              contact={
                "email": "anamariamoreno88@gmail.com",
              })
# routers
app.include_router(router)

@app.on_event("startup")
async def startup_db_client():
  #if os.getenv('ENVIRONMENT') != "DEVELOP":
 init_db. db_global_init(engine)
