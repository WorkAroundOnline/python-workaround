from workaround import api
import workaround.Client as Client
import psycopg2

api.set_base_url('http://localhost:3010')

wao = Client(api_key='PAPI_TEST_KEY')

def test_connection():
    wao.test_connection()
