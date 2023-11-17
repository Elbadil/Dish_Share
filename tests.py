#!/usr/bin/python3
"""Create and save new objects"""
import models
from models.user import User
from models.recipe import Recipe

# dictionary = {'username': 'ouiam', 'email':'elb@aadail', 'password': 'elbadil'}

# haytam = User(**dictionary)
# models.storage.new(haytam)
# models.storage.save()

# print(haytam)

adel = models.storage.get(User, '03eef546-1a8a-4056-890b-97adb2799bab')
adels_recipes = adel.recipes
for recipe in adels_recipes:
    print(recipe)

ouiam = models.storage.get(User, 'da1ea8b2-4c48-4241-a81a-5b57b9fa2b2a')
models.storage.delete(ouiam)
models.storage.save()