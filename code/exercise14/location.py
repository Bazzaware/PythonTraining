
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

    def __repr__(self):
        return 'Location({!r}, {!r}, {!r})'.format(self.name, self.longitude, self.latitude)

    def __str__(self):
        return '<Location name: {}, longitude: {}, latitude: {}>'.format(self.name, self.longitude, self.latitude)

    def __eq__(self, other):
        if not isinstance(other, Location):
            return False
        return self.name == other.name and self.longitude == other.longitude and self.latitude == other.latitude

    def __iter__(self):
        for field in 'name', 'longitude', 'latitude':
            yield getattr(self, field)

    @property
    def name(self):
        return self._name

    @property
    def longitude(self):
        return self._longitude

    @property
    def latitude(self):
        return self._latitude