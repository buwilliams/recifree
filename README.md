# Recifree

Cooking is a joy, especially during covid. Finding recipes doesn't spark joy however. I created recifree because I'm annoyed with *long* food blog stories and recipes sites filled to the brim with ads.

Recifree, is a **simple**, **fast**, and **ad-free**. Start by creating your own profile. Add your favorite recipes. Share them with friends or keep them as your personal recipe database.

*Completely open-source. Created with love to increase the joy of cooking.*

## Getting started

```bash
mkdir -p data/db
docker compose up
docker ps # grab container id from recifree_web image
docker exec -it `container_id` /bin/bash
% python manage.py createsuperuser # create super user
```