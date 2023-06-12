from fastapi import Depends, HTTPException, status

from app.utils import AppModel

from ..service import Service, get_service
from . import router


class CreateAdvertisementRequest(AppModel):
    type: str
    price: int
    address: str
    area: float
    rooms_count: int
    description: str


class CreateAdvertisementResponse(AppModel):
    id: str


@router.post(
    "/shanyraks/",
    response_model=CreateAdvertisementResponse,
    status_code=status.HTTP_201_CREATED,
)
def create_advertisement(
    ad: CreateAdvertisementRequest,
    svc: Service = Depends(get_service),
) -> CreateAdvertisementResponse:
    # Assuming you generate an ID for the advertisement
    ad_id = svc.repository.create_shanyrak(ad.dict())

    return CreateAdvertisementResponse(id=ad_id)
