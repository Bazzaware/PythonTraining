class Source():
    def __init_(self,filename):

class FileSource(Source):
    def __init__(self, filename):
        self.filename = filename

    def fetch(self):
        with open(self.filename) as h:
            return self._handle_lines(h)


class NetworkSource(Source):
    def __init__(self, url):
        self.url = url

    def fetch(self):
        response = requests.get(self.url)
        if response.status_code != 200:
            raise Exception("url {!r} failed with status code {}".format(self.url, response.status_code))
        lines = response.text.splitlines()
        return self._handle_lines(lines)
