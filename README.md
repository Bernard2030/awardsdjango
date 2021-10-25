## awardsdjango
Is an application that allows users to  view posted projects, post, rate or review users projects. The user can also search for projects, view projects overal score and also view a profile in the profile page.
## Author
Bernard Opiyo

## Setup Requirements
* Git
* Github
* Django 3.2.8
* PostgreSQL
* Web-browser of your choice
* pip
* Python 3.8.10
* Cloudinary (for image upload)

## Installation
Use the following command to install all the requirement applications. pip freeze -r requirements.txt

## setup
* Run git clone https://github.com/Bernard2030/awardsdjango or download the zip file from github.

After extracting the files,

* Navigate to the project folder cd into it.

* Creating a virtual environment virtualenv virtual.

* Activating the virtual environment source virtual/bin/activate.

* Running the application python3 manage.py runserver

* Running tests python3 manage.py test.

* create database
    You will need to create a database a new postgress database by typing the following command to access postgress
        $ psql
    Then run below query to create a new database named instagramphotos
        
* create Database migrations
    make migrations on postgres using django
        python3.8 manage.py makemigrations 
    then run the below command.
        python3.8 manage.py migrate

## Technologies used
* Python3.8
* Django 
* rest_framework 
* HTML5 
* CSS 
* Bootstrap5
* PostgreSQL

user story

* View posted projects and their details
* Post a project to be rated/reviewed
* Rate/ review other users' projects
* Search for projects 
* View projects overall score
* View my profile page

## pictorial Discription
<img src="images/landingpage.png" alt="landing"/>
<img src="images/singleimage.png" alt="singlepage"/>
<img src="images/profile.png" alt="profile"/>
<img src="images/restapi.png" alt="restapi"/>
<img src="images/comments.png" alt="comments"/>

	
	
	
	
	
## Known Bugs
There are no known bugs at the moment if you find any reach out through brobernard.254@gmail.com

## Collaboration
To contribute on the application you can do so by reaching me on brobernard.254@gmail.com

## LICENSE
This project is under [MIT](LICENSE).