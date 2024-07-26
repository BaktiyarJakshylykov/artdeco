from pydantic import BaseModel
from typing import Optional, List


class CatalogList(BaseModel):
    id: int
    code: str
    image_url: str

    class Config:
        from_attributes = True


class CatalogImage(BaseModel):
    id: int
    image_url: Optional[str] = None

    class Config:
        from_attributes = True


class CatalogDetail(BaseModel):
    id: int
    code: str
    image_url: str
    article: str
    width: str
    height: str
    aliquet: int
    description: Optional[str] = None
    image_url: str
    images: List[CatalogImage] = []

    class Config:
        from_attributes = True
