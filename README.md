# Pics Backend Server API

---

#### Pics API: Python with Django Server


This PostgreSQL Database was developed to store and relay information related to users, picture cards, and likes to facilitate the operation a smooth Picture Sharing Client Application.

---

## Table of Contents

 - Important Links
 - Planning Story
 - User Stories
 - Technologies Used
 - Unsolved Problems
 - Entity Relationship Diagram

---

## Important Links

[Deployed Client](https://ttamsmas.github.io/pics_app/)

[Heroku git URL](https://git.heroku.com/pics-api2020.git)

[Client Repository](https://github.com/ttamsmas/pics_app)

[Server Repository](https://github.com/ttamsmas/pics_api)

---

#### Planning Story

I began this project with the stretch goal of mimicking Pinterest and at minimum a photo sharing application. I mapped out an ERD Diagram connecting Users, Likes, and Picture Resource Relationships, which was especially helpful because of the complex functionality of Like/Unlike Resources.

To achieve the MVP within the server, I slated to accomplish:

 - Create a Python based server using Django
 - Develop Routes to track Users & Pictures they upload
 - Setup functional CRUD Responses

Stretch Goals Included:

 - Add a Like/Unlike Resource linking Pictures and Users in a ManyToMany Relationship
      - One User should only make a single like
      - Besides Create/Delete like via toggle, we'll need to summarize likes by picture so will require Index, Create, and Delete CRUD Routes
 - Setup Follow/Unfollow OneToMany Relationship between Users and other Users
 - Connect to Amazon Web Service etc. to store uploaded images

---

## User Stories

 1. As a regular user, I would like to upload photos
 2. As a regular user, I would like to edit or delete photos I post
 3. As a regular user, I would like to follow other accounts
 4. As a mobile user, I would like the application scale relative to my screen size
 5. As a new user, I would like to be able to see all photos, not just those I follow

---

## Technologies Used

 - Django & Python
 - PostgreSQL

---

## Unsolved Problems

 - Users are unable to follow other Users
 - Heroku isn't designed to hold pictures so users are adding links to images rather than uploading them

---

## Entity Relationship Diagram

[ERD Point of Sale](https://i.imgur.com/uSDraTs.jpg)
