from fastapi import Depends, Response, HTTPException, status
from app.auth.adapters.jwt_service import JWTData
from app.auth.router.dependencies import parse_jwt_user_data
from app.utils import AppModel

from ..service import Service, get_service
from . import router


class UpdateUserRequest(AppModel):
    phone: str
    name: str
    city: str


@router.patch("/users/me")
def update_user_data(
    input: UpdateUserRequest,
    jwt_data: JWTData = Depends(parse_jwt_user_data),
    svc: Service = Depends(get_service),
) -> dict[str, str]:
    user_id = jwt_data.user_id
    svc.repository.update_user_data(user_id, input.dict())

    return Response(status_code=200)


class UpdateAdvertisementRequest(AppModel):
    type: str
    price: int
    address: str
    area: float
    rooms_count: int
    description: str


@router.patch("/shanyraks/{id}")
def update_advertisement(
    id: str,
    ad: UpdateAdvertisementRequest,
    svc: Service = Depends(get_service),
) -> Response:
    advertisement = svc.repository.get_advertisement_by_id(id)
    if not advertisement:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Advertisement not found",
        )

    svc.repository.update_advertisement_data(id, ad.dict())

    return Response(status_code=status.HTTP_200_OK)
