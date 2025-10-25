from pydantic import BaseModel, Field
from typing import List


class ResultBase(BaseModel):
    name: str = Field(...)


class ResultText(ResultBase):
    text: str = Field(...)


class ResultModel(BaseModel):
    result: List[ResultText] = Field(...)
    final_result: bool = Field(False)
