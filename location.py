class Location:
    def __init__(self,name,longitude,latitude):
        if not isinstance(name,str):
            raise TypeError("Name must be a string. {!r}".format(name))
        self._name = name
        if not isinstance(longitude,(float,int)):
            raise TypeError("longitude must be a float {!r}".format(longitude))
        self._longitude = longitude
        if not isinstance(latitude,(float,int)):
            raise TypeError("latitude must be a float {!r}".format(latitude))
        self._latitude = latitude

    def __repr__(self):
        return 'Location({!r},{!r},{!r})'.format(self.name, self.longitude, self.latitude)

        
    
    @property
    def name(self):
        return self._name

    @property
    def longitude(self):
        return self._longitude
    
    @property
    def latitude(self):
        return self._latitude
