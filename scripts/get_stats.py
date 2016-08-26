import requests

api_key = CONFIG.get('mailgun_api_key')

response = requests.get(
    "https://api.mailgun.net/v3/sandboxa8ccfb01296d4b19bace47fb8102d130.mailgun.org/stats/total",
    auth=("api", api_key),
    params={
        "event": ["accepted", "delivered", "failed"],
        "duration": "1m"}
)

if response.status_code == 200:
    set_response(HttpResponse(status_code=200, content=response.text, content_type='application/json'))
else:
    set_response(HttpResponse(status_code=400, content=response.text, content_type='application/json'))
