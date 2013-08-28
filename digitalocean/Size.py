import requests

class Size(object):
    def __init__(self, client_id="", api_key=""):
        self.client_id = client_id
        self.api_key = api_key
        self.name = None
        self.id = None

    def all(self):
        """
            Get all Sizes
        """
        payload = {'client_id': self.client_id, 'api_key': self.api_key}
        r = requests.get("https://api.digitalocean.com/sizes/", params=payload)
        return r.json()

        
