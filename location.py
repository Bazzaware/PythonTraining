class Location:
    def __init__(self,name,lon,lat):
        if not isinstance(name,str):
            raise TypeError("Name must be a string. {!r}".format(name))
        self._name = name
        if not isinstance(lon,(float,int)):
            raise TypeError("lon must be a float {!r}".format(lon))
        self._lon = lon
        if not isinstance(lat,(float,int)):
            raise TypeError("lat must be a float {!r}".format(lat))
        self._lat = lat

        @property
        def name(self):
            return self._name
        def lon(self):
            return self._lon
        def lat(self):
            return self._lat
