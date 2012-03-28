import urllib, urllib2, json

class PGPException(Exception):
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return repr(self.value)

class PyGooglePlaces:
    def __init__(self, api_key=""):
        """
        @api_key is required

        Returns a PyGooglePlaces object
        """
        if not api_key == "":
            self.API_KEY = api_key
        else:
            raise PGPException("API Key is required.")

    def search(self, location="", radius=100, sensor="true", keyword="", language="en", name="", types=""):
        """
        Searches for places.

        @location is latitude and longitude seperated by comma, e.g. "12.123,56.234"
        @sensor is true or false.
        @radius is specified in meters.
        @language list of available languages - http://goo.gl/kVquC
        @types list of available types - http://goo.gl/IUJZr
        """
        base_url = "https://maps.googleapis.com/maps/api/place/search/json"
        params = urllib.urlencode(
                        {
                            'key': self.API_KEY, 
                            'location': location, 
                            'radius': radius, 
                            'sensor': sensor,
                            'keyword': keyword,
                            'language': language,
                            'name': name,
                            'types': types,
                        }
                    )
        response_json = urllib.urlopen(base_url + "?" + params)
        response = json.load(response_json)
        return response

    def getPlaceDetails(self, reference="", sensor="true", language="en"):
        """
        Gets place details by Reference

        @reference is required.
        @sensor is true or false.
        @language list of available languages - http://goo.gl/kVquC
        """
        base_url = "https://maps.googleapis.com/maps/api/place/details/json"
        params = urllib.urlencode(
                {
                    'key': self.API_KEY,
                    'reference': reference,
                    'sensor': sensor,
                    'language': language,
                }
            )
        response_json = urllib.urlopen(base_url + "?" + params)
        response = json.load(response_json)
        return response

