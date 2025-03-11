import os
from pprint import pprint
import pynetbox

NETBOX_API = os.getenv('NETBOX_API')
NETBOX_TOKEN = os.getenv('NETBOX_TOKEN')
TENANT = os.getenv('TENANT')

nb = pynetbox.api(NETBOX_API, NETBOX_TOKEN)

result = nb.tenancy.tenants.get(name=TENANT)

pprint(dict(result), indent=4)
