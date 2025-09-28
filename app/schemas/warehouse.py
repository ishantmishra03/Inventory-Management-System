from pydantic import BaseModel

class WareHouseBase(BaseModel):
    name: str
    location: str

class WareHouseCreate(WareHouseBase):
    pass

class WareHouseUpdate(WareHouseBase):
    pass

class WareHouseOut(BaseModel):
    id: int
    name: str
    location: str
    created_at: str
    updated_at: str

    class Config:
        from_attributes = True