
from src.gununmaclari import *
from src.site.footballpredictionsnet import *


import config
config = config.Config('./config/config.py')


def __main__():
    dailymatches = dailymatch()
    footballpredictionsnet(dailymatches)

__all__ = ["__main__"]