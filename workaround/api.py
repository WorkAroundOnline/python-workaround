import os
import requests
import json

api_base = 'https://api.workaround.online'
api_key = None

def set_base_url(url):
    global api_base
    api_base = 'http://localhost:3010'

def set_api_key(key):
    global api_key
    api_key = key

def test_connection():
    '''
    Tests connection, returns true if connected
    '''
    url = '{}/v1'.format(api_base)
    response = requests.get(url)
    return response.json()

def create_quote(task_group=None, task_count=None):
    '''
    Get information regarding a quote.
    '''
    url = '{}/v1/quote'.format(api_base)
    params = {
        'task_group': task_group,
        'task_count': task_count,
        'api_key': api_key
    }
    return requests.post(url, json=params).json()

def get_quote(quote=None):
    '''
    Get information regarding a quote.
    '''
    url = '{}/v1/quote'.format(api_base)
    params = {
        'api_key': api_key,
        'quote': quote
    }
    return requests.get(url, params=params).json()

def create_tasks(quote=None, task_group=None, tasks=None):
    '''
    Creates tasks for workers to perform.
    '''
    url = '{}/v1/task'.format(api_base)
    params = {
        'api_key': api_key,
        'quote': quote,
        'task_group': task_group,
        'tasks': tasks
    }
    return requests.post(url, json=params).json()

def get_task_status(task_numbers=None, quote=None, task_group=None):
    '''
    Gets the status for one or more tasks.
    '''
    url = '{}/v1/task'.format(api_base)
    params = {
        'api_key': api_key,
        'task_numbers[]': task_numbers,
        'quote': quote,
        'task_group': task_group
    }
    return requests.get(url, params=params).json()

def cancel_tasks(task_numbers=None, quote=None, task_group=None):
    '''
    Cancel tasks.
    '''
    url = '{}/v1/task'.format(api_base)
    params = {
        'api_key': api_key,
        'task_numbers': task_numbers,
        'quote': quote,
        'task_group': task_group
    }
    return requests.delete(url, json=params).json()

def get_billing():
    '''
    Get billing information for the connect account
    '''
    url = '{}/v1/billing'.format(api_base)
    params = {
        'api_key': api_key
    }
    return requests.get(url, params=params).json()

def report_task(fulfillment_ids=None, reject=None, accept=None):
    '''
    Report task as being correct or incorrect.
    '''
    url = '{}/v1/report'.format(api_base)
    params = {
        'api_key': api_key,
        'fulfillment_ids': fulfillment_ids,
        'reject': reject,
        'accept': accept
    }
    return requests.post(url, json=params).json()
