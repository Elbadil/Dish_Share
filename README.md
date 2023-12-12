# Dish Share
## Where Culinary Creativity Finds Its Community.
![Project Landing Page](https://github.com/Elbadil/Dish_Share/raw/master/app/static/images/landing-page.jpg)
## Introduction
Welcome to [Dish Share](https://www.elbadel.tech), a platform where you can discover a world of diverse recipe ideas and showcase your culinary masterpieces!
At Dish Share, you have the opportunity to create your own personal account. Sign in anytime to explore, share, and get inspired by different recipe ideas provided by the platform and your fellow food enthusiasts. However, it's important to note that you don't have to sign in to enjoy browsing and discovering the wonderful posts and recipes shared by the community.

The idea behind Dish Share is simple, I wanted to create something that not only showcases the skills and tools I've acquired at ALX but also aligns with my love for food. Being a food enthusiast myself, it became the perfect project for me to take on.

## Technology Stack
### Backend:
* Python (Framework: Flask)

### Frontend:
* HTML
* CSS
* Javascript

### Database:
* MySQL

### DevOps:
* **Web Server:** Nginx
* **Application Server:** Gunicorn to serve the Flask app
* **Security:** Utilized SSL for secure connections and UFW Firewall for added protection.

---

## Dish Share - BackEnd
### Technologies
The back-end server and RESTful API of Dish Share, built in **Python**, **Flask** Framework and **MySQL** database.

### API
For External API I've used the Spoonacular API to enhance user experience by providing a diverse range of recipe suggestions. Spoonacular is a comprehensive food API that offers access to a vast database of recipes, ingredients, and culinary information.
Visit to the [Spoonacular API documentation](https://spoonacular.com/food-api/docs) for detailed information on terms of use and guidelines, available endpoints, request formats, and response structures.

---

## Dish Share - FrontEnd
### Technologies Used:
The front-end of Dish Share, built using **HTML**, **CSS**, and **Javascript**.

### Routes:

- **`/` - Landing Page:**
  Introduction to Dish Share, featuring the web app's slogan, description, and key features.

- **`/home` - Home Page:**
  Displays various recipe ideas directly on the home page, showcasing a curated selection.

- **`/recipe-feed` - Recipe Feed Page:**
  Showcases user-generated recipe posts, each containing the user's name, date posted, recipe title, and an accompanying picture.

- **`/recipe/:id` - Recipe Page:**
  Displays detailed information about a specific recipe, including ingredients and instructions.

- **`/recipes/:username` - User's Recipes Page:**
  Displays all recipe posts submitted by a specific user.

- **`/recipes/new` - Add New Recipe Page:**
  Allows users to fill out a form with all the necessary information for posting a new recipe (title, description, ingredients, etc.).

- **`/login` - Login Page:**
  Provides a login form for user authentication.

- **`/register` - Sign Up Page:**
  Features a registration form for new user sign-ups.

---

## Installation
To set up and run the Dish Share App locally, follow these steps:
   1. Clone the repository: *https://github.com/Elbadil/Dish_Share.git*  
   2. Navigate to the project directory: *cd Dish_Share*
   3. Create a virtual environment: *python -m venv env*
   4. Navigate to the virtual environment: *source env/bin/activate*
   5. Install the required dependancies: *pip install -r requirements.txt*
   6. Run the app: *python3 -m app.routes*
   7. Open the app on your browser: *http://127.0.0.1:5000/*

<!-- 1. **Database Setup:**
   - Created a MySQL database and user to store web app data.

2. **Authentication System:**
   - Implemented user login and registration forms for secure authentication.

3. **User's Account:**
   - Created an account form where users can update their information(Profile Picture, Username, Email)

4. **Recipe Posting Functionality:**
   - Added a post recipe form to allow users to share their favorite recipes with the community.

5. **External API Integration:**
   - Integrated the Spoonacular API to enhance user experience:
      - Implemented a search bar for users to discover recipes easily.
      - Showcased trending recipes on the home page for current popular choices.
      - Created an "Explore Recipes" section, utilizing the Spoonacular API to provide users with a diverse range of recipe suggestions.

### Frontend:
1. **Navigation Bar:**
   - Created a navigation bar where the Dish Share logo is aligned on the left, and on the right, defined different sections provided by the web app.

2. **Form Pages:**
   - Implemented a consistent style and design for the web app forms.

3. **Main Pages:**
   * **Landing Page:**
      - Divided the landing page into two main sections:
         + **First Section:**
            - Introduction to the web app with its slogan, description, a picture of several dishes, and two buttons: One to navigate to the home, and the other to navigate to the add recipe page where the user can describe and post his recipes.
         + **Second Section:**
            - Description of the different features that the web app provides to its users.
   * **Home Page:**
      - The home page is also divided into two main sections:
         + **First Section:**
            - **Featured Dish:** Showcased an easy-to-make and delicious main dish to attract users.
            - **Trending Recipes:** Highlighted trending recipes provided by the Spoonacular API.
         + **Second Section:**
            - Added an "Explore Recipes" section, utilizing the Spoonacular API to allow users to discover various recipes directly from the home page.
   * **Recipe Feed:**
      - The Recipe Feed page is designed as articles where every article is a recipe post by the user that contains the name of the user, date posted, recipe's title, and recipe's picture. It is ordered from the latest to the oldest. I defined 5 posts for a maximum number of posts per page. Users can navigate from page to page using number buttons at the bottom of the page. -->
<!-- 
      - To get the full recipe with its ingredients and intructions, you can just click the title or the image or a link that says full recipe to navigate to the page of the full recipe. -->

