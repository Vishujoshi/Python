import phonenumbers
from phonenumbers import geocoder           

x=phonenumbers.parse("+91-7696687959")
print(x)
print(geocoder.description_for_number(x,"en"))