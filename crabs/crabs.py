import io

from PIL import Image

from matplotlib import pyplot as plt

import requests

from .api_caller import CrabCaller

class Crab():
    def __init__(self, quantity):
        self.cc = CrabCaller()
        self.quantity = quantity

    def begin_show(self):
        url_list = self.cc.call_crabs(self.quantity)
        self.show_crabs(url_list)

    def invite_friends(self, friend):
        url_list = self.cc.call_friends(self.quantity, friend)
        self.show_crabs(url_list)

    def show_crabs(self, url_list):
        for url in url_list:
            data = requests.get(url).content
            img = Image.open(io.BytesIO(data))
            plt.figure()
            plt.imshow(img)
            plt.axis('off')
            plt.tight_layout()
        plt.show()
