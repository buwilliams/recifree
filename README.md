# Recifree

Recifree is a **fast**, **ad-free**, and **open-source** recipe website.

## Motivation

Cooking is a joy, especially during Covid. Finding and sharing recipes doesn't spark joy however. I 
created Recifree because I'm annoyed with *long* food blog stories and recipes sites with
so many annoying ads.

*Completely open-source. Created with love to increase the joy of cooking.*

## For Users of Recifree

How to use Recifree:
1. Start by creating your profile. This is where all your recipes will be saved.
1. Add your recipes.
1. Share your recipes with friends, ad-free.

Recifree is not live at this time since it's under construction. Thanks for your interest!

## For Developers

Recifree high-level goals are **simplicity** and **performance**. We are making saving
and sharing recipes an excellent experience. I don't expect users to spend a large amount 
of time on this site. Users should be able to get what they need quickly.

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
