# News-mvp - news blog

## The main page is hosted on https://news-mvp.herokuapp.com/

## To view api routs go to https://news-mvp.herokuapp.com/api

To start app as docker container: docker-compose up<br/>
To start app not as docker container: python manage.py runserver<br/>


###/api - directory that is responsible for API
  /migration - directory that is responsible for migrations
  /__init__.py - makes package from repository
  /admin.py - file that gives an opportunity to register model to admin\`s iterface
  /apps.py - file that is responsible for app settings
  /models.py - file that is responsible for models
  /serializers.py - file that is responsible for transforming models into JSON format(serializing)
  /tests.py - file that is responsible for tests
  /urls.py - file that is responsible for API routes
  /wiews.py - file that is responsible for API views
  

###/frontend - directory that is responsive for frontend
  /migration - directory that is responsible for migrations
  /__init__.py - makes package from repository
  /admin.py - file that gives an opportunity to register model to admin\`s iterface
  /apps.py - file that is responsible for app settings
  /models.py - file that is responsible for models
  /tests.py - file that is responsible for tests
  /urls.py - file that is responsible for frontend routes
  /wiews.py - file that is responsible for frontend views
  /static/frontend - directory that is reponsible for static files(.js, .css, images)
  /templates/frontend - directory that is reponsible for HTML files

manage.py - tool for executing many Django-specific tasks
.gitignore - file that is responsible for files that dont need to be uploaded to github
Dockerfile - file for Docker container
docker-compose - file for composing Docker container
Procfile - file for Heroku
runtime.txt - file for Heroku
requirements.txt - requirements for project
