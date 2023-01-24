from pyexpat.errors import messages
from twilio.rest import Client


account_sid = ""
auth_token = ""
client = Client(account_sid, auth_token)
message = messages.create(
    body="kindly join my 7 aside football team on saturday for  dribbling and shooting skills",
    from_="+18636941209",
    to="+254791025786",
)
#+18636941209
