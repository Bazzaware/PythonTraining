from location import Location

from math import cos, asin, sqrt
from formatter import create_formatter

import requests

class LocationStore:

    def __init__(self, formatter_name):
        self._formatter = create_formatter(formatter_name)
        self._places = {}

    def __getitem__(self, name):
        #print("Fetching name" , name)
        return self._places[name]

    def __setitem__(self, name, value):
       # print("Setting name ",name)
        self._places[name] = value

    def __delitem__(self, name):
        del self._places[name]

    def __len__(self):
        return len(self._places)

    def __contains__(self, name):
        return name in self._places

    def __iter__(self):
        for item in self._places.values():
            yield item

    def fetch_places(self, source):
        places = source.fetch()
        for place in places:
            self[place.name] = place

    def get_place(self, name):
        return self[name]

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

    def display_locations(self):
        self._formatter.headings(['Name', 'Longitude', 'Latitude'])
        for name in self.all_names():
            place = self[name]
            rowdata = [place.name,place.longitude,place.latitude]
            self._formatter.row(rowdata)


class Source():
    def fetch(self):
        raise NotImplementedError

    def _handle_lines(self, Response):
        places = []
        for line in Response:
            line = line.rstrip()
            if line == "":
                continue
            name, latitude, longitude = line.split('\t')
            places.append(Location(name, float(longitude), float(latitude)))
        return places
    

class NetworkSource(Source):
    def __init__(self, url):
        self.url = url

    def fetch(self):
        response = requests.get(self.url)
        if response.status_code != 200:
            raise Exception("url {!r} failed with status code {}".format(self.url, response.status_code))
        linesFromSource = response.text.splitlines()
        return self._handle_lines(linesFromSource)
        
        
class FileSource(Source):
    def __init__(self, filename):
        self.filename = filename

    def fetch(self):
        with open(self.filename) as contents:
            return self._handle_lines(contents)

if __name__ == '__main__':
    #store = LocationStore("html")
    store = LocationStore("txt")
    #source = NetworkSource('http://www.voidspace.org.uk/coords.txt')
    source = FileSource("data/coords.txt")
    store.fetch_places(source)
    print(store.distance("Marlow", "Redruth"))
    store.display_locations()
    
