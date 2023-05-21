from sqlalchemy import Column, Integer, String, Float
from database import Base

class Element(Base):
    __tablename__ = "PeriodicTable"

    id = Column(Integer, primary_key=True)
    element = Column(String)
    symbol = Column(String)
    atomicMass = Column(Float)
    numberOfNeutrons = Column(Integer)
    numberOfProtons = Column(Integer)
    numberOfElectrons = Column(Integer)
    period = Column(Integer)
    group = Column(Integer)
    phase = Column(String)
