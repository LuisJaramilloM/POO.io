import phonenumbers
from phonenumbers import geocoder

phone_number1 = phonenumbers.parse("+593996812371")

print("\nPhone Numbers = Location\n")
country = geocoder.description_for_number(phone_number1, "en")
print(country)


