from fastapi import APIRouter, HTTPException, status, UploadFile
from schema import *
from services.file import FileService
from fastapi.responses import FileResponse

router = APIRouter(tags=['Files'])

@router.post("/files")
async def upload_files(request: List[UploadFile]):
    try:
        with FileService() as service:
            service.add_file(request)
        return {'Success':True}
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))

@router.get("/files")
async def get_files():
    with FileService() as service:
        files = service.get_all()
    return [File.from_orm(s) for s in files]

@router.get("/files/{id}")
async def download_file(id : int):
    try:
        with FileService() as service:
            file = service.get_by_id(id)
        return FileResponse(path=file.path, filename=file.file_name, media_type='multipart/form-data')
    except:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Файл не найден")

@router.delete("/files/{id}")
async def delete_file(id : int):
    try:
        with FileService() as service:
            file = service.delete_file(id)
        return {'Success':True}
    except:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Файл не найден")

