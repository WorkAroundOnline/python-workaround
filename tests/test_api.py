from workaround import api
import psycopg2

api.set_base_url('http://localhost:3010')
api.set_api_key('PAPI_TEST_KEY')

def test_connection():
    api.test_connection()

def test_create_quote():
    quote1 = api.create_quote()
    assert(isinstance(quote1['quote_id'], str))

def test_get_quote():
    quote1 = api.create_quote()
    assert(isinstance(quote1['quote_id'], str))
    quote2 = api.get_quote(quote=quote1['quote_id'])
    assert(isinstance(quote2['quote_id'], str))

def test_create_tasks():
    quote1 = api.create_quote()
    response = api.create_tasks(quote=quote1['quote_id'], tasks=[
        { 'meta': { 'id': 1 }, 'external_url': 'https://google.com' },
        { 'meta': { 'id': 2 }, 'external_url': 'https://google.com' }
    ])
    assert(isinstance(response['tasks'], list))

def test_get_task_status():
    quote1 = api.create_quote()
    tasks = api.create_tasks(quote=quote1['quote_id'], tasks=[
        { 'meta': { 'id': 1 }, 'external_url': 'https://google.com' },
        { 'meta': { 'id': 2 }, 'external_url': 'https://google.com' }
    ])['tasks']
    response = api.get_task_status(task_numbers=[t['task_number'] for t in tasks])
    for t in response['tasks']:
        assert(t['status'] == 'incomplete')

def test_cancel_tasks():
    quote1 = api.create_quote()
    tasks = api.create_tasks(quote=quote1['quote_id'], tasks=[
        { 'meta': { 'id': 1 }, 'external_url': 'https://google.com' },
        { 'meta': { 'id': 2 }, 'external_url': 'https://google.com' }
    ])['tasks']
    cancel_response = api.cancel_tasks(task_numbers=[t['task_number'] for t in tasks])
    response = api.get_task_status(task_numbers=[t['task_number'] for t in tasks])
    for t in response['tasks']:
        assert(t['status'] == 'cancelled')

def test_get_billing():
    billing1 = api.get_billing()
    assert(isinstance(billing1['account_credit'], float) or isinstance(billing1['account_credit'], int) )

# There's no way to complete tasks via the partner api currently, so this
# method will have to be manually tested
# def test_report_task():
#     pass
