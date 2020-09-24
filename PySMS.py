from twilio.rest import Client

# Find these values at https://twilio.com/user/account
account_sid = ""
auth_token = ""

client = Client(account_sid, auth_token)

client.api.account.messages.create(
    to="enter number verified by twilio",
    from_="enter twilio number",
    body="Hello there!")
