import requests
from columnar import columnar

# Helper that accepts JSON data as parameter and returns the top 5 goal scorers from the data. 
def get_top_scorers(json_data):
    
    scorers = json_data['scorers']
    
    scorer_list = []
    
    # Iterate through list of dictionaries to get player name, team and number of goals scored in a new dictionary object. 
    for ele in scorers:
        scorer_details = {}
        scorer_details['player_name'] = ele['player']['name']
        scorer_details['numberOfGoals'] = ele['numberOfGoals']
        scorer_details['team'] = ele['team']['name']
        scorer_list.append(scorer_details)
        
    # Get the top 5 goal scorers.

    # 1. Sort the list of dictionaries by the number of goals scored. 
    sorted_list = sorted(scorer_list, key = lambda i : i['numberOfGoals'], reverse = True)
    top_goalscorers = []
    num_goals = []

    # 2. Print the player names, number of goals scored and their respective clubs
    for ele in sorted_list[:5]:
        top_goalscorers.append(ele['player_name'])
        num_goals.append(ele['numberOfGoals'])
        
    # convert data into list of lists to fit into the columnar function. 
    data = [list(a) for a in zip(top_goalscorers, num_goals)]
    headers = ["Name", "Goals"]
    
    table = columnar(data, headers)
    
    return table

# URL for Premier League data. 
url = "https://api.football-data.org/v2/competitions/PL/scorers?limit=250"
headers = {"X-Auth-Token": "d3850215608a4bfcbcde80bd3a89dc25"}

# Make an API call to get goalscorers' data for the requested URL.
response = requests.get(url, headers=headers)
pl_data = response.json()

pl_top_scorers = get_top_scorers(pl_data)

print(pl_top_scorers)

# URL for Champions League data. 
url = "http://api.football-data.org/v2/competitions/CL/scorers?limit=350"
headers = {"X-Auth-Token": "d3850215608a4bfcbcde80bd3a89dc25"}

# Make an API call to get goalscorers' data for the requested URL.
response = requests.get(url, headers=headers)
cl_data = response.json()

cl_top_scorers = get_top_scorers(cl_data)

print(cl_top_scorers)

# URL for Spanish League data. 
url = "http://api.football-data.org/v2/competitions/PD/scorers?limit=250"
headers = {"X-Auth-Token": "d3850215608a4bfcbcde80bd3a89dc25"}

# Make an API call to get goalscorers' data for the requested URL.
response = requests.get(url, headers=headers)
la_liga_data = response.json()

la_liga_top_scorers = get_top_scorers(la_liga_data)

print(la_liga_top_scorers)
