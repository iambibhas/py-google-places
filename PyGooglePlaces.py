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
			self.API_KEY = "AIzaSyCtHGAefB9YS7oLCQDzz6mQs_RbUIu0Q7o"
			self.BASE_URL = "https://maps.googleapis.com/maps/api/place/search/json"
		else:
			raise PGPException("API Key is required.")

	def search(self, location="", radius=100, sensor="true", keyword="", language="en", name="", types=""):
		"""
		Searches for places.

		@location is latitude and longitude seperated by comma, e.g. "12.123,56.234"
		@radius is specified in meters.
		@language list of available languages - http://goo.gl/kVquC
		@types list of available types - http://goo.gl/IUJZr
		"""
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
		response_json = urllib.urlopen(self.BASE_URL + "?" + params)
		response = json.load(response_json)

		return response
