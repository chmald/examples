from azure.mgmt.resource import ResourceManagementClient
from azure.common.credentials import UserPassCredentials

subscription_id = 'subscription_id'

credentials = UserPassCredentials(
		'user@domain.com',
		'password',
		)

resource_client = ResourceManagementClient(
		credentials,
		subscription_id
		)

print 'Successfully logged in.'
