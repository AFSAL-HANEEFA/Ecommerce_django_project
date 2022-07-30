from django.contrib import messages
from django.conf import settings
from twilio.rest import Client



# =============== Twilio API for sending SMS ==============


# Download the helper library from https://www.twilio.com/docs/python/install
# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure

account_sid = settings.TWILIO_ACCOUNT_SID
auth_token = settings.TWILIO_AUTH_TOKEN
verification_sid = settings.VERIFICATION_SID

client = Client(account_sid, auth_token)

def get_otp(request, mob_number):
    try:
        client.verify \
            .services(verification_sid) \
            .verifications \
            .create(to='+91'+mob_number, channel='whatsapp')
        messages.success(request, 'OTP successfuly sent! Please check your WhatsApp')
        return True
    except:
        messages.info(request, 'Something went wrong, free sms trial may be expired!')
        return False

def check_otp(request, otp, mob_number):

    try:
        verification_check = client.verify \
                            .services(verification_sid) \
                            .verification_checks \
                            .create(to='+91'+mob_number, code=otp)

        if(verification_check.status == 'approved'):
            return True
    except:
        return False