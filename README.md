# Recifree

Recifree is an **open-source**, **fast**, and **ad-free** recipe website.

1. Start by creating your own profile. 
1. Add your favorite recipes. 
1. Share them with friends or keep them as your personal recipe database.

## Motivation

Cooking is a joy, especially during covid. Finding and sharing recipes doesn't spark joy however. I 
created Recifree because I'm annoyed with *long* food blog stories and recipes sites with
so many annoying ads.

*Completely open-source. Created with love to increase the joy of cooking.*

## Getting started

```bash
mkdir -p data/db
docker compose up
docker ps # grab Container ID from recifree_web image
docker exec -it [Container ID] /bin/bash
python manage.py createsuperuser # create super user
```