from azure.mgmt.resource import ResourceManagementClient
from azure.common.credentials import ServicePrincipalCredentials
from azure.mgmt.compute import ComputeManagementClient

subscription_id = 'subscriptionID'

credentials = ServicePrincipalCredentials(
		client_id = 'client_id',
		secret = 'client_secret',
		tenant = 'ad tenant'
		)

resource_client = ResourceManagementClient(credentials, subscription_id)
compute_client = ComputeManagementClient(credentials, subscription_id)

print('Successfully logged in.')

print('Listing VMs:')
for group in resource_client.resource_groups.list():
	for vm in compute_client.virtual_machines.list(group.name):
		print('\tVM: {}'.format(vm.name))
		print(vm)
		virtual_machine = compute_client.virtual_machines.get(group.name, vm.name)
		print(virtual_machine)
