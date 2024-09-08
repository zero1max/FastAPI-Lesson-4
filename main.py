from fastapi import FastAPI, Header
from fastapi.responses import Response, RedirectResponse, JSONResponse
from typing import Annotated, Any
from pydantic import BaseModel, EmailStr
from enum import Enum

app = FastAPI()

# @app.get("/items/")
# async def items_show(
#     user_agent: Annotated[str | None , Header()] = None,
#     accept_language: Annotated[str | None, Header()] = "en"
#     ):
#     return {
#         "User-agent": user_agent,
#         "Accept language": accept_language
#     }

# ------------------------------------------------------------------

class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None
    tags: list[str] = []

@app.post("/items/", response_model=Item)
async def create_item(item: Item) -> Item:
    return {'message': 'Created'}


@app.get("/items/", response_model=list[Item], response_model_exclude_unset=True)
async def get_item() -> Any:
    return [
        Item(name='Apple', price=23.00),
        Item(name="Banana", price=25.00),
        {'name': 'Cherry', 'price': 20.00}
    ]

# -----------------------------------------------------------------------

# class UserBase(BaseModel):
#     username: str
#     email: EmailStr
#     full_name: str | None = None

# class UserIn(UserBase):
#     password: str

# class SocialMedias(Enum):
#     youtube = "youtube"
#     telegram = 'telegram'
#     github = 'github'

# @app.post("/users/", response_model=UserBase)
# async def create_user(user_data: UserIn):
#     # Validate and Save the use to the DB
#     return user_data


# @app.get("/sms/")
# async def redirect_social_media(social_media: SocialMedias | None = None) -> Response:
#     if social_media == 'telegram':
#         return RedirectResponse(url="https://t.me/zero_1_max")
#     elif social_media == 'youtube':
#         return RedirectResponse(url='https://youtube.com/@zero_1_max')
#     elif social_media == 'github':
#         return RedirectResponse(url='https://github.com/zero1max')
#     else:
#         return JSONResponse(
#             {
#                 'message':"Pass the social media query to get teleported"
#             }
#         )