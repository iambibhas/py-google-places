from PyGooglePlaces import PyGooglePlaces

p = PyGooglePlaces("AKI_KEY")

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