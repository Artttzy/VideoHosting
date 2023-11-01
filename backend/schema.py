from pydantic import BaseModel
from typing import List


class ORM(BaseModel):
    class Config:
        from_attributes=True
        orm_mode=True

class File(ORM):
    file_name: str
    path: str

