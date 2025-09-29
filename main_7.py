"""
Declare Request Example Data
"""
from typing import Annotated

from fastapi import FastAPI, Body
from pydantic import BaseModel, Field

app = FastAPI()

# Additional JSON Schema data
# class Item(BaseModel):
#     name: str
#     description: str | None = None
#     price: float
#     tax: float | None = None

#     model_config = {
#         "json_schema_extra": {
#             "examples": [
#                 {
#                     "name": "Foo",
#                     "description": "A very nice item",
#                     "price": 35.4,
#                     "tax": 3.2,
#                 }
#             ]
#         }
#     }

# Field additional arguments
# class Item(BaseModel):
#     name: str = Field(examples=["Foo"])
#     description: str | None = Field(
#         default=None, examples=["A very nice item"])
#     price: float = Field(examples=[35.4])
#     tax: float | None = Field(default=None, examples=[3.2])


# @app.put('/items/{item_id}')
# async def update_item(item_id: int, item: Item):
#     results = {"item_id": item_id, "item": item}
#     return results


# Body with examples
class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None


@app.put('/items/{item_id}')
async def update_item(
    item_id: int,
    item: Annotated[
        Item,
        Body(
            examples=[
                {
                    "name": "Foo",
                    "description": "A very nice item",
                    "price": 35.4,
                    "tax": 3.2
                }
            ]
        )
    ]
):
    results = {"item_id": item_id, "item": Item}
    return results
