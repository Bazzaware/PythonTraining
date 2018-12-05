import requests
from location import Location


class FileSource:
    def __init__(self, filename):
        self.filename = filename

    def fetch(self):
        places = []
        with open(self.filename) as h:
            for line in h:
                line = line.rstrip()
                if line == "":
                    continue
                name, longitude, latitude = line.split('\t')
                places.append(Location(name, float(longitude), float(latitude)))
        return places


class NetworkSource:
    def __init__(self, url):
        self.url = url

    def fetch(self):
        places = []
        response = requests.get(self.url)
        if response.status_code != 200:
            raise Exception("url {!r} failed with status code {}".format(self.url, response.status_code))
        for line in response.text.splitlines():
            line = line.rstrip()
            if line == "":
                continue
            name, latitude, longitude = line.split('\t')
            places.append(Location(name, float(longitude), float(latitude)))
        return places



from math import cos, asin, sqrt

class LocationStore:

    def __init__(self):
        self._places = {}

    def fetch_places(self, source):
        places = source.fetch()
        for place in places:
            self._places[place.name] = place

    def get_place(self, name):
        return self._places[name]

    def all_names(self):
        return list(self._places.keys())

    def distance(self, name1, name2):
        """Haversine geographic distance. Returns distance in kilometres."""
        loc1 = self.get_place(name1)
        loc2 = self.get_place(name2)
        return self._distance(loc1, loc2)

    def _distance(self, location1, location2):
        lat1 = location1.latitude
        lat2 = location2.latitude
        lon1 = location1.longitude
        lon2 = location2.longitude

        p = 0.017453292519943295     #Pi/180
        a = 0.5 - cos((lat2 - lat1) * p)/2 + cos(lat1 * p) * cos(lat2 * p) * (1 - cos((lon2 - lon1) * p)) / 2
        return 12742 * asin(sqrt(a))


if __name__ == '__main__':
    source = NetworkSource('http://voidspace.org.uk/coords.txt')
    store = LocationStore()
    store.fetch_places(source)
    print(store.distance("Marlow", "Redruth"))