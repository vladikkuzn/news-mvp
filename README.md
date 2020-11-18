# News-mvp - news blog

## The main page is hosted on https://news-mvp.herokuapp.com/

## To view api routs go to https://news-mvp.herokuapp.com/api

## Requirements
The final project is your opportunity to design and implement a dynamic website of your own. So long as your final project draws upon this course’s lessons, the nature of your website will be entirely up to you, albeit subject to the staff’s approval.

In this project, you are asked to build a web application of your own. The nature of the application is up to you, subject to a few requirements:

Your web application must utilize at least two of Python, JavaScript, and SQL.
Your web application must be mobile-responsive.
In README.md, include a short writeup describing your project, what’s contained in each file you created or modified, and (optionally) any other additional information the staff should know about your project.
If you’ve added any Python packages that need to be installed in order to run your web application, be sure to add them to requirements.txt!
Beyond these requirements, the design, look, and feel of the website are up to you!

## Final project
My final project is something similar to news blog. Users are able to create, edit, delete they own news. All the actions performed through API.

The project was built using Django as a backend framework and JavaScript as a frontend programming language. All generated information are saved in database (PostgreSQL).

All webpages of the project are mobile-responsive.

### Installation
To start app as docker container: docker-compose up<br/>
To start app not as docker container: python manage.py runserver<br/>


### /api - directory that is responsible for API
 * /migration - directory that is responsible for migrations<br/>
 * /__init__.py - makes package from repository<br/>
 * /admin.py - file that gives an opportunity to register model to admin\`s iterface<br/>
 * /apps.py - file that is responsible for app settings<br/>
 * /models.py - file that is responsible for models<br/>
 * /serializers.py - file that is responsible for transforming models into JSON format(serializing)<br/>
 * /tests.py - file that is responsible for tests<br/>
 * /urls.py - file that is responsible for API routes<br/>
 * /wiews.py - file that is responsible for API views<br/>
  

### /frontend - directory that is responsive for frontend
 * /migration - directory that is responsible for migrations<br/>
 * /__init__.py - makes package from repository<br/>
 * /admin.py - file that gives an opportunity to register model to admin\`s iterface<br/>
 * /apps.py - file that is responsible for app settings<br/>
 * /models.py - file that is responsible for models<br/>
 * /tests.py - file that is responsible for tests<br/>
 * /urls.py - file that is responsible for frontend routes<br/>
 * /wiews.py - file that is responsible for frontend views<br/>
 * /static/frontend - directory that is reponsible for static files(.js, .css, images)<br/>
 * /templates/frontend - directory that is reponsible for HTML files<br/>

 manage.py - tool for executing many Django-specific tasks<br/>
 .gitignore - file that is responsible for files that dont need to be uploaded to github<br/>
 Dockerfile - file for Docker container<br/>
 docker-compose - file for composing Docker container<br/>
 Procfile - file for Heroku<br/>
 runtime.txt - file for Heroku<br/>
 requirements.txt - requirements for project<br/>
