import requests

api_key = '91d56cbaa06d40ca99503561e241a29a'
url = 'https://newsapi.org/v2/everything?q=tesla&'\
       'from=2023-11-20&sortBy=publishedAt&apiKey='\
       '91d56cbaa06d40ca99503561e241a29a'

# Make request
request = requests.get(url)

# Get a dictionary with data
content = request.json()

# Access the article titles and description
for article in content['articles']:
       print(article['title'])
       print(article['description'])