# Travel:list Web Application

## Summary

**Travel:list** allows a user to create trips to store activities and recommendations. The Google maps and Geocoding API 's work together to allow users to visually track upcoming trips.  A user can create/update/add and delete both activities and trips as needed.


## About the Developer

Travel:list was created by Benish Sarinelli, a software engineer in San Francisco, CA. This is her first project.
Visit her on [LinkedIn](https://www.linkedin.com/in/bsarinelli/).


## Technologies

**Tech Stack:**
- Backend: Python, Flask, PostgreSQL, SQLAlchemy, JSON
- Frontend: JavaScript, jQuery, AJAX, Jinja2, Bootstrap, HTML5, CSS3
- APIs: Google Maps and Google Geocode


Travel:list is an app built on a Flask server with a PostgreSQL database, with SQLAlchemy as the ORM. The front end templating uses Jinja2, the HTML was built using Bootstrap, and the Javascript uses JQuery and AJAX to interact with the backend. 


## Features

![alt text](https://github.com/bsarinelli/travellist/static/travellist.gif)



- **Interactive trip plotting functionality:** Once a user creates a trip entering the two required pieces of information: city and state, Google Maps API and Google Geocoding work together to dynamically update the users and maps view.


## For Version 2.0

- **More input control:** Implement the ability for multiple users to collaborate on a single trip.
- **Upload Image for a trip:** Allow user to upload an image of their desination once a trip has been added.
