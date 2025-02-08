from enum import Enum

from typing import Any 
from pydantic import BaseModel

class Status(Enum): 
    SUCCESS = "SUCCESS"
    FAILED = "FAILED"


class ResponseModel(BaseModel): 
    result: Any = None
    message: str = None 
    status: Status