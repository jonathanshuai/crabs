from .api_caller import caller as crabcaller


class Crab():
    def call_crabs(self):
        crabcaller.call()
        return True
