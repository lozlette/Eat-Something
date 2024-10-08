# WDI - Project-04

# General Assembly Project 4: Eat Something - an app for parents of fussy eaters.

## Goal: To create a full-stack app with React.js and Python.

### Timeframe
7 days

## Technologies used

* Python
* Flask
* SQLAlchemy
* PostgreSQL
* React.js
* JavaScript (ES6) / HTML5 / SCSS
* JWT
* Git / GitHub
* Bulma CSS Framework

# Our App: Eat something
![homepage](https://user-images.githubusercontent.com/42389173/53878909-05554800-4005-11e9-9943-5c9d9d8f1ebd.png)

A hosted version of this app can be found on Heroku at [eat-something1.heroku.com] (https://eat-something1.herokuapp.com) - (build errors to be fixed).

### Application Overview

An app that suggests recipes to parents of fussy eaters, based on two choices; 1 ingredient that their child likes to eat, and 1 ingredient that the parents want them to eat. This was a group project with one other developer.

### Instructions

1. The Eat Something homepage displays an image and a navbar, and takes you through to choose your ingredients page via a button. There are also options to register and log in via the navbar links.

2. Once on the ingredients index page, a user can select two ingredients, and then submit their choices. This will redirect them to the recipe show page.

![ingredients index](https://user-images.githubusercontent.com/42389173/53879014-4d746a80-4005-11e9-85d5-69e5a0a90fc6.png)

3. Once on the recipe show page, the user can see information on the chosen recipe, which combines both chosen ingredients. There is an image, nutrition information on both ingredients, the other ingredients needed, and the method. There is also an option to comment on the recipe in a comments form, and these comments are displayed at the bottom of the page in the comments feed.

![recipes show page](https://user-images.githubusercontent.com/42389173/53879098-857bad80-4005-11e9-86f4-6be2761e4392.png)

4. Users can register from the Register page and login on the login page. Users must provide a unique email address and matching password/password confirmation.

![register](https://user-images.githubusercontent.com/42389173/53879180-bbb92d00-4005-11e9-9d5f-ef647f2a82df.png)

![login page](https://user-images.githubusercontent.com/42389173/53879238-dc818280-4005-11e9-9321-ef440045c4d3.png)

5. Once logged in, users are redirected back to the homepage. There will now be an option to visit their profile page in the navbar.

![profile page](https://user-images.githubusercontent.com/42389173/53879318-0fc41180-4006-11e9-82bf-8ca1ef5b0ab7.png)

6. Once on their profile page users can see their avatar, details, message form, and their inbox. Here the user has the option to send a message to another user, by selecting that user from the dropdown menu. These messages will show up in the inbox of that other users profile page.

![profile page 2 - inbox](https://user-images.githubusercontent.com/42389173/53879392-41d57380-4006-11e9-8117-ddbf198a8d28.png)

## Process

This was a project with one other developer, [Gessica Santoro](https://github.com/Gessy90). We used Trello to manage the project and performed daily standups. Features were created on separate git branches before being merged into the development branch.

![trello board](https://user-images.githubusercontent.com/42389173/53879448-6f222180-4006-11e9-8b6d-1b1abf8bc124.png)

We started the project by planning our models and database structure. I then set up the models and controllers. This proved to be a challenge due to the relationships needed between models. (Please see challenges below). Gessica worked on setting up the seeds file, so that we had some data to work with on the front end.

Once the server side code was working and had been tested by making API requests with Insomnia, then we moved onto creating the frontend using React. We divided up the components and Gessica worked on the Register and Log in forms while I worked on the Ingredients Index and Recipe Show pages. We later added the user profile page.

We pair coded to work on the logic to display a recipe based on the users two ingredient choices. This proved to be a challenge, and we had to install an extra JS array methods library called Lodash in order to help with the logic in getting two ingredients choices to display one recipe. See code screenshot here for the intersection method used.
![intersection method](https://user-images.githubusercontent.com/7090684/55801976-2a8b1980-5acf-11e9-859a-6e86c60b466e.png)

I then worked on the extra feature of commenting on recipes, when a user is logged in. First I set up the comment model and comments controller, and added the create route for comments to the recipes controller. I also set up the route.
![createroute](https://user-images.githubusercontent.com/7090684/55802261-c6b52080-5acf-11e9-9db5-680eafdb1734.png)
On the front end I then worked on building the comments form component and displayed this within the RecipesShow page.


Next I decided to add the extra feature of internal messaging from user to user. As with comments I set up the model and controller, and the route. I found that the challenge was working out what to set as the message receiver in the create route in the User controller.
![messagescreateroute](https://user-images.githubusercontent.com/7090684/55802602-7ab6ab80-5ad0-11e9-8e53-09563754d2b7.png)

Gessica then added error messages and worked on testing our app.

We later pair coded to add flash messages.

We used Bulma and SCSS for the styling of the site. We used our wireframes throughout the process, to which some changes were made as we worked.

### Challenges

Setting up the relationships between the models on the backend was a challenge. For example for the recipes model, there was a join table needed between ingredients and recipes, as well as nested comment and ingredient schemas.
![recipesmodel](https://user-images.githubusercontent.com/7090684/55801474-185cab80-5ace-11e9-82f4-63b0b46a047c.png)

The logic involved in getting the page to redirect to a specific recipe based on the two ingredients chosen was a challenge.

Setting up the database was also a challenge as were new to working with database relationships, as was working in Python, a language we had only just learned.

Internal messaging was also a challenge.

### Wins

We worked really well together as a team, especially pair coding, which was very productive. We organised our time well, with the use of Trello, daily stand-ups and prioritisation of features.

Internal messaging was a win, as this was quite a challenge to get working.

## Future features

We would like to make the site more mobile responsive.

We would like to add an external API for the nutrition information on eahc ingredient. We found one called Edamam which would be perfect for this, and would enable us to cut the size of our seeds file in half.

We would like to add a search bar as an alternate option, that would enable you to choose two ingredients.

We would also like to add a delete function on the messages and comments.
