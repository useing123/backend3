from typing import Any

from fastapi import Depends
from pydantic import Field

from app.utils import AppModel

from ..adapters.jwt_service import JWTData
from ..service import Service, get_service
from . import router
from .dependencies import parse_jwt_user_data


class GetMyAccountResponse(AppModel):
    id: Any = Field(alias="_id")
    email: str
    phone: str
    name: str
    city: str


@router.get("/users/me", response_model=GetMyAccountResponse, name="router_get_user")
def get_my_account(
    jwt_data: JWTData = Depends(parse_jwt_user_data),
    svc: Service = Depends(get_service),
) -> GetMyAccountResponse:
    user = svc.repository.get_user_by_id(jwt_data.user_id)
    return GetMyAccountResponse(
        id=user["_id"],
        email=user["email"],
        phone=user.get("phone", ""),
        name=user.get("name", ""),
        city=user.get("city", "")
    )
