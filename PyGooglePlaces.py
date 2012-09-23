import urllib, urllib2, json

class PGPException(Exception):
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return repr(self.value)

class PyGooglePlaces:
    base_url = 'base_url = "https://maps.googleapis.com/maps/api/place/'
    API_KEY = ""

    def __init__(self, api_key, base_url=""):
        """
        @api_key is required
        """
        if not api_key == "":
            self.API_KEY = api_key
        else:
            raise PGPException("API Key is required.")

        if not base_url == "":
            self.base_url = base_url

    def get(self, method, params={}):
        """
        Generic method to call the API and return response
        """
        if method == "":
            raise PGPException("No Method is provided.")

        try:
            params['key'] = self.API_KEY
            url = "%s/%s/json" % (self.base_url, method)
            parameters = urllib.urlencode(params)
            response_json = urllib.urlopen(url + "?" + parameters)
            response = json.load(response_json)
            return response
        except Exception as e:
            print str(e)
            return False

    def search(self, location="", radius=100, sensor="true", keyword="", language="en", name="", types=""):
        """
        Searches for places.

        @location is latitude and longitude seperated by comma, e.g. "12.123,56.234"
        @sensor is true or false.
        @radius is specified in meters.
        @language list of available languages - http://goo.gl/kVquC
        @types list of available types - http://goo.gl/IUJZr
        """
        response = self.get(
            "search", {
                'location': location, 
                'radius': radius, 
                'sensor': sensor,
                'keyword': keyword,
                'language': language,
                'name': name,
                'types': types,
            }
        )
        return response

    def getPlaceDetails(self, reference, sensor="true", language="en"):
        """
        Gets place details by Reference

        @reference is required.
        @sensor is true or false.
        @language list of available languages - http://goo.gl/kVquC
        """
        if reference == "":
            raise PGPException("No Reference is provided.")

        response = self.get(
            "details", {
                'reference': reference,
                'sensor': sensor,
                'language': language,
            }
        )
        return response
        

    def checkin(self, reference, sensor="true"):
        """
        Checks the user in to the given place

        @reference is required.
        """
        if reference == "":
            raise PGPException("No Reference is provided.")

        response = self.get(
            "check-in", {
                'reference': reference,
                'sensor': sensor,
            }
        )
        return response