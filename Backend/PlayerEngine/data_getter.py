import requests
import json

# gets and returns a json object of stats of all NBA players
def get_API_data():
    url = "http://api.sportsdata.io/v3/nba/stats/json/PlayerSeasonStats/2021"

    headers = {
        'Ocp-Apim-Subscription-Key': "5375d931e0014ded93f15316afb50524"
        }

    response = requests.request("GET", url, headers=headers)

    return response.text

def jprint(obj):
    # create a formatted string of the Python JSON object
    text = json.dumps(obj, sort_keys=False, indent=4)
    print(text)