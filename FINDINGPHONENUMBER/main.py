import phonenumbers 
from phonenumbers import geocoder, carrier, timezone
print("x"*50)
entered_num = input("Enter your phone numbers:")
phone_num = phonenumbers.parse(entered_num, "EG")
print(phone_num)
print(geocoder.description_for_number(phone_num, "en"))
print(carrier.name_for_number(phone_num, "en"))
print(timezone.time_zones_for_number(phone_num))
