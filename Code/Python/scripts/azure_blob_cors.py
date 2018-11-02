from azure.storage.blob import (
    BlockBlobService,
    ContainerPermissions
)
from azure.storage.models import CorsRule
from datetime import datetime, timedelta

ACCOUNT_NAME ="account_name"
ACCOUNT_KEY ="account_key"
CONTAINER_NAME='container_name'

block_blob_service = BlockBlobService(account_name=ACCOUNT_NAME, account_key=ACCOUNT_KEY)

sas_url = block_blob_service.generate_container_shared_access_signature(
            CONTAINER_NAME,
            ContainerPermissions(True, True, True, True, ''),
            datetime.utcnow() + timedelta(weeks=52),
        )

print sas_url
print "---------------------------------------------"
url = ['*']
method =['GET','POST','PUT','OPTIONS']

corslist = []
corslist.append(CorsRule(url,method,allowed_headers=['*'],max_age_in_seconds=20,exposed_headers=['*']))

block_blob_service.set_blob_service_properties(None,None,None,corslist,"2015-02-21",None)

print block_blob_service.get_blob_service_properties()
