from azure.storage.blob import (
    BlockBlobService,
    ContainerPermissions
)
from datetime import datetime, timedelta

ACCOUNT_NAME ="account_name"
ACCOUNT_KEY ="account_key"
CONTAINER_NAME='container_name'

block_blob_service = BlockBlobService(account_name=account_name, account_key=account_key)

sas_url = block_blob_service.generate_container_shared_access_signature(
            CONTAINER_NAME,
            ContainerPermissions.WRITE,
            datetime.utcnow() + timedelta(hours=1),
        )

print sas_url
