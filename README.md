# Django-react-app framework

This is an example django-react framework with hybrid-app configuration (one deploy process). It is intended to be used with Heroku and has prebuilt, separate config files for different environments. The apps have been placed into a single folder to allow for more readable project structure. This repo was originally forked from a react-django framework and then adapted significantly.

The procfile and runtime.txt are used by heroku. If you aren't gonna use heroku then get rid of them.

## Frontend

### Building
```
npm run build
```

### Running Frontend (in development)
```
npm start
```

## Backend

### Running Backend (in development)

```
pip install -r requirements.txt
```

Dev server
```
python manage.py runserver
```

Testing
```
python manage.py test
```