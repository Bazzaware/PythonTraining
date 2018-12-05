
class Location:

    def __init__(self, name, longitude, latitude):
        if not isinstance(name, str):
            raise TypeError('name should be a string: {!r}'.format(name))
        if not isinstance(longitude, float):
            raise TypeError('longitude should be a float: {!r}'.format(longitude))
        if not isinstance(latitude, float):
            raise TypeError('latitude should be a float: {!r}'.format(name))
        self._name = name
        self._longitude = longitude
        self._latitude = latitude

    @property
    def name(self):
        return self._name

    @property
    def longitude(self):
        return self._longitude

    @property
    def latitude(self):
        return self._latitude