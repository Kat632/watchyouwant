




# Watch You Want?

[![showpiece home page](README_docs/showpieces/01-home.PNG)](https://watchyouwant-pp5.herokuapp.com/)

Click [here](https://watchyouwant-pp5.herokuapp.com/) to visit the live site.
------

## Introduction

**Watch You Want?** is a full stack e-commerce website for the 5th and final project of the Code Institute diploma in Software Development (e-commerce applications).

The site is a full B2C e-commerce website for a fictional watch shop selling brand new and restored watches.

The site provides role based permissions for users to interact with a central dataset. It includes user authentication, email validation, full CRUD functionality for approved users for Products, Categories, Blog Posts and Reviews.

The payment system uses Stripe.  Please note that this website is for EDUCATIONAL PURPOSES only and the credit card payment functionality is not set up to accept real payments.  Please do not enter any personal credit/debit card details when using the site.

**Testing interactively**

When testing interactively, use a card number, such as 4242 4242 4242 4242. Enter the card number in the Dashboard or in any payment form.

    Use a valid future date, such as 12/34.
    Use any three-digit CVC (four digits for American Express cards).
    Use any value you like for other form fields. 

This information has been taken directly from the [Stripe testing documentation](https://stripe.com/docs/testing).

## UX

### Ideal User Demographic
#### The ideal users of this website are:
- Gift givers
- Trendy individuals
- Fashion-conscious individuals
- People looking for a treat for themselves
- People who are interested in restoring and reusing old technology

### Development Planes
The overall design of the **Watch You Want?** website takes inspiration from [United Colours of Benetton](https://gb.benetton.com/) and [Swatch](https://www.swatch.com/).  I wanted a simple, clean site with a 1980s vibe and neon colours.  I felt that this would help to differentiate the site from the ones mentioned below.

#### Inspirations
Having extensively researched e-commerce websites, and then latterly specific watch websites, I knew that I wanted the website to have a white background and to not be overly busy.  My research led me to [Watch Shop](https://www.watchshop.com/) and to [House of Watches](https://www.houseofwatches.co.uk/), both of which served as inspiration for **Watch You Want?**.

#### Strategy
Broken into three categories, the website will attempt to focus on the following target audiences:
- **Roles:**
     - Site User
     - Site Owner

- **Demographic:**
     - Young to mature adults
     - Gift givers

- **Psychographics:**
    - Personality & Attitudes:
        - Fun-loving
        - Creative
        - Outgoing
        - Playful

    - Values:
        - Fashion conscious
        - Trendsetter
        - Interested in reusing and restoring old technology

    - Lifestyles:
        - Keeps up with the latest trends
        - Likes to wear a quality wrist watch
        - May own more than one wrist watch

The website needs to enable the **Site User** to:
- Find attractive products designed for themselves and their family and friends.
- Add their desired products to the shopping bag for purchasing.
- Filter products according to name, categories, rating and prices.
- Search products by name or description.
- Create a personalised profile to store their personal details and to be able to view past orders.
- Leave a review for a product (if logged in).
- Leave a comment on a blog post (if logged in).

The website needs to enable the **Site Owner** to:
- Add, edit and delete products on the site.
- View orders on the admin screen.
- Add, edit and delete blog posts.
- Approve or delete blog comments.
- Delete reviews.

The homepage gives the user plenty of choices to browse watches by specific category, or to view all products, either by way of the navbar dropdowns or by clicking on one of the choices in the coloured boxes.  If the user scrolls down further, they can immediately see anything in the "featured" category of products.

The checkout page features the ability to pay by Stripe in order for the user to make a purchase.

A logged in user can also leave reviews for products and leave a comment on blog posts.

A user can also sign up to the newsletter.


## Purpose

The app is designed as a e-commerce application that encourages the users to purchase one of the products on the website and the watch restoration blog gives users the opportunity to engage with the website.


## User Stories

#### EPICS
I began with some broad epics that allowed further refinement, resulting in the user stories outlined below:
- EPIC #1: Allow Site User to view what is on the site
- EPIC #2: Allow Site User to manage their own account
- EPIC #3: Allow a Shopper to refine what they are seeing on the screen
- EPIC #4: Allow a Shopper to make a purchase
- EPIC #5: Allow Site Admin to manage the site

#### Site User:
- As a Shopper, I want to be able to view a list of products so that I can select some to purchase.
- As a Shopper, I want to be able to view a specific category of products so that I can quickly find products I’m interested in without having to search through all the products.
- As a Shopper, I want to be able to view individual product details so that I can identify the price, description, product rating, product image and available colours.
- As a Shopper, I want to be able to view reviews of individual products by other shoppers so that I can see what other people have said about the items I am thinking of purchasing.
- As a Shopper, I want to be able to view the site blog and read about real-life watch restoration projects so that I can engage with the site’s content without necessarily having to make a purchase.
- As a Shopper, I want to be able to quickly identify deals, clearance items and special offers so that I can take advantage of special savings on products I’d like to purchase.
- As a Shopper, I want to be able to easily view the total of my purchases at any one time so that I can avoid spending too much!
- As a User, I want to be able to easily register for an account so that I can have a personal account and be able to view my profile.
- As a User, I want to be able to easily log in or out so that I can access my personal account information.
- As a User, I want to be able to easily recover my password in case I forget it so that I can recover access to my account.
- As a User, I want to be able to receive an email confirmation after registering so that I can verify my account registration was successful.
- As a User, I want to be able to leave a comment on a blog post so that I can engage with the site’s content without necessarily having to make a purchase.
- As a User, I want to be able to leave a review for an individual product I have purchased so that I can let other site user’s know what I think of something I have previously purchased.
- As a User, I want to be able to have a personalised user profile so that I can view my personal order history and order confirmations and save my payment information.
- As a Shopper, I want to be able to sort the list of available products so that I can easily identify the best rated, best priced and categorically sorted products.
- As a Shopper, I want to be able to sort a specific category of products so that I can find the best priced or best rated product in a particular category, or sort the products in that category by name.
- As a Shopper, I want to be able to sort multiple categories of products simultaneously so that I can find the best priced or best rated products across multiple categories, such as “Men’s Watches” and “Unisex Watches”.
- As a Shopper, I want to be able to search for a product by name or description so that I can find a specific product I’d like to purchase.
- As a Shopper, I want to be able to easily see what I’ve searched for and the number of results so that I can quickly decide if the product I want is available.
- As a Shopper, I want to be able to view items in my bag to be purchased so that I can identify the total cost of my purchase and all the items I will receive.
- As a Shopper, I want to be able to easily select the quantity of a product when purchasing it so that I can ensure I don’t accidentally select the wrong product or quantity.
- As a Shopper, I want to be able to adjust the quantity of individual items in my bag so that I can easily make changes to my purchase before checkout.
- As a Shopper, I want to be able to easily enter my payment information so that I can checkout quickly and with no hassles.
- As a Shopper, I want to be able to feel my personal and payment information is safe and secure so that I can confidently provide the required information to make a purchase.
- As a Shopper, I want to be able to view an order confirmation after checkout so that I can verify that I haven't made any mistakes.
- As a Shopper, I want to be able to receive an email confirmation after checkout so that I can keep the confirmation of what I’ve purchased for my records.

#### Site Admin:
- As a Site Admin, I want to be able to add a product so that I can add new items to my store.
- As a Site Admin, I want to be able to edit and update products so that I can change product prices, descriptions, images and other product criteria.
- As a Site Admin, I want to be able to delete a product so that I can remove items that are no longer for sale.
- As a Site Admin, I want to be able to write a blog post so that I can add new posts to my blog.
- As a Site Admin, I want to be able to edit/update a blog post so that I can change aspects of my blog, correct spelling mistakes, update images and other.
- As a Site Admin, I want to be able to delete a blog post so that I can remove blog posts that are no longer relevant.
- As a Site Admin, I want to be able to approve comments on my blog so that I can filter out any spam or irrelevant comments.
- As a Site Admin, I want to be able to delete comments on my blog so that I can filter out any spam or irrelevant comments.
- As a Site Admin, I want to be able to approve product reviews so that I can remove comments that are spam or offensive.
- As a Site Admin, I want to be able to delete product reviews so that I can remove product reviews that are irrelevant or unhelpful.


With the user stories in mind, I created the below strategy table to determine the trade-off of importance and viability with the following results: INSERT STRATEGY TABLE

### User Stories that have been satisfied by creation of particular apps in ths project:


**EPIC #1: Allow Site User to view what is on the site**
| id  |  content | how was it satisfied
| ------ | ------ | ------ |
|  [#1](https://github.com/Kat632/watchyouwant/issues/7) | As a Shopper, I want to be able to view a list of products so that I can select some to purchase | navigation, home page, products page |
|  [#2](https://github.com/Kat632/watchyouwant/issues/8) | As a Shopper, I want to be able to view a specific category of products so that I can quickly find products I’m interested in without having to search through all the products. | navigation, home page, products page |
|  [#3](https://github.com/Kat632/watchyouwant/issues/9) | As a Shopper, I want to be able to view individual product details so that I can identify the price, description, product rating, product image and available colours. | product details page |
|  [#4](https://github.com/Kat632/watchyouwant/issues/10) | As a Shopper, I want to be able to view reviews of individual products by other shoppers so that I can see what other people have said about the items I am thinking of purchasing. | review app on product details page |
|  [#6](https://github.com/JKat632/watchyouwant/issues/11) | As a Shopper, I want to be able to view the site blog and read about real-life watch restoration projects so that I can engage with the site’s content without necessarily having to make a purchase. | blog app |
|  [#7](https://github.com/Kat632/watchyouwant/issues/12) | As a Shopper, I want to be able to quickly identify deals, clearance items and special offers so that I can take advantage of special savings on products I’d like to purchase. | navigation, home page, products page |
|  [#8](https://github.com/Kat632/watchyouwant/issues/13) | As a Shopper, I want to be able to easily view the total of my purchases at any one time so that I can avoid spending too much! | cart app |

**EPIC #2: Allow Site User to manage their own account**
| id  |  content | how was it satisfied
| ------ | ------ | ------ |
|  [#9](https://github.com/Kat632/watchyouwant/issues/14) | As a User, I want to be able to easily register for an account so that I can have a personal account and be able to view my profile. | profile app |
|  [#10](https://github.com/Kat632/watchyouwant/issues/15) | As a User, I want to be able to easily log in or out so that I can access my personal account information. |  profile app |
|  [#11](https://github.com/Kat632/watchyouwant/issues/16) | As a User, I want to be able to easily recover my password in case I forget it so that I can recover access to my account. |  profile app |
|  [#12](https://github.com/Kat632/watchyouwant/issues/17) | As a User, I want to be able to receive an email confirmation after registering so that I can verify my account registration was successful. |  profile app |
|  [#13](https://github.com/Kat632/watchyouwant/issues/18) | As a User, I want to be able to leave a comment on a blog post so that I can engage with the site’s content without necessarily having to make a purchase. |  blog app |
|  [#14](https://github.com/Kat632/watchyouwant/issues/19) | As a User, I want to be able to leave a review for an individual product I have purchased so that I can let other site user’s know what I think of something I have previously purchased. | review app |
|  [#15](https://github.com/Kat632/watchyouwant/issues/20) | As a User, I want to be able to have a personalised user profile so that I can view my personal order history and order confirmations and save my payment information. | profile app |
| EPIC #3 | Allow a Shopper to refine what they are seeing on the screen |
| id  |  content | how was it satisfied
| ------ | ------ | ------ |
|  [#16](https://github.com/Kat632/watchyouwant/issues/21) | As a Shopper, I want to be able to sort the list of available products so that I can easily identify the best rated, best priced and categorically sorted products. | products app |
|  [#17](https://github.com/Kat632/watchyouwant/issues/22) | As a Shopper, I want to be able to sort a specific category of products so that I can find the best priced or best rated product in a particular category, or sort the products in that category by name. | products app |
|  [#20](https://github.com/Kat632/watchyouwant/issues/23) | As a Shopper, I want to be able to sort multiple categories of products simultaneously so that I can find the best priced or best rated products across multiple categories, such as “Men’s Watches” and “Unisex Watches”. | products app |
|  [#21](https://github.com/Kat632/watchyouwant/issues/24) | As a Shopper, I want to be able to search for a product by name or description so that I can find a specific product I’d like to purchase. |  products app, site-wide search bar |
|  [#22](https://github.com/Kat632/watchyouwant/issues/25) | As a Shopper, I want to be able to easily see what I’ve searched for and the number of results so that I can quickly decide if the product I want is available. | products app |
| EPIC #4 | Allow a Shopper to make a purchase |
| id  |  content | how was it satisfied
| ------ | ------ | ------ |
|  [#23](https://github.com/github.com/Kat632/watchyouwant/issues/27) | As a Shopper, I want to be able to view items in my bag to be purchased so that I can identify the total cost of my purchase and all the items I will receive. | bag app |
|  [#24](https://github.com/Kat632/watchyouwant/issues/26) | As a Shopper, I want to be able to easily select the quantity of a product when purchasing it so that I can ensure I don’t accidentally select the wrong product or quantity. | bag app |
|  [#36](https://github.com/Kat632/watchyouwant/issues/28) | As a Shopper, I want to be able to adjust the quantity of individual items in my bag so that I can easily make changes to my purchase before checkout. | bag app |
|  [#42](https://github.com/Kat632/watchyouwant/issues/29) | As a Shopper, I want to be able to easily enter my payment information so that I can checkout quickly and with no hassles. | checkout app |
|  [#48](https://github.com/Kat632/watchyouwant/issues/30) | As a Shopper, I want to be able to feel my personal and payment information is safe and secure so that I can confidently provide the required information to make a purchase. | checkout app |
|  [#49](https://github.com/Kat632/watchyouwant/issues/31) | As a Shopper, I want to be able to view an order confirmation after checkout so that I can verify that I haven't made any mistakes. | checkout app |
|  [#52](https://github.com/Kat632/watchyouwant/issues/32) | As a Shopper, I want to be able to receive an email confirmation after checkout so that I can keep the confirmation of what I’ve purchased for my records. | checkout app |
| EPIC #5 | Allow Site Admin to manage the site |
| id  |  content | how was it satisfied
| ------ | ------ | ------ |
|  [#110](https://github.com/Kat632/watchyouwant/issues/33) | As a Site Admin, I want to be able to add a product so that I can add new items to my store. | admin panel, products app |
|  [#118](https://github.com/Kat632/watchyouwant/issues/34) | As a Site Admin, I want to be able to edit and update products so that I can change product prices, descriptions, images and other product criteria. | admin panel, products app
|  [#110](https://github.com/Kat632/watchyouwant/issues/35) | As a Site Admin, I want to be able to delete a product so that I can remove items that are no longer for sale. | admin panel, products app |
|  [#110](https://github.com/Kat632/watchyouwant/issues/36) | As a Site Admin, I want to be able to write a blog post so that I can add new posts to my blog. | admin panel, blog app |
|  [#110](https://github.com/Kat632/watchyouwant/issues/37) | As a Site Admin, I want to be able to edit/update a blog post so that I can change aspects of my blog, correct spelling mistakes, update images and other. | admin panel, blog app |
|  [#110](https://github.com/Kat632/watchyouwant/issues/38) | As a Site Admin, I want to be able to delete a blog post so that I can remove blog posts that are no longer relevant. | admin panel, blog app |
|  [#110](https://github.com/Kat632/watchyouwant/issues/39) | As a Site Admin, I want to be able to approve comments on my blog so that I can filter out any spam or irrelevant comments. | admin panel, blog app |
|  [#110](https://github.com/Kat632/watchyouwant/issues/40) | As a Site Admin, I want to be able to delete comments on my blog so that I can filter out any spam or irrelevant comments. | admin panel, blog app |
|  [#110](https://github.com/Kat632/watchyouwant/issues/41) | As a Site Admin, I want to be able to approve product reviews so that I can remove comments that are spam or offensive. | admin panel, reviews app |
|  [#110](https://github.com/Kat632/watchyouwant/issues/42) | As a Site Admin, I want to be able to delete product reviews so that I can remove product reviews that are irrelevant or unhelpful. | admin panel, reviews app |

### User stories that are planned for next sprint

| id  |  content | 
| ------ | ------ |























































































































































































## Existing Features

### Navbar and Footer

![home page](README_docs/readme_images/watchyouwant_home.png)

A wide, deep navbar, incoporating a large logo and large icons has been designed for desktop users and narrow, simple navbar for mobile phone users. Each navbar appears and disapears according to bootstrap classes. 

### Footer
The footer is also wide and deep and is divided into three sections.  The first section is a logo that if clicked will take the user back to the home page.  The second section is a list of links pertaining to the user's account, in addition to links to the Privacy Policy, the Terms & Conditions and a link to the Contact Us page.  The third section has a link to sign up for the newsletter and links to social media presences.

### Shop

![products page](README_docs/readme_images/watchyouwant_all_products.png)

Each individual watch is set on its own bootstrap card. Cards are organised in grid utilising bootstrap classes. The mobile phone user will see one card in a row, medium screens will show 2 cards in a row and large screens will have 4 cards in a row.

Each card has the name of the product, an image of the product, the price and the rating.  If the user is logged in as a superuser, they will also be able to edit and delete a product from here.

When a product image is clicked, it takes the user to a page with more details about the given product.

### Product Detail page

![product detail page](README_docs/readme_images/watchyouwant_product_detail_top.png)

The top of the product detail page is divided into two halves.  The left-hand half contains a large product image and the right-hand half contains all the other details about the product, such as a longer description and features of the product.  At the bottom of this section is where the user can to change the quantity of the item, if they wish to purchase more than one and then add the product to their bag.  It is also possible to see if an item is out of stock here.  If an item is out of stock, the increment quantity buttons will not work and a user won't be able to add an item to their bag.

On mobile devices, this entire section will be in one column.

![product detail page](README_docs/readme_images/watchyouwant_product_detail_reviews.png)

The bottom of the product detail page is the review section.  A user can see reviews for the product they are viewing and logged-in users are also able to leave a review for the product.

### Shopping bag
![shopping bag page](README_docs/readme_images/watchyouwant_shopping_bag.png)

On the shopping bag page the user is able to see everything in their bag, including a product image, the quantity of the item they are ordering and the sub total of that item.  The user is also able to add more of an item to their bag, reduce the quantity or completely remove an item from their bag.  The subtotal and the bag total will respond accordingly.

There are two buttons at the bottom.  If the user clicks on Keep Shopping it will take them back to the All Products page and if they click Secure Checkout, it will take them to the checkout page.

### Checkout page
![checkout page](README_docs/readme_images/watchyouwant_checkout_page.png)

The checkout page is divided into two halves.  One half has a form for the user to input their details, and the other one has a summary of the order about to be purchased.  If the user is logged in, this form will appear pre-filled with their details if they have saved them to their account previously.  A user will always have to fill in their credit card details because the website does not store these details.

There are two buttons at the bottom.  One will take the user back to their bag if they wish to adjust it and the second one confirms the payment.

### Order confirmation
![order confirmation page](README_docs/readme_images/watchyouwant_confirmation.png)

The order confirmation page allows the user to see a summary of what they have just paid for, the address it is being sent to and successful completion of an order sends an email to the user.

### Blog

![blog page](README_docs/readme_images/watchyouwant_blog.png)

Each individual blog post is set on its own bootstrap card. Cards are organised in grid utilising bootstrap classes. The mobile phone user will see one card in a row, medium screens will show 2 cards in a row and large screens will have 3 cards in a row.

Each card has the title of the blog post, an image pertaining to the blog post, the author at the top and the number of post likes and comments at the bottom.

![blog detail page]()

