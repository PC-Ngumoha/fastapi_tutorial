"""
Form Models
"""
from typing import Annotated

from fastapi import FastAPI, Form
from pydantic import BaseModel

app = FastAPI()


class FormData(BaseModel):
    username: str
    password: str

    # model_config = {"extra": "forbid"}


@app.post('/login/')
async def login(form_data: Annotated[FormData, Form()]):
    return {"form_data": form_data}
