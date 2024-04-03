import requests


class APIClient:
    def __init__(self, url_base):
        self.url_base = url_base

    def send_post(self, url, body):
        full_url = self.url_base + url
        response = requests.post(full_url, json=body)
        return response


class APIError(Exception):
    def __init__(self, message, status_code=None):
        self.message = message
        self.status_code = status_code

    def __str__(self):
        if self.status_code:
            return f"{self.message} (Status Code: {self.status_code})"
        else:
            return self.message
