import phonenumbers
from phonenumbers import geocoder

phoneno1=phonenumbers.parse("<insert phone number. example:+911234567890>")
phoneno2=phonenumbers.parse("<>")

print(geocoder.description_for_number(phoneno1,'en'))
print(geocoder.description_for_number(phoneno2,'en'))
