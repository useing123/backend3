from fastapi import APIRouter, Depends, HTTPException, status
from bson.objectid import ObjectId

from app.utils import AppModel
from ..service import Service, get_service
from . import router


class AdvertisementResponse(AppModel):
    _id: str
    type: str
    price: int
    address: str
    area: float
    rooms_count: int
    description: str
    user_id: str


@router.get("/shanyraks/{id}", response_model=AdvertisementResponse)
def get_advertisement(
    id: str,
    svc: Service = Depends(get_service),
) -> AdvertisementResponse:
    ad = svc.repository.get_advertisement_by_id(id)
    if ad is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Advertisement not found",
        )
    return AdvertisementResponse(**ad)
