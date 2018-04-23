"""
WebLights - TPLink
Control TPLink bulbs and switches 
By Dylan Hamer
"""

from pyHS100 import SmartPlug, SmartBulb, Discover

class tplink:
    def __init__(self):
        pass
    
    def getDevices(self):
        for device in Discover.discover().values():
    
    

