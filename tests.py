from PyGooglePlaces import PyGooglePlaces

p = PyGooglePlaces("AIzaSyDiT51Mmo8IA-D37Pm7v4TyDjeUPH088tw")

response = p.search("22.88,88.22", radius=4000)
if response['status'] == 'OK':
	print "Passed: search() test"
else:
	print "Failed: search() test"
	print response

response = p.getPlaceDetails("CnRtAAAAmaM586RQB3jY5Plj2Yub94qgGomgDiYiNVR1i7vVSgydhMBu44ruo_ndzUiy9dWb3beCrghWo0fA0m-Mr4xhDg8Gwb9Vjemr2IjpvFTAYf8HrbpO1nAsSO_c6tra1UuXOrS6zsaYzQaPOzIWBuU9QRIQvKVmtxw0a-R76NifJnxuHxoUnr3sZ16jtGY87wqg__kUIc0MLiE")
if response['status'] == 'OK':
	print "Passed: getPlaceDetails() test"
else:
	print "Failed: getPlaceDetails() test"
	print response

response = p.checkin("CnRtAAAAmaM586RQB3jY5Plj2Yub94qgGomgDiYiNVR1i7vVSgydhMBu44ruo_ndzUiy9dWb3beCrghWo0fA0m-Mr4xhDg8Gwb9Vjemr2IjpvFTAYf8HrbpO1nAsSO_c6tra1UuXOrS6zsaYzQaPOzIWBuU9QRIQvKVmtxw0a-R76NifJnxuHxoUnr3sZ16jtGY87wqg__kUIc0MLiE")
if response['status'] == 'OK':
	print "Passed: checkin() test"
else:
	print "Failed: checkin() test"
	print response