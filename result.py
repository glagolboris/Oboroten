import sys
from io import BytesIO
import requests
from PIL import Image

class Main:
    def __init__(self, zoom, longitude, lattitude):
        self.zoom = zoom
        self.longitude = longitude
        self.lattitude = lattitude

    def get_result(self):

        try:
            map_params = {
                "ll": ",".join([self.longitude, self.lattitude]),
                "z": self.zoom,
                "l": "map"
            }

            map_api_server = "http://static-maps.yandex.ru/1.x/"
            response = requests.get(map_api_server, params=map_params)

            return BytesIO(response.content)

        except Exception as e:
            print(e)


    def show_result(self, content):
        Image.open(content).show()

