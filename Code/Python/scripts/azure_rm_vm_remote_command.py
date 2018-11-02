from azure.common.credentials import ServicePrincipalCredentials
from azure.mgmt.compute import ComputeManagementClient

subscription_id = 'subscriptionID'

credentials = ServicePrincipalCredentials(
		client_id = 'client_id',
		secret = 'client_secret',
		tenant = 'ad tenant'
		)

compute_client = ComputeManagementClient(credentials, subscription_id)

vm_name = "azure_vm_name"
resource_group = "azure_resource_groupe"

print('Successfully logged in.')

run_command_params = {
    'commandId': 'RunPowerShellScript',
    'script': [
        'Import-Module WebAdministration;',
        'Start-WebAppPool -Name "MyWebAppPool"'
    ]
}

cmd_obj = compute_client.virtual_machines.run_command(resource_group, vm_name, run_command_params, polling=True)
cmd_obj.wait()