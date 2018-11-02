from azure.mgmt.resource import ResourceManagementClient
from azure.common.credentials import ServicePrincipalCredentials

subscription_id = 'subscriptionID'

credentials = ServicePrincipalCredentials(
		client_id = 'client_id',
		secret = 'client_secret',
		tenant = 'ad tenant'
		)

resource_client = ResourceManagementClient(
		credentials,
		subscription_id
		)

print('Successfully logged in.')
