# Dish Share
## Where Culinary Creativity Finds Its Community.
![Project Landing Page](https://github.com/Elbadil/Dish_Share/raw/master/app/static/images/landing-page.jpg)
### Introduction
Welcome to [Dish Share](https://www.elbadel.tech), a platform where you can discover a world of diverse recipe ideas and showcase your culinary masterpieces!
At Dish Share, you have the opportunity to create your own personal account. Sign in anytime to explore, share, and get inspired by different recipe ideas provided by the platform and your fellow food enthusiasts. However, it's important to note that you don't have to sign in to enjoy browsing and discovering the wonderful posts and recipes shared by the community.

The idea behind Dish Share is simple, I wanted to create something that not only showcases the skills and tools I've acquired at ALX but also aligns with my love for food. Being a food enthusiast myself, it became the perfect project for me to take on.

### Technology Stack
#### Backend:
* Python (Framework: Flask)

#### Frontend:
* HTML
* CSS
* Javascript

#### Database:
* MySQL

#### DevOps:
* **Web Server:** Nginx
* **Application Server:** Gunicorn to serve the Flask app
* **Security:** Utilized SSL for secure connections and UFW Firewall for added protection.

### Project Development Overview
#### Backend:
In this section, I'll provide a detailed overview of my work on Dish Share, covering aspects from the backend to the frontend.
1. **Database Setup:**
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

#### Frontend:
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
      - The Recipe Feed page is designed as articles where every article is a recipe post by the user that contains the name of the user, date posted, recipe's title, and recipe's picture. It is ordered from the latest to the oldest. I defined 5 posts for a maximum number of posts per page. Users can navigate from page to page using number buttons at the bottom of the page.

      <!-- - To get the full recipe with its ingredients and intructions, you can just click the title or the image or a link that says full recipe to navigate to the page of the full recipe. -->
      

   



For the frontend, I started with 