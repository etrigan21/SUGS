from typing import List, Optional
from pydantic import BaseModel 

class SensorQueryModel(BaseModel):

    columns: List[str]
    deviceType: str 
    #This query will be akin to the following: 
    # query = "param1 >= 0 AND param2 <= 5"
    query: str = None
    limit: int = None