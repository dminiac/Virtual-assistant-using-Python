from twilio.rest import Client 
import smtplib, ssl
from .login_credentials import USERNAME,PASSWORD
import requests


ip_request=requests.get('https://get.geojs.io/v1/ip.json')
ipAdd = ip_request.json()['ip']
url='https://get.geojs.io/v1/ip/geo/'+ipAdd+'.json'
geo_request=requests.get(url).json()
latitude=geo_request['latitude']
longitude=geo_request['longitude']
city=geo_request['city']
state=geo_request['region']
country=geo_request['country']
timezone=geo_request['timezone']
location_info=latitude+' , '+longitude+'\n'+city+' , '+state+' , '+country+"\n"+timezone
def send_whatsapp(msg):
    account_sid = 'ACe663722c4f2fbfeac4a2240e4a2c7fdd' 
    auth_token = 'ccecadf6b8ca957763c42830717f4c05' 
    client = Client(account_sid, auth_token) 
    message = client.messages.create(from_='whatsapp:+14155238886',body="\n"+msg+"\n"+location_info,    to='whatsapp:+919455266878' ) 
    print(message.sid)
def send_sms(msg):
    account_sid = 'ACe663722c4f2fbfeac4a2240e4a2c7fdd' 
    auth_token = 'ccecadf6b8ca957763c42830717f4c05' 
    client = Client(account_sid, auth_token) 
    message = client.messages.create( from_='+14842558182',   to='+919455266878' ,body="\n"+msg+"\n"+location_info) 
    print(message.sid)
def send_mail(msg):
    port = 465  # For SSL
    smtp_server = "smtp.gmail.com"
    sender_email = USERNAME # Enter your address
    receiver_email = "sanskar0703@gmail.com"  # Enter receiver address
    password = PASSWORD
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email,"\n"+ msg+"\n"+location_info)
