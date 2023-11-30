#!/usr/bin/python3
"""Create and save new objects"""
import requests
import os


# dictionary = {'username': 'me', 'email':'chicken', 'password': 'Nice'}

# haytam = User(**dictionary)
# models.storage.new(haytam)
# models.storage.save()

# print(haytam)

# recipe = Recipe(**dictionary)
# models.storage.new(recipe)
# models.storage.save()

# ouiam = models.storage.get(User, 'da1ea8b2-4c48-4241-a81a-5b57b9fa2b2a')
# models.storage.delete(ouiam)
# models.storage.save()

SPN_API = "https://api.spoonacular.com/recipes/complexSearch"
API_KEY = "ae39ae6304cc477887db49aeafb39abd"


# Make the initial request to get the list of results
apiKey = {'apiKey': API_KEY}
req = requests.get(SPN_API, params=apiKey)
req_json = req.json()
for ingredient in req_json['results']:
        print(ingredient)
