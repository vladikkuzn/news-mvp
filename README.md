# News-mvp - news blog

## The main page is hosted on https://news-mvp.herokuapp.com/

## To view api routs go to https://news-mvp.herokuapp.com/api

To start app as docker container: docker-compose up<br/>
To start app not as docker container: python manage.py runserver<br/>


### /api - directory that is responsible for API
  /migration - directory that is responsible for migrations<br/>
  /__init__.py - makes package from repository<br/>
  /admin.py - file that gives an opportunity to register model to admin\`s iterface<br/>
  /apps.py - file that is responsible for app settings<br/>
  /models.py - file that is responsible for models<br/>
  /serializers.py - file that is responsible for transforming models into JSON format(serializing)<br/>
  /tests.py - file that is responsible for tests<br/>
  /urls.py - file that is responsible for API routes<br/>
  /wiews.py - file that is responsible for API views<br/>
  

### /frontend - directory that is responsive for frontend
  /migration - directory that is responsible for migrations<br/>
  /__init__.py - makes package from repository<br/>
  /admin.py - file that gives an opportunity to register model to admin\`s iterface<br/>
  /apps.py - file that is responsible for app settings<br/>
  /models.py - file that is responsible for models<br/>
  /tests.py - file that is responsible for tests<br/>
  /urls.py - file that is responsible for frontend routes<br/>
  /wiews.py - file that is responsible for frontend views<br/>
  /static/frontend - directory that is reponsible for static files(.js, .css, images)<br/>
  /templates/frontend - directory that is reponsible for HTML files<br/>

manage.py - tool for executing many Django-specific tasks<br/>
.gitignore - file that is responsible for files that dont need to be uploaded to github<br/>
Dockerfile - file for Docker container<br/>
docker-compose - file for composing Docker container<br/>
Procfile - file for Heroku<br/>
runtime.txt - file for Heroku<br/>
requirements.txt - requirements for project<br/>
