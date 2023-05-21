from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel, Field
import models
from models import Element
from database import engine, SessionLocal
from sqlalchemy.orm import Session

app = FastAPI()

models.Base.metadata.create_all(engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/get/all")
def get_all(db: Session = Depends(get_db)):
    return db.query(models.Element).all()


@app.get("/get/{id}")
async def getElementById(id: int, db: Session = Depends(get_db)):
    return db.query(models.Element).filter(models.Element.id == id).first()

# @app.post("/post/all")
# def load_csv(db: Session = Depends(get_db)):
#     with open("periodicTable.csv", newline='') as csvFile:
#         reader = csv.reader(csvFile)
#         for row in reader:
#             _element = models.Element()
#             rowString = ",".join(row)
#             info = rowString.split(";")
#             _element.element = info[1]
#             _element.symbol = info[2]
#             _element.atomicMass = info[3]
#             _element.numberOfNeutrons = info[4]
#             _element.numberOfProtons = info[5]
#             _element.numberOfElectrons = info[6]
#             _element.period = info[7]
#             _element.group = info[8]
#             _element.phase = info[9]
#             db.add(_element)
#             db.commit()
#     return "done"
#
# @app.delete("/delete/all")
# def delete_all(db: Session = Depends(get_db)):
#     db.query(models.Element).delete(synchronize_session=False)
#     db.commit()
