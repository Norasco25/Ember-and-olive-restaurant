# Ember & Olive
A fictional Mediterranean restaurant website. HTML, CSS, vanilla JavaScript, Python/Django, and Node.js build tooling. Node.js builds the static preview; Django runs the server and saves reservations in SQLite. No npm dependencies required.

## Run the full website
Requires Python 3.10+ and Node.js 18+.

```sh
python -m venv .venv
# macOS/Linux:
source .venv/bin/activate
# Windows instead: .venv\Scripts\activate
python -m pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```
Open http://127.0.0.1:8000 and http://127.0.0.1:8000/admin/.

## Frontend preview
```sh
npm run build
npm run check
```
The dist directory is a static design preview. It does not submit or store reservations. The Django site accepts pending requests; it does not send emails or automatically confirm table availability. Staff manage requests through Django admin.

## Customize
Edit restaurant/templates/index.html for restaurant name, menu, sample hours and copy. Edit restaurant/static/style.css for styling. Replace illustrative Unsplash photos with your own licensed images. Google Fonts and images require internet access.

## Production
Use a Django-capable host and a production WSGI server. Set DJANGO_DEBUG=0, a strong DJANGO_SECRET_KEY, and DJANGO_ALLOWED_HOSTS. Configure HTTPS, static file serving, backups, logging, request rate limiting, and reservation capacity rules before accepting real customers. The supplied settings default to local development. No real restaurant address or contact details are claimed.
