import requests
import json

api_key = CONFIG.get('mailgun_api_key')

to_email = ARGS.get('to_email')
subject = ARGS.get('subject')
email_body = ARGS.get('email_body')

response = requests.post(
    "https://api.mailgun.net/v3/sandboxa8ccfb01296d4b19bace47fb8102d130.mailgun.org/messages",
    auth=("api", api_key),
    data={
        "from": "Mailgun Sandbox <postmaster@sandboxa8ccfb01296d4b19bace47fb8102d130.mailgun.org>",
        "to": to_email,
        "subject": subject,
        "text": email_body
    }
)

if response.status_code == 200:
    success_content = json.dumps(
        {
            'status_code': 200,
            'info': u'Mail successfully send to {}'.format(to_email)
        }
    )
    set_response(HttpResponse(status_code=200, content=success_content, content_type='application/json'))
else:
    fail_content = json.dumps(
        {
            'status_code': response.status_code,
            'info': response.text
        }
    )
    set_response(HttpResponse(status_code=400, content=fail_content, content_type='application/json'))
