ISS satelite detector
 
 #   #   #  This code is about API request to detect if international space statios is above my country  #   #   #
 
 # import modules
 import requests
 from datetime import datetime
 import smtplib
 import time
 
 MY_EMAIL = "lagutest133@gmail.com"
 MY_PASSWORD = "email.password"
 MY_LAT = 41.693630 # latitude
 MY_LONG = 44.801620 # longitude
 
 
 def is_iss_overhead():
     response = requests.get(url="http://api.open-notify.org/iss-now.json")
     response.raise_for_status()
     data = response.json()
 
     iss_latitude = float(data["iss_position"]["latitude"])
     iss_longitude = float(data["iss_position"]["longitude"])
 
     #Your position is within +5 or -5 degrees of the iss position.
     if MY_LAT-5 <= iss_latitude <= MY_LAT+5 and MY_LONG-5 <= iss_longitude <= MY_LONG+5:
         return True
 
 
 def is_night():
     parameters = {
         "lat": MY_LAT,
         "lng": MY_LONG,
         "formatted": 0,
     }
     response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
     response.raise_for_status()
     data = response.json()
     sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
     sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])
 
     time_now = datetime.now().hour
 
     if time_now >= sunset or time_now <= sunrise:
         return True
 
 
 while True:
     time.sleep(60)
     if is_iss_overhead() and is_night():
         connection = smtplib.SMTP("smtp.gmail.com", 587)
         connection.starttls()
         connection.login(MY_EMAIL, MY_PASSWORD)
         connection.sendmail(
             from_addr=MY_EMAIL,
             to_addrs="lagur7777@gmail.com",
             msg="Subject:Look Up Lagur👆\n\nThe ISS(International Space Station) is above you in the sky."
         )
