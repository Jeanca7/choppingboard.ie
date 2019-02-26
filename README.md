![img_0050](https://user-images.githubusercontent.com/43143675/53450907-62556a80-3a15-11e9-8d53-0ad96dc523bd.jpg)
## ChoppingBoard
Social media for those who want to learn from others and want to show the world their own recipes.

## Motivation
Sharing ideas, knowledge and experiences through a social media dedicated to a diversed world. 
People can learn from others and introduce followers/viewers to their own recipes, and they can do this without being a profesional chef but being passionate about cooking.

## Build status
Travis has been used for building status of continus integration.

[![Build Status](https://travis-ci.org/Jeanca7/choppingboard.ie.svg?branch=master)](https://travis-ci.org/Jeanca7/choppingboard.ie)

## Code style
I have used standard code style.

## Screenshots


## Tech/framework used
<b>Built with</b>
* Django
* Bootstrap 4
* jQuery
* Ajax
* Python
* JavaScript
* CSS3
* HTML5
* PostgreSQL database
* Stripe
* Heroku

## Features
Everyone can view recipes including their videos and pictures. However, in order to interact with ChoppingBoard and its users, viewers must register.
The content on ChoppingBoard is created by its users only.

Specific features are as follows:
1. Authentication system (registration, login, logout, password change and password reset)
2. Social authentication (register and login using Facebook, Linkedin and Google+ (please notice that Google+ will come to an end in April 2019)) 
3. Custom user profiles (Users can change their profile information including names, email, avatar, background image, etc.)
4. Generated images tumbnails (using sorl-thumbnail)
5. Pagination (using ajax)
5. follower system (using ajax)
6. like system (using ajax)
7. Views 
8. Users can email cooks from their profile. 


## Installation

You might need to create an account on AWS (Amazon  and generate secret keys to access the static files. You can find information here: (https://docs.aws.amazon.com/general/latest/gr/aws-sec-cred-types.html#access-keys-and-secret-access-keys)   
Additionally, you need to install an SQL databse system to store information. ChoppingBoard uses PostgreSQL.  
ChoppingBoard utilises Stripe for payments, you can create an account here: (https://stripe.com/ie)

To run this project you will need to clone this repository and enter the following command in your console.
```
$ sudo pip3 -r install requirements.txt
```

## Deployment
ShoppingBoard is hosted on Heroku and static files are stored on AWS.  
(https://jeancasedo-choppingboard.herokuapp.com/)

## Tests
Testing was executed manually to ensure the website's responsiveness, funcionality and defensiveness work correnctly.   

* Responsiveness:
The site was tested on a 23.8" monitor and 13.3" MacBook Air, iphone X and ipad Pro. It was also tested on Firefox, Chrome and Safari.

* Functionality:
To ensure features of the site work effectively and on different operating systems.
    * registration
    * Login/logout
    * social authentication(on Facebook, Linkedin and Google+) Social Uthentication works on deployed website only.
    * Uploading files as images and videos.

* Deffensiveness:
    * Only users can login and post a recipe.
    * An unregistered person cannot follow a user.
    * An unregistered person cannot give a like to recipes.
    * Only users can delete and edit their own recipe and not someone else's.
    * Only users can edit their own profile and not someone else's.
    * Users' profiles can only be viewed by other users.

## How to use?
You can register with your email or login with a social media account(Facebook, Linkedin or Google+).  
Alternatively, you can use the username:guest and password:guest777  
ChoppingBoard: (https://jeancasedo-choppingboard.herokuapp.com/)

## Credits
 Django documentation (https://docs.djangoproject.com/en/2.1/)  
 Appreciation for Django authentication. Simple is better than complex (https://simpleisbetterthancomplex.com/)  
 Book Django 2 by Example By Antonio Mele (Publisher:Packt, 2018)

### Media
* Videos were obtained from Pexels.com
* Images obtained from Pexels.com and Google.
* Icons from Fontawesome.com
* Fonts from GoogleFonts.
    
