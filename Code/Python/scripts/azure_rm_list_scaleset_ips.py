from azure.mgmt.resource import ResourceManagementClient
from azure.common.credentials import ServicePrincipalCredentials
from azure.mgmt.compute import ComputeManagementClient
from azure.mgmt.network import NetworkManagementClient
from azure.mgmt.network.operations import NetworkInterfacesOperations

subscription_id = 'subscriptionID'

credentials = ServicePrincipalCredentials(
		client_id = 'client_id',
		secret = 'client_secret',
		tenant = 'ad tenant'
		)

resource_client = ResourceManagementClient(credentials, subscription_id)
compute_client = ComputeManagementClient(credentials, subscription_id)

print('Successfully logged in.')

print('Listing NICs:')

nic_client = NetworkManagementClient(credentials, subscription_id)
nic_list = nic_client.network_interfaces.list_virtual_machine_scale_set_network_interfaces('vmscalesetname', 'vmname')
for curr_nic in nic_list:
    for ip_config in curr_nic.ip_configurations:
        print('\tPublic IP: {}'.format(ip_config.public_ip_address))
        print('\tPrivate IP: {}'.format(ip_config.private_ip_address))