#!/usr/bin/python3
"""Create and save new objects"""
import models
from models.user import User
from models.recipe import Recipe

dictionary = {'username': 'me', 'email':'chicken', 'password': 'Nice'}

haytam = User(**dictionary)
models.storage.new(haytam)
models.storage.save()

print(haytam)

# recipe = Recipe(**dictionary)
# models.storage.new(recipe)
# models.storage.save()

# ouiam = models.storage.get(User, 'da1ea8b2-4c48-4241-a81a-5b57b9fa2b2a')
# models.storage.delete(ouiam)
# models.storage.save()