class Client:
    def __init__(self, api_key=None):
        if not api_key:
            raise "api_key must be provided to Client"
        self.api_key = api_key

    def create_quote(self):
        pass

    def create_tasks(self, quote=None, tasks=None):
        if not quote:
            quote = self.create_quote()
        if not tasks:
            raise 'tasks are required'

