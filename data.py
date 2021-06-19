import requests

API_TRIVIA = 'https://opentdb.com/api.php'

parameters = {'amount': 10,
              'type': 'boolean'
              }

response = requests.get(API_TRIVIA, params=parameters)
response.raise_for_status()

data =response.json()
question_data = data['results']










