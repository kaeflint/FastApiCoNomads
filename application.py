from fastapi import FastAPI,Depends
from pydantic import BaseModel
from typing import Optional,List
from utils.schema import *
from utils.crud import *



app = FastAPI()

@app.get('/')
async def loadIndex(depends = Depends(get_db)):
    return {'Message':'Welcome back buddy'}


@app.post('/places/', response_model=Place)
def create_places_view(place: Place, db: Session = Depends(get_db)):
    db_place = create_place(db, place)
    return db_place

@app.get('/places/', response_model=List[Place])
def get_places_view(db: Session = Depends(get_db)):
    return get_places(db)

@app.get('/place/{place_id}')
def get_place_view(place_id: int, db: Session = Depends(get_db)):
    return get_place(db, place_id)


