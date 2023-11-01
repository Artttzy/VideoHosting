from schema import *
from schema import File as SchemaFile
from db.models import File as ModelFile
from db.connection import Session
import os, shutil
from fastapi import UploadFile

class CreateFileException(Exception):
    ...

class FileNotFound(Exception):
    ...

class FileService:
    def __enter__(self):
        self.session = Session()
        return self

    def __exit__(self, *args):
        self.session.commit()

    def add_file(self, files: List[UploadFile]):
        try:
            path = f'./videos'
            for file in files: 
                f = file.file.read()
                with open(f'{path}/{file.filename}', 'wb') as v:
                    v.write(f)
                model = ModelFile(**{'file_name': file.filename, 'path':f'{path}/{file.filename}'})
                self.session.add(model)
        except Exception as e:
            raise CreateFileException(str(e))
        
    def get_all(self):
        files = self.session.query(ModelFile).all()
        return files

    def get_by_id(self, id: int):
        file = self.session.query(ModelFile).where(ModelFile.id==id).one_or_none()
        if file:
            return file
        else:
            raise FileNotFound

    def delete_file(self, id: int):
        file = self.get_by_id(id=id)
        self.session.delete(file)