"""
Working with files
"""
from typing import Annotated

from fastapi import FastAPI, File, UploadFile
from fastapi.responses import HTMLResponse

app = FastAPI()

# # ORIGINAL
# @app.post('/files/')
# async def create_file(file: Annotated[bytes, File()]):
#     return {"file_size": len(file)}


# @app.post('/uploadfile/')
# async def create_upload_file(file: UploadFile):
#     return {"filename": file.filename}


# # OPTIONAL FILE PARAMETER
# @app.post('/files/')
# async def create_file(file: Annotated[bytes | None, File()] = None):
#     if not file:
#         return {"message": "No file sent."}
#     else:
#         return {"file_size": len(file)}


# @app.post('/uploadfile/')
# async def create_upload_file(file: UploadFile | None = None):
#     if not file:
#         return {"message": "No upload file sent."}
#     else:
#         return {"filename": file.filename}


# # FILE WITH ADDITIONAL METADATA
# @app.post('/files/')
# async def create_file(file: Annotated[bytes, File(description="A file read as bytes")]):
#     return {"file_size": len(file)}


# @app.post('/uploadfile/')
# async def create_upload_file(file: Annotated[UploadFile, File(description="A file read as UploadFile")]):
#     return {"filename": file.filename}


# WORKING WITH MULTIPLE FILES
@app.post('/files/')
async def create_files(files: Annotated[list[bytes], File()]):
    return {"file_sizes": [len(file) for file in files]}


@app.post('/uploadfiles')
async def create_upload_files(files: list[UploadFile]):
    return {"filenames": [file.filename for file in files]}


@app.get('/')
async def main():
    content = """
<body>
<form action="/files/" enctype="multipart/form-data" method="post">
<input name="files" type="file" multiple>
<input type="submit">
</form>
<form action="/uploadfiles/" enctype="multipart/form-data" method="post">
<input name="files" type="file" multiple>
<input type="submit">
</form>
</body>
"""
    return HTMLResponse(content=content)
