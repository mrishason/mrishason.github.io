# Ibrahim Mrisha Portfolio — Django

A database-powered personal portfolio with:

- A public portfolio website
- A generated CV with print/PDF support
- A secure Django admin dashboard
- Editable profile, work experience, education, skills, projects, conferences, topics, and publications
- SQLite for local development

## 1. Set up the project

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
```

## 2. Create an admin account

```bash
python manage.py createsuperuser
```

Enter your preferred username, email, and password when prompted.

## 3. Run the website

```bash
python manage.py runserver
```

Open:

- Public website: <http://127.0.0.1:8000/>
- Generated CV: <http://127.0.0.1:8000/cv/>
- Admin dashboard: <http://127.0.0.1:8000/admin/>

## Managing content

Sign in to the admin dashboard and update:

1. **Profile & CV contact details** — name, photo, biography, contact links, and CV summary
2. **Work experience** — jobs and achievements
3. **Education** — qualifications and institutions
4. **Skills** — technical, tools, language, and professional skills
5. **Projects** — portfolio projects, technologies, links, and images
6. **Conferences** — events and talks
7. **Topics** — interest tags displayed on the homepage
8. **Publications** — articles, papers, and research

The public pages update automatically whenever visible content is saved.

## Generate a PDF CV

Open `/cv/`, click **Print / Save PDF**, then select **Save as PDF** in the browser print dialog.

## Tests

```bash
python manage.py check
python manage.py test
```

## Production environment variables

Set these before deployment:

```bash
export DJANGO_DEBUG=False
export DJANGO_SECRET_KEY="a-long-random-secret-key"
export DJANGO_ALLOWED_HOSTS="your-domain.com,www.your-domain.com"
```
