#Project Prerequisites: 
#You have to install the package called phone numbers for this project.
#To know more about the phonenumbers package can read this documentation – https://pypi.org/project/phonenumbers/
#Command for installing phonenumbers through cmd – pip install phonenumbers

# track location and time zone using the phone number
import phonenumbers
from phonenumbers import timezone
from phonenumbers import geocoder
from phonenumbers import carrier
 
number = input("Enter the phone number with country code : ")
 
# Parsing String to the Phone number
phoneNumber = phonenumbers.parse(number)
 
# printing the timezone using the timezone module
timeZone = timezone.time_zones_for_number(phoneNumber)
print("timezone : "+str(timeZone))
 
# printing the geolocation of the given number using the geocoder module
geolocation = geocoder.description_for_number(phoneNumber,"en")
print("location : "+geolocation)
 
# printing the service provider name using the carrier module
service = carrier.name_for_number(phoneNumber,"en")
print("service provider : "+service)
