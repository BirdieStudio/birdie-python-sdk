from pydantic import BaseModel, Field
from typing import List, Any, Optional


class ResultBase(BaseModel):
    name: str = Field(...)


class ResultText(ResultBase):
    text: str = Field(...)

class ResultPDF(ResultBase):
    content: str = Field(...)

class ResultImage(ResultBase):
    content: str = Field(...)

class ResultHTML(ResultBase):
    content: str = Field(...)

class ResultModel(BaseModel):
    content: str = Field(...)
    state: Optional[dict] = Field(None)
    parts: Optional[Any] = Field(None)
    step: int = Field(...)
    result: Optional[List[ResultText|ResultPDF|ResultHTML|ResultImage]] = Field([])
    final_result: bool = Field(False)
