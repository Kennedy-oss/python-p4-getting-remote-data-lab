import requests  # This line imports the requests library
import json

class GetRequester:
    def __init__(self, url):
        self.url = url

    def get_response_body(self):
        response = requests.get(self.url)
        return response.content  # Returns the raw bytes of the response payload

    def load_json(self):
        # Assuming you've corrected this method as previously discussed
        response_body = self.get_response_body()
        return json.loads(response_body)  # Make sure json is imported if you're using it here
