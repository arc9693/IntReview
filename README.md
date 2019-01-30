# IntReview
[![Build Status](https://travis-ci.org/arc9693/IntReview.svg?branch=master)](https://travis-ci.org/arc9693/IntReview)
![Python Versions](https://img.shields.io/pypi/pyversions/django.svg?style=flat)<br>
![forthebadge](https://forthebadge.com/images/badges/made-with-python.svg)<br>
![forthebadge](https://forthebadge.com/images/badges/built-with-love.svg)<br>
An app that records various interview responses and publicise them.

## Build Setup
#### Requirements
Python 3.6.3

```bash
#creating virtual env
mkdir project
cd project
virtualenv .
source bin/activate

#clone the directory
git clone https://github.com/arc9693/IntReview.git

#change directory
cd IntReview

#Install dependencies
pip install -r requirements.txt

#Do migrations
python manage.py makemigrations
python manage.py migrate

#Run server
python manage.py runserver
```
