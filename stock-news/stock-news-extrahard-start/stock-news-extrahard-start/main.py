import requests

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
url = 'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=TSLA&interval=30min&apikey=I55TG7ET6WRI8H95'
r = requests.get(url)
data = r.json()
yesterday_close = float(data['Time Series (30min)']['2023-02-07 20:00:00']['4. close'])
day_before_close = float(data['Time Series (30min)']['2023-02-06 20:00:00']['4. close'])
diff = (yesterday_close-day_before_close)
if diff < 0:
    diff = -(diff)

if diff > (0.05*yesterday_close):
    print("Get News")


## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 
response = requests.get(url = 'https://newsapi.org/v2/everything?q=Tesla_Inc&from=2023-02-08&sortBy=popularity&apiKey=85927759dff94ae1b224da483f033c63')
data = response.json()
news = {}
for i in range(0,2):
    news[data['articles'][i]['title']] = data['articles'][i]['description'] 
print(news)

## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number. 


#Optional: Format the SMS message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

