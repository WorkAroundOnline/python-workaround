import os
import requests

api_base = 'https://api.workaround.online'

try:
    api_base = os.env['API_BASE_URL']
except:
    pass

def get_quote(task_group=None, task_count=None):
    url = '{}/v1/quote'.format(api_base)
    
