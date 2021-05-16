![Recifree](recipes/static/images/logo-400.png)

Recifree is a recipe website that's **fast**, **ad-free**, and **open-source**.

## Motivation

Cooking is a joy. Finding and sharing recipes doesn't spark joy however. I 
created Recifree because I'm annoyed with *long* food blog stories and recipes sites with
so many annoying ads. It's open-source because like cooking recipes belong to the people.

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

## Tech Stack

- [Postgres](https://www.postgresql.org/) database
- [Django](https://www.djangoproject.com/) backend server
- [Django templates](https://docs.djangoproject.com/en/3.2/topics/templates/) for rendering server-side content
- [Vue.js](https://vuejs.org/) dynamic frontend
- [Bulma](https://bulma.io/) css framework
- [Font Awesome](https://fontawesome.com/) icon framework
- [Pexels](https://www.pexels.com/) stock photos

### Getting started

**Setup**
```bash
mkdir -p data/db # create db directory
docker compose up # sets up server and runs migrations
docker ps # grab Container ID from recifree_web image
docker exec -it [Container ID] /bin/bash
python manage.py createsuperuser # create super user for local dev
exit
```

**URLs**

- [/admin](http://localhost:8000/admin) - django admin UI
- [/api](htpp://localhost:8000/api) - rest API UI
- [/](http://localhost:8000/) - recifree app

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
- Use Django templates for initial page load so that it's search engine friendly. 
- Decorate templates with Vue for dynamic content and forms.
- Vue should use Django API endpoints.
- Do not use Django forms instead use Vue with JavaScript Fetch API.
