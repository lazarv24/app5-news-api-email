import requests
from send_email import send_email

topic = 'tesla'

api_key = '91d56cbaa06d40ca99503561e241a29a'
url = 'https://newsapi.org/v2/everything?' \
      f'q={topic}&' \
      'from=2023-11-22&sortBy=publishedAt' \
      '&apiKey=91d56cbaa06d40ca99503561e241a29a&' \
      'language=en'

# Make request
request = requests.get(url)

# Get a dictionary with data
content = request.json()

# Access the article titles and description
body = "Subject: Today's news\n\n"
for article in content['articles'][:20]:
    if article['title'] is not None:
        body += article['title'] + '\n' \
               + str(article['description']) \
               + '\n' + article['url'] + 2*'\n'

body = body.encode('utf-8')
send_email(message=body)
