import requests

app_id = 'e3f8cead'
app_key = '7ffa41a78b42ecd6f234495acfa4578e'

language = 'en-gb'
word_id = input("Enter a word: ")
fields = 'pronunciations'
strictMatch = 'false'

url = 'https://od-api.oxforddictionaries.com:443/api/v2/entries/' + language + '/' + \
      word_id.lower() + '?fields=' + fields + '&strictMatch=' + strictMatch

r = requests.get(url, headers={'app_id': app_id, 'app_key': app_key})

print("code {}\n".format(r.status_code))
print("text \n" + r.text)
