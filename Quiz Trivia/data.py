import requests

parameters = {                                                                                                          # Declaring the amount of questions and the answer type like true or false
    "amount": 50,
    "type": "boolean"
}
response = requests.get(url="https://opentdb.com/api.php", params=parameters)                                           # Using the Trivia API accessing the questions and answers
response.raise_for_status()

data = response.json()
question_data = data["results"]                                                                                         # Saving the question details in question_data

