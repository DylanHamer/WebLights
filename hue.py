"""
WebLights - Hue
Control Phillips Hue lights with WebLights
By Dylan Hamer
"""

import phue

class hueController(object):
    def __init__(self, ip):
        """Initialise controller with an IP address"""
        try:
            self.bridge = phue.Bridge(ip)  # Initialise connection to bridge
        except phue.PhueRequestTimeout:
            print("Failed to connect to bridge: {}".format(ip))
        
    def getDevices(self):
        devices = {}
        lights = self.bridge.lights  # Get all lights
        for light in lights:
            devices[light.name] = light  # Create a dictionary of light names and their objects
        return devices
