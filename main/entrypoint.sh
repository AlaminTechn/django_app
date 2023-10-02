#!/bin/bash

# Apply migrations
python manage.py makemigrations
python manage.py migrate

