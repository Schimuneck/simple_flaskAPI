
import requests


if __name__ == '__main__':

    URL = "http://127.0.0.1:4996/sensorterra/"

    name = 'Matias ama Ana'
    author = 'Matias'
    genre = 'Romance'

    JSON = {'name': name,
              'author': author,
              'genre': genre
              }

    r = requests.post(URL, json=JSON)

    data = r.json()

    print('Response: %s' % data)
