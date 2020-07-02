# Email Settings
EMAIL_HOST = 'HOST_ADDRESS'

EMAIL_PORT = 587

EMAIL_HOST_USER = 'USERNAME'

EMAIL_HOST_PASSWORD = 'PASSWORD'

EMAIL_USE_TLS = True


# VATUSA Settings
ULS_KEY = {"alg":"HS256","use":"sig","kty":"oct","k":"NotARealULSKey"}

API_KEY = 'NotARealAPIKey'


# General Website Settings
RESOURCE_CATEGORIES = ['VRC', 'vSTARS', 'vERAM', 'vATIS', 'SOP', 'LOA', 'MAVP', 'Misc']


# ARTCC Geography
ARTCC_BOUNDARY = [[0, 0], [0, 0]]   # TMU Boundary JSON from VATUSA website

MAP_CENTER = ['Decimal Representation of Latitude', 'Decimal Representation of Longitude']

AIRFIELDS = ['IATA', 'IATA', '...']
