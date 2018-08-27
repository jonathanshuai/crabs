import io

from PIL import Image

from matplotlib import pyplot as plt

import requests

from api_caller import CrabCaller


class Crab():
    def __init__(self):
        self.cc = CrabCaller()

    def call_crabs(self):
        # cc.call()
        return True

    def show_crabs(self, url_list):
        for url in url_list:
            data = requests.get(url).content
            img = Image.open(io.BytesIO(data))
            plt.imshow(img)
            plt.show()
