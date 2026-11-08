import pywhatkit
from dotenv import load_dotenv, find_dotenv
import os

load_dotenv(find_dotenv(), override=True)

MobileNo = str(os.getenv("MOBILE_NUMBER"))

Msg = "Good Afternoon Everyone!"

# pywhatkit.sendwhatmsg(MobileNo, Msg, 15,56, 10)

image_path = "C:/AI Images/Happy_Diwali_2026.jpg"
caption = "HAPPY DIWALI 2026"

pywhatkit.sendwhats_image(MobileNo, image_path, caption, 10)
