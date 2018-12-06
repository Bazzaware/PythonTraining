
def typedproperty(name, type):
    variable = "_" + name
    @property
    def function(self):
        return getattr(self, variable)
    @function.setter
    def function(self, value):
        if not isinstance(value, type):
            raise TypeError("Expected type {!r}, got {!r}".format(type, value))
        setattr(self, variable, value)
    return function
        

class Location:
    name = typedproperty('name', str)
    longitude = typedproperty('longitude', float)
    latitude = typedproperty('latitude', float)

    def __init__(self, name, longitude, latitude):
        self.name = name
        self.longitude = longitude
        self.latitude = latitude
