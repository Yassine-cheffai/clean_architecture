import meilisearch
import json

# open pull request fixing the missing api_key in the docs and the print too
client = meilisearch.Client('http://localhost:7700', api_key='MASTER_KEY')

json_file = open('/home/yassine/learning/clean_architecture/meilisearch/movies.json')
movies = json.load(json_file)

# result = client.index('movies').add_documents(movies)
# print(result)

result = client.index('movies').search('botman')
print(result)

