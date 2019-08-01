# Download the helper library from https://www.twilio.com/docs/python/install
from twilio.rest import Client
import twilio_creds # local file

account_sid = twilio_creds.account_sid
auth_token = twilio_creds.auth_token
client = Client(account_sid, auth_token)

def quick_text(message_contents):
	from_number = twilio_creds.twilio_number
	to_number = twilio_creds.russell_number
	message = client.messages \
	                .create(
	                     body=message_contents,
	                     from_= from_number,
	                     to= to_number
	                 )
	print("SMS message sent from {} to {} with message SID {} and message contents: {}"
		.format(from_number, to_number, message.sid, message_contents))

if __name__ == '__main__':
	quick_text("This is a quick practice text :)")
