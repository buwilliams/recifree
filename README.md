# Recifree

Recifree is a **fast**, **ad-free**, and **open-source** recipe website.

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

**Setup**
```bash
mkdir -p data/db
docker compose up
docker ps # grab Container ID from recifree_web image
docker exec -it [Container ID] /bin/bash
python manage.py createsuperuser # create super user
```

**Start**
```bash
python manage.py makemigrations
python manage.py migrate
python manage.py runserver 0.0.0.0:8000
```

### Contributing Guidelines

- Features, tasks, and bugs are managed using standard GitHub issues. Active work is listed
  on the [Recifree project page](https://github.com/buwilliams/recifree/projects/1) using standard
  GitHub projects.
- [Open an issue](https://github.com/buwilliams/recifree/issues/new) with any
  suggestions or questions you have.
- Pull requests should be squashed during merge.

### Code Guidelines

- Keep the architecture simple.
- Be mobile friendly.
- Use Django templates for search engine friendly pages. 
- Decorate templates with Vue for dynamic content and forms.
- Vue should use Django API endpoints.
