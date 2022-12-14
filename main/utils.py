import os
from uuid import uuid4

def rename_imagefile_to_uuid(instance, filename):
        upload_to = f'temp/'
        ext = filename.split('.')[-1]
        uuid = uuid4().hex
        filename = '{}.{}'.format(uuid, ext)
        return os.path.join(upload_to, filename)



def rename_userimagefile_to_uuid(instance, filename):
        upload_to = f'user_temp_filter/'
        ext = filename.split('.')[-1]
        uuid = uuid4().hex
        filename = '{}.{}'.format(uuid, ext) 
        return os.path.join(upload_to, filename)