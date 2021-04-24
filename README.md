# Recifree

Recifree is an **open-source**, **fast**, and **ad-free** recipe website.

1. Start by creating your own profile. 
1. Add your favorite recipes. 
1. Share them with friends or keep them as your personal recipe database.

## Motivation

Cooking is a joy, especially during Covid. Finding and sharing recipes doesn't spark joy however. I 
created Recifree because I'm annoyed with *long* food blog stories and recipes sites with
so many annoying ads.

*Completely open-source. Created with love to increase the joy of cooking.*

## For Users of Recifree

Our public site is not ready yet since the basic project is under construction. Thanks 
for your interest!

## For Developers

Below you will find information on setting up your local environment and contributing to 
Recifree. The high-level goals are **simplicity** and **performance**.

### Getting started

```bash
mkdir -p data/db
docker compose up
docker ps # grab Container ID from recifree_web image
docker exec -it [Container ID] /bin/bash
python manage.py createsuperuser # create super user
```

### Contributing Guidelines

- Avoid frameworks. Use vanilla CSS, HTML, and JavaScript. This will ensure good performance.
- Always be mobile friendly.
- Usually you should prefer performance over user-experience.
- Keep pages and scenes lightweight with minimal functionality. This will aid in keeping the code maintainable.
- General performance should be gained through caching.

### Project Plans

Project plans are tracked as standard GitHub issues. You can all see the open [project plan issues here](https://github.com/buwilliams/recifree/issues?q=is%3Aissue+is%3Aopen+release+version).