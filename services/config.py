# Copyright (c) Microsoft Corporation.
# Licensed under the MIT license.

class BaseConfig(object):

    # Can be set to 'MasterUser' or 'ServicePrincipal'
    AUTHENTICATION_MODE = 'ServicePrincipal'

    # Workspace Id in which the report is present
    WORKSPACE_ID = '26a3baa8-52ca-41e1-9abb-8ef1999be7fc'
    
    # Report Id for which Embed token needs to be generated
    REPORT_ID = '92b721c3-64e9-433a-90d5-9403e7c24de8'
    
    # Id of the Azure tenant in which AAD app and Power BI report is hosted. Required only for ServicePrincipal authentication mode.
    TENANT_ID = '892246bd-c9f8-4b64-92e1-08e56825da42'
    
    # Client Id (Application Id) of the AAD app
    CLIENT_ID = '0d938a7d-e344-4038-b8fb-deebffbfb2b4'
    
    # Client Secret (App Secret) of the AAD app. Required only for ServicePrincipal authentication mode.
    CLIENT_SECRET = 'W9j7Q~HRp8GuQdJBgJXC2UuM8fD3WtP0mzNGN'
    
    # Scope Base of AAD app. Use the below configuration to use all the permissions provided in the AAD app through Azure portal.
    SCOPE_BASE = ['https://analysis.windows.net/powerbi/api/.default']
    
    # URL used for initiating authorization request
    AUTHORITY_URL = 'https://login.microsoftonline.com/organizations'
    
    # Master user email address. Required only for MasterUser authentication mode.
    POWER_BI_USER = ''
    
    # Master user email password. Required only for MasterUser authentication mode.
    POWER_BI_PASS = ''