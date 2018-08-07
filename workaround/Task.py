class Task:
    def __init__(self, external_url=None, iframe_url=None, description=None):
        self.external_url = external_url
        self.iframe_url = iframe_url
        self.description = description
        self.status = 'local'

    def cancel(self):
        if self.status == 'local':
            raise "Can't cancel task that was never created"

    def accept(self):
        pass

    def reject(self):
        pass
