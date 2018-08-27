from .api_caller import CrabCaller


class Crab():
    def __init__(self, quantity, animal=['crab']):
        self.cc = CrabCaller()
        self.quantity = quantity

    def begin_show(self):
        url_list = self.cc.call_crabs(self.quantity)
        # self.show_crabs(url_list)
        return True
