from fastapi import FastAPI
from pydantic import BaseModel

class ModelInput(BaseModel):
    Temperature	:int
    RH	:int
    Ws:int
    Rain:float
    FFMC	:float
    DMC	:float
    ISI	:float
    Classes	:int
    Region:float