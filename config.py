class Config:
    SECRET_KEY = 'B!1w8NAt1T^%kvhUI*S^'


class DevelopmentConfig(Config):
    DEBUG = True
    MYSQL_HOST = '192.168.0.240'
    MYSQL_USER = 'dani'
    MYSQL_PASSWORD = ''
    MYSQL_DB = 'PowerBI'


config = {
    'development': DevelopmentConfig
}

class BaseConfig(object):

    # Can be set to 'MasterUser' or 'ServicePrincipal'
    AUTHENTICATION_MODE = 'MasterUser'

    # Workspace Id in which the report is present
    WORKSPACE_ID = 'cc70026a-4268-4078-acab-bb2432884811'
    
    # Report Id for which Embed token needs to be generated
    REPORT_ID = '479da02a-e70c-475b-b087-131ddcedeab9'

    ROLE_ID = 'Del Vigo'

    DATASET_ID = '0317344f-bf8a-4a6f-8a83-8d3c2f190c8c'
    
    # Id of the Azure tenant in which AAD app and Power BI report is hosted. Required only for ServicePrincipal authentication mode.
    TENANT_ID = '892246bd-c9f8-4b64-92e1-08e56825da42'
    
    # Client Id (Application Id) of the AAD app
    CLIENT_ID = '0d938a7d-e344-4038-b8fb-deebffbfb2b4'
    
    # Client Secret (App Secret) of the AAD app. Required only for ServicePrincipal authentication mode.
    CLIENT_SECRET = ''
    
    # Scope Base of AAD app. Use the below configuration to use all the permissions provided in the AAD app through Azure portal.
    SCOPE_BASE = ['https://analysis.windows.net/powerbi/api/.default']
    
    # URL used for initiating authorization request
    AUTHORITY_URL = 'https://login.microsoftonline.com/organizations'
    
    # Master user email address. Required only for MasterUser authentication mode.
    POWER_BI_USER = 'powerbi@golmar.es'
    
    # Master user email password. Required only for MasterUser authentication mode.
    POWER_BI_PASS = 'G01m@rP0w3rB1'