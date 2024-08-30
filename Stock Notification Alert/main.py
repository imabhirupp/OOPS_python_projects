import requests
from twilio.rest import Client

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

## API endpoints and their keys

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
stock_api_key = "Your API Key"

NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
news_api_key = "Your API Key"

## API Parameters

stock_params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "outputsize": "compact",
    "apikey": stock_api_key,
}

news_params = {
    "q": COMPANY_NAME,
    "apikey": news_api_key,
}

## Twilio Account details

account_sid = "Your SID"
auth_token = "Your Auth Token"


## Using API to get the data

response = requests.get(STOCK_ENDPOINT, params=stock_params)
response.raise_for_status()
stock_data = response.json()["Time Series (Daily)"]

## Converting the data dict into a data list

data_list = [value for (key, value) in stock_data.items()]

## Fetching yesterday's data

yesterdays_data = data_list[0]
yesterdays_data_closing_price = yesterdays_data["4. close"]

## Fetching day before yesterday's data

day_before_yesterdays_data = data_list[1]
day_before_yesterdays_data_closing_price = day_before_yesterdays_data["4. close"]

## Calculating the difference of the closing price and it's percentage

difference = abs(float(yesterdays_data_closing_price) - float(day_before_yesterdays_data_closing_price))
diff_percentage = (difference / float(yesterdays_data_closing_price)) * 100

## If above 5% then send a message notification to the phone number

if diff_percentage > 5:
    news_response = requests.get(NEWS_ENDPOINT, params=news_params)
    news_response.raise_for_status()
    articles = news_response.json()["articles"]                                                                                     # Accessing only the articles
    three_articles = articles[:3]                                                                                                   # Slicing to three articles only

    message_content = [f"Headline: {article['title']}. \nBrief: {article['description']}" for article in three_articles]            # Formatting the articles from the three articles

    client = Client(account_sid, auth_token)                                                                                        # Intializing twilio client

    for article in message_content:
        message = client.messages.create(
                body=article,
                from_="Your temporary number",
                to="Your registered/verified number",
        )
        print(message.status)


