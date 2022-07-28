# **Watch You Want - Testing** 

[Main README.md file](/README.md)

[View live project](https://watchyouwant-pp5.herokuapp.com/)

[View GitHub repository](https://github.com/Kat632/watchyouwant)

***
## **Table of contents**
1. [Manual Testing](#Manual-Testing)
2. [Automated Testing](#Automated-Testing) 
     - [Code Validation](#Code-Validation)
3. [Project Bugs and Solutions](#project-bugs-and-solutions)
3. [User Testing](#User-Testing)
***

## **Manual Testing**

| Manual Testing                        |                                                           |                                                                                                                                                                                           |      |   |
|---------------------------------------|-----------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------|---|
|                                       |                                                           |                                                                                                                                                                                           |      |   |
| **Navigation**                            |                                                           |                                                                                                                                                                                           |      |   |
| **Reference**                             | **Test object**                                               | **Expected Result**                                                                                                                                                                           | **Pass** |   |
| **Navbar**                                |                                                           |                                                                                                                                                                                           |      |   |
|                                     1 | Store Logo/Home link                                      | Directs the user to the home page                                                                                                                                                         | PASS |   |
|                                     2 | Categories link                                           | Opens the categories dropdown menu. All categories links work                                                                                                                             | PASS |   |
|                                     3 | All Products link                                         | Opens the all products dropdown menu.  All links work                                                                                                                                     | PASS |   |
|                                     4 | Special Offers link                                       | Opens the special offers dropdown menu.  All the links work.                                                                                                                              | PASS |   |
|                                     5 | Blog Link                                                 | Directs the user to the 'Blog' page                                                                                                                                                       | PASS |   |
|                                     6 | Search bar                                                | Directs the user to the 'Products' page showing products that match the query                                                                                                             | PASS |   |
|                                     7 | My Account Icon                                           | Opens the account links dropdown menu                                                                                                                                                     | PASS |   |
|                                     8 | Sign in link (unsigned users)                             | Directs the 'Sign in' page                                                                                                                                                                | PASS |   |
|                                     9 | Sign up link (unsigned users)                             | Directs the 'Sign up' page                                                                                                                                                                | PASS |   |
|                                    10 | Sign out link (signed in users)                           | Directs the 'Sign out' page                                                                                                                                                               | PASS |   |
|                                    11 | My Profile (signed in users)                              | Directs the user to the profile page                                                                                                                                                      | PASS |   |
|                                    12 | Product management (superuser)                            | Directs the user to the 'Product management' page                                                                                                                                         | PASS |   |
|                                    13 | Bag Icon                                                  | Directs the user to their shopping cart page                                                                                                                                              | PASS |   |
|                                    14 | Burger menu                                               | Burger menu opens the burger menu with the appropriate links work based on what type of user is signed in                                                                                 | PASS |   |
| **Footer**                                |                                                           |                                                                                                                                                                                           |      |   |
|                                     1 | Contact us link                                           | Directs the user to the 'Contact us' page                                                                                                                                                 | PASS |   |
|                                     2 | Terms & Conditions link                                   | Directs user to the Terms & Conditions page                                                                                                                                               | PASS |   |
|                                     3 | Privacy Policy link                                       | Directs user to the Privacy Policy page                                                                                                                                                   | PASS |   |
|                                     4 | Account Links (unsigned users)                            | Direct the users to the appropriate pages                                                                                                                                                 | PASS |   |
|                                     5 | Account Links (signed in users)                           | Direct the users to the appropriate pages                                                                                                                                                 | PASS |   |
|                                     6 | Newsletter subscribe button                               | Displays the appropriate message INVALID/VALID                                                                                                                                            | PASS |   |
|                                     7 | Social media links                                        | Open the respective social network page in a new tab                                                                                                                                      | PASS |   |
| **Home Page**                             |                                                           |                                                                                                                                                                                           |      |   |
| **Reference**                             | **Test object**                                               | **Expected Result**                                                                                                                                                                           | Pass |   |
| 1                                     | Products by category links                                | Direct the user to the 'Products' page with the correct category filters in place                                                                                                         | PASS |   |
| **Products Page**                         |                                                           |                                                                                                                                                                                           |      |   |
| **Reference**                             | **Test object**                                               | **Expected Result**                                                                                                                                                                           | Pass |   |
|                                     1 | Product Count                                             | Product Count updates in accordance with the number of products displayed and search term displays if a user has entered a search query                                                   | PASS |   |
|                                     2 | View all products link                                    | Redirects to the 'Products' page showing the entire catalogue of products                                                                                                                 | PASS |   |
|                                     3 | Breadcrumb Home link                                      | Clicking on Home in the breadcrumbs takes the user back to the home page                                                                                                                  | PASS |   |
|                                     4 | Sort By Dropdown                                          | Sort by dropdown displays all the options available and sorts the products in accordance with the selection                                                                               | PASS |   |
|                                     5 | Product Cards                                             | Clicking on a product card directs the user to the correct 'Product details' page                                                                                                         | PASS |   |
|                                     6 | Edit Product link (superuser)                             | Directs the superuser to the edit product form                                                                                                                                            | PASS |   |
|                                     7 | Delete Product link (superuser)                           | Triggers the delete confirmation modal                                                                                                                                                    | PASS |   |
|                                     8 | Delete Product Modal                                      | Clicking the 'Cancel' button closes the modal and clicking the 'Yes' button deletes the product successfully                                                                              | PASS |   |
| **Product Detail Page**                   |                                                           |                                                                                                                                                                                           |      |   |
| **Reference**                             | **Test object**                                               | **Expected Result**                                                                                                                                                                           | Pass |   |
| **Product Details**                       |                                                           |                                                                                                                                                                                           |      |   |
|                                     1 | Product Details                                           | Displays the detail of the appropriate product                                                                                                                                            | PASS |   |
|                                     2 | Technical Details                                         | Displays the appropriate technical details for the product                                                                                                                                | PASS |   |
|                                     3 | Quantity selectors                                        | Allows the user to adjust the quantity by clicking the plus and minus icons.                                                                                                              | PASS |   |
|                                     4 | Add to bag link                                           | When a product is added to the bag, a toast to confirm the action is displayed, and the amount below the cart icon in the navbar is updated to reflect the price of the items in the cart | PASS |   |
|                                     5 | Out of Stock items                                        | A user cannot add an item that is out of stock to their basket                                                                                                                            | PASS |   |
| **Reviews**                               |                                                           |                                                                                                                                                                                           |      |   |
|                                     1 | Product Reviews                                           | Displays the reviews for the product                                                                                                                                                      | PASS |   |
|                                     2 | No Reviews message                                        | Displays when no reviews are present                                                                                                                                                      | PASS |   |
|                                     3 | Add review button                                         | Open the page to add a product review                                                                                                                                                     | PASS |   |
|                                     4 | Delete Comment link (reviewer)                            | Deletes the review                                                                                                                                                                        | PASS |   |
|                                     5 | Edit Comment link (reviewer)                              | Takes the user to the edit comment page                                                                                                                                                   | PASS |   |
| **Add a Review Page**                     |                                                           |                                                                                                                                                                                           |      |   |
| **Reference**                             | **Test object**                                               | **Expected Result**                                                                                                                                                                           | Pass |   |
|                                     1 | Add a review                                              | Allows user to post a review if all fields are valid, by clicking on the 'Submit' button.                                                                                                 | PASS |   |
| **Edit a Review Page**                    |                                                           |                                                                                                                                                                                           |      |   |
| **Reference**                             | **Test object**                                               | **Expected Result**                                                                                                                                                                           | Pass |   |
|                                     1 | Edit a review                                             | Allows a user to edit a review if all the fields are valid, by clicking the submit button.                                                                                                | PASS |   |
| **Shopping Bag page**                     |                                                           |                                                                                                                                                                                           |      |   |
| **Reference**                             | **Test object**                                               | **Expected Result**                                                                                                                                                                           | Pass |   |
|                                     1 | Quantity Selectors                                        | Allows the user to adjust the quantity by clicking the plus and minus icons. Limits the quantity to what items are in stock. Disallows minus numbers                                      | PASS |   |
|                                     2 | Update Link                                               | Updates the quantity for the selected product                                                                                                                                             | PASS |   |
|                                     3 | Remove Link                                               | Removes the selected product from the cart                                                                                                                                                | PASS |   |
|                                     4 | Price totals                                              | The subtotal of each product, cart total and grand total are updated whenever the cart's content is changed                                                                               | PASS |   |
|                                     5 | Delivery Cost                                             | Delivery cost is added or removed when cart total is above or below £50                                                                                                                   | PASS |   |
|                                     6 | Keep Shopping Button                                      | Redirects the user to the Products page                                                                                                                                                   | PASS |   |
|                                     7 | Secure Checkout Button                                    | Directs the user to the checkout page                                                                                                                                                     | PASS |   |
|                                     8 | Cart is empty message                                     | Displays when there are no products in the cart. Below 'Keep shopping' button is displayed and redirects the user to the Products page                                                    | PASS |   |
| Checkout page                         |                                                           |                                                                                                                                                                                           |      |   |
| **Reference**                             | **Test object**                                               | **Expected Result**                                                                                                                                                                           | Pass |   |
|                                     1 | Order Summary                                             | Order summary information renders correctly. Price totals match the contents of the bag                                                                                                   | PASS |   |
|                                     2 | Checkout Form                                             | Form only submits when all the required fields are filled                                                                                                                                 | PASS |   |
|                                     3 | Pre-populated fields                                      | When a user is signed in and their shipping details have been saved on their profile, the corresponding fields are pre-populated                                                          | PASS |   |
|                                     4 | Save details checkbox                                     | When the delivery information checkbox is checked the user's profile is updated with the correct information after the form submission                                                    | PASS |   |
|                                     5 | Log In and Sign Up Links (unsigned users)                 | The sign in and sign up links are displayed and redirected the user to the relevant page                                                                                                  | PASS |   |
|                                     6 | Card errors                                               | Card errors message displays in case of: invalid card number, insufficient funds, etc.                                                                                                    | PASS |   |
|                                     7 | Card Charge notification                                  | Is displayed to let the user know how much their card will be charged to verify that the figure matches the total in the order summary section                                            | PASS |   |
|                                     8 | Adjust Cart button                                        | Redirects the user to the shopping cart                                                                                                                                                   | PASS |   |
|                                     9 | Complete Order button                                     | Triggers the loading overlay before redirecting the user to the Checkout Success page                                                                                                     | PASS |   |
| **Checkout success page and Stripe**      |                                                           |                                                                                                                                                                                           |      |   |
| **Reference**                             | **Test object**                                               | **Expected Result**                                                                                                                                                                           | Pass |   |
|                                     1 | Toast success message                                     | When the user is redirected to the Checkout Success page, a confirmation toast with the order number and a message to let the user know a confirmation email has been sent is displayed   | PASS |   |
|                                     2 | Confirmation Email                                        | The user receives a confirmation email to the address entered on the checkout page                                                                                                        | PASS |   |
|                                     3 | Order Summary                                             | Renders correctly with a list of the purchased products                                                                                                                                   | PASS |   |
|                                     4 | Order and Billing Info                                    | Matches the information entered on the checkout form and displays correct totals                                                                                                          | PASS |   |
|                                     5 | Continue Shopping link                                    | Redirects the user to the Products page                                                                                                                                                   | PASS |   |
|                                     6 | Back to profile link (if user accessed page from Profile) | Displays when users are looking at past orders from their profile, and when clicked it redirects the user back to the Profile page                                                        | PASS |   |
|                                     7 | Stripe payment succeed webhook                            | If payment succeeds, Stripe shows webhook: payment_intent.succeeded with status 200                                                                                                       | PASS |   |
|                                     8 | Order confirmation email                                  | If payment succeeds, the user receives a confirmation email with the order details                                                                                                        | PASS |   |
| **Contact Page**                          |                                                           |                                                                                                                                                                                           |      |   |
| **Reference**                             | **Test object**                                               | **Expected Result**                                                                                                                                                                           | Pass |   |
| 1                                     | Form Validation                                           | The form cannot be submitted without all the required fields being filled                                                                                                                 | PASS |   |
|                                     2 | Submit Button                                             | Once clicked the form is cleared and a success message displays to inform the user that their message has been sent                                                                       | PASS |   |
| **Blog Page**                             |                                                           |                                                                                                                                                                                           |      |   |
| **Reference**                             | **Test object**                                               | **Expected Result**                                                                                                                                                                           | Pass |   |
|                                     1 | Blog Post links                                           | Direct the user to the correct 'Blog Post' page                                                                                                                                           | PASS |   |
| **Blog Post Page**                        |                                                           |                                                                                                                                                                                           |      |   |
| **Reference**                             | **Test object**                                               | **Expected Result**                                                                                                                                                                           | Pass |   |
|                                     1 | Log In and Sign Up Links (unsigned users)                 | Log In and Sign Up Links (unsigned users)                                                                                                                                                 | PASS |   |
|                                     2 | Log In and Sign Up Links (unsigned users)                 | Displays when no comments are present                                                                                                                                                     | PASS |   |
|                                     3 | Add comment button                                        | Open the post comment modal                                                                                                                                                               | PASS |   |
|                                     4 | Post Comment form                                         | Allows user to post a comment, given that all the required field on the form are filed, by clicking on the 'Submit' button                                                                | PASS |   |
| **Profile Page**                          |                                                           |                                                                                                                                                                                           |      |   |
| **Reference**                             | **Test object**                                               | **Expected Result**                                                                                                                                                                           | Pass |   |
|                                     1 | Delivery Information Form                                 | User's shipping information is displaying in the relevant fields if they have previously made an order and clicked the save to profile checkbox                                           | PASS |   |
|                                     2 | Update Information button                                 | Saves changes to the user's profile if form is valid and a success message displays to confirm this to the user                                                                           | PASS |   |
|                                     3 | Previous orders                                           | Displays in the order history section with the latest order at the top                                                                                                                    | PASS |   |
|                                     4 | Previous order confirmation                               | Clicking the order number takes the user to the checkout success page for the selected order                                                                                              | PASS |   |
| **Add Product (Product Management) Page** |                                                           |                                                                                                                                                                                           |      |   |
| **Reference**                             | **Test object**                                               | **Expected Result**                                                                                                                                                                           | Pass |   |
|                                     1 | Required Fields                                           | Form does not submit unless required fields are correctly filled                                                                                                                          | PASS |   |
|                                     2 | Dropdown Fields                                           | All the categories options appear in the dropdown fields                                                                                                                                  | PASS |   |
|                                     3 | Select Image Link                                         | Allows the user to upload an image from their device, and a message displays to the user the images' name                                                                                 | PASS |   |
|                                     4 | Cancel Button                                             | Redirects the user back to the products page                                                                                                                                              | PASS |   |
|                                     5 | Add Product Button                                        | Redirects the user to the 'Product details' page for the new product with the correct information displayed                                                                               | PASS |   |
| **Edit Product Page**                     |                                                           |                                                                                                                                                                                           |      |   |
| **Reference**                             | **Test object**                                               | **Expected Result**                                                                                                                                                                           | Pass |   |
|                                     1 | Form Fields                                               | Form fields are pre-populated with the product information stored in the database                                                                                                         | PASS |   |
|                                     2 | Cancel Button                                             | Redirects the user back to the 'Products' page                                                                                                                                            | PASS |   |
|                                     3 | Update Product Button                                     | Updates any of the product information and redirects the user to the 'Product details' page for the edited product with the correct information displayed                                 | PASS |   |
| Backend Blog post pages               |                                                           |                                                                                                                                                                                           |      |   |
| **Reference**                             | **Test object**                                               | **Expected Result**                                                                                                                                                                           | Pass |   |
|                                     1 | Add blog post                                             | Superuser can add a blog post                                                                                                                                                             | PASS |   |
|                                     2 | Edit blog post                                            | Superuser can edit a blog post                                                                                                                                                            | PASS |   |
|                                     3 | Delete blog post                                          | Superuser can delete a blog post                                                                                                                                                          | PASS |   |
|                                     4 | Approve comments                                          | Superuser can approve blog post comments                                                                                                                                                  | PASS |   |
|                                     5 | Delete comments                                           | Superuser can delete comments                                                                                                                                                             | PASS |   |
| **Backend Reviews**                       |                                                           |                                                                                                                                                                                           |      |   |
| **Reference**                             | **Test object**                                               | **Expected Result**                                                                                                                                                                           | Pass |   |
|                                     1 | Delete a review                                           | Superuser can delete a review                                                                                                                                                             | PASS |   |
| **Sign In**                               |                                                           |                                                                                                                                                                                           |      |   |
| **Reference                             | Test object                                               | Expected Result**                                                                                                                                                                           | Pass |   |
|                                     1 | Sign Up Link                                              | Directs the user to the sign up page                                                                                                                                                      | PASS |   |
|                                     2 | Home Link                                                 | Directs the user to the home page                                                                                                                                                         | PASS |   |
|                                     3 | Forgot Password Link                                      | Directs the user to the Password Reset page                                                                                                                                               | PASS |   |
|                                     4 | Sign In Link                                              | If the details are correct the user is redirected to the home page                                                                                                                        | PASS |   |
| **Sign Out**                              |                                                           |                                                                                                                                                                                           |      |   |
| **Reference                             | Test object                                               | Expected Result**                                                                                                                                                                           | Pass |   |
| 1                                     | Sign Out button                                           | Signs the user out of their account and redirects to the home page                                                                                                                        | PASS |   |
| **Sign Up**                               |                                                           |                                                                                                                                                                                           |      |   |
| **Reference                             | Test object                                               | Expected Result**                                                                                                                                                                           | Pass |   |
|                                     1 | Sign In Link                                              | Directs the user to the sign in page                                                                                                                                                      | PASS |   |
|                                     2 | Back to Login Link                                        | Redirects the user to the sign in page                                                                                                                                                    | PASS |   |
|                                     3 | Sign Up Link                                              | If the form is valid directs the user to the verify email address page and a confirmation email is sent to the user                                                                       | PASS |   |

[Back to top](#)

## **Automated Testing**

### **Lighthouse**
<details>
<summary>Lighthouse</summary>

![Home Page HTML Validation Results](README_docs/readme_images/testing/lighthouse/lighthouse.png)

</details>

### **Code Validation**
The [W3C Markup Validator](https://validator.w3.org/ "Link to M£C Markup Validator Site") service was used to validate the `HTML` and `CSS` code used. The [PEP8 Python Validator](http://pep8online.com/ "Link to the PEP8 Python Validator Site") was used to validate the `Python`code used. The [JSHint JavaScript Validator](https://jshint.com/ "Link to the JSHint JavaScript Validator Site") was used to validate the `JavaScript` code used.

#### **Results:**

##### **HTML Pages**
<details>
<summary>HTML Pages - HTML Validation</summary>

| Watch You Want – HTML Validation – Page Test List |                                                  |          |              |              |
|---------------------------------------------------|--------------------------------------------------|----------|--------------|--------------|
|                                                   |                                                  |          |              |              |
| Page and scenario tested                          | Checked on https://validator.w3.org/ - Live site |          | Screenshot 1 | Comments     |
| bag.html                                          | OK                                               | 24/07/22 |              |              |
| bag.html with one item                            | See image                                        | 25/07/22 |              |              |
| bag.html with three items                         | See image                                        | 25/07/22 |              |              |
| checkout_success.html – 1 item                    | OK                                               | 25/07/22 |              |              |
| checkout_success.html – 3 items                   | OK                                               | 25/07/22 |              |              |
| checkout.html – 1 item                            | OK                                               | 25/07/22 |              |              |
| checkout.html – 3 items                           | OK                                               | 25/07/22 |              |              |
| contact.html                                      | Ok                                               | 24/07/22 |              |              |
| index.html                                        | ok                                               | 24/07/22 |              |              |
| privacy.html                                      | Ok                                               | 24/07/22 |              |              |
| terms.html                                        | Ok                                               | 24/07/22 |              |              |
| products.html – all products                      | OK                                               | 24/07/22 |              |              |
| products.html – new arrivals                      | OK                                               | 24/07/22 |              |              |
| products.html – category “women”                  | OK                                               | 24/07/22 |              |              |
| products.html – category “restored”               | OK                                               | 24/07/22 |              |              |
| products.html – search with results               | OK                                               | 24/07/22 |              |              |
| products.html – search with no results            | OK                                               | 24/07/22 |              |              |
| add_product.html                                  | OK                                               | 25/07/22 |              |              |
| edit_product.html                                 | OK                                               | 25/07/22 |              |              |
| delete_product                                    |                                                  |          |              |              |
| product_detail with no reviews                    |                                                  |          |              |              |
| product_detail with reviews                       | OK                                               | 25/07/22 |              |              |
| product_detail with out of stock item             | Ok                                               |          |              |              |
| add_review.html                                   | OK                                               | 26/07/22 |              |              |
| login.html                                        | OK                                               | 25/07/22 |              |              |
| logout.html                                       | OK                                               | 25/07/22 |              |              |
| register.html                                     | OK                                               | 25/07/22 |              |              |
| blog.html                                         | OK                                               | 25/07/22 |              |              |
| blog_detail.html                                  | OK                                               | 25/07/22 | ![Blog Detail HTML Validation Results](README_docs/readme_images/testing/html/blog_detail_html.png)             | The lack of alt attributes on images uploaded to the blog seems to be a limitation of Summernote.  There are third-party extentions out there to do this with Summernote, but I lack the time to do this before my project deadline.  Of course, I could take the images out, but that would not be satisfactory in the context of the blog functionality.             |

</details>

##### **CSS stylesheets**
<details>
<summary>CSS Stylesheets - CSS Validation</summary>

![Style sheet validation results - base.css](README_docs/readme_images/testing/css/w3c_base_css.png)

![Style sheet validation results - blog.css](README_docs/readme_images/testing/css/w3c_blog_css.png)

![Style sheet validation results - checkout.css](README_docs/readme_images/testing/css/w3c_checkout_css.png)

![Style sheet validation results - profile.css](README_docs/readme_images/testing/css/w3c_profile_css.png)

</details>

##### **JavaScript Files**
<details>
<summary>JavaScript Files - JS Validation</summary>

![JS validation results - bag.html - postloadjs](README_docs/readme_images/testing/js/jshint_bag_postloadjs_warnings.png)

![JS validation results - bag.html - postloadjs](README_docs/readme_images/testing/js/jshint_bag_postloadjs_fixed.png)

![JS validation results - base.html - postloadjs](README_docs/readme_images/testing/js/jshint_base_postloadjs.png)

![JS validation results - countryfield.js](README_docs/readme_images/testing/js/jshint_countryfield.png)

![JS validation results - countryfield.js](README_docs/readme_images/testing/js/jshint_countryfield_fixed.png)

![JS validation results - quantity_input_script.js](README_docs/readme_images/testing/js/jshint_quantity_input_script.png)

![JS validation results - stripe_elements.js](README_docs/readme_images/testing/js/jshint_stripe_elements.png)

</details>

##### **Python Files**

- Bag
    <details>
    <summary>Bag Files - Python Validation</summary>

    ![Python Validation - apps.py](README_docs/readme_images/testing/bag/pep8_valid_bag_apps.png)

    ![Python Validation - contexts.py](README_docs/readme_images/testing/bag/pep8_valid_bag_contexts.png)

    ![Python Validation - urls.py](README_docs/readme_images/testing/bag/pep8_valid_bag_urls.png)

    ![Python Validation - views.py](README_docs/readme_images/testing/bag/pep8_valid_bag_views.png)

    </details>

- Blog
    <details>
    <summary>Blog Files - Python Validation</summary>

    ![Python Validation - admin.py](README_docs/readme_images/testing/blog/pep8_valid_blog_admin.png)

    ![Python Validation - apps.py](README_docs/readme_images/testing/blog/pep8_valid_blog_apps.png)

    ![Python Validation - forms.py](README_docs/readme_images/testing/bag/pep8_valid_blog_forms.png)

    ![Python Validation - models.py](README_docs/readme_images/testing/bag/pep8_valid_blog_models.png)

    ![Python Validation - urls.py](README_docs/readme_images/testing/bag/pep8_valid_blog_urls.png)

    ![Python Validation - views.py](README_docs/readme_images/testing/bag/pep8_valid_blog_views.png)

    </details>

- Checkout
    <details>
    <summary>Checkout Files - Python Validation</summary>

    ![Python Validation - admin.py](README_docs/readme_images/testing/checkout/pep8_valid_checkout_admin.png)

    ![Python Validation - apps.py](README_docs/readme_images/testing/checkout/pep8_valid_checkout_apps.png)

    ![Python Validation - forms.py](README_docs/readme_images/testing/checkout/pep8_valid_checkout_forms.png)

    ![Python Validation - models.py](README_docs/readme_images/testing/checkout/pep8_valid_checkout_models.png)

    ![Python Validation - signals.py](README_docs/readme_images/testing/checkout/pep8_valid_checkout_signals.png)

    ![Python Validation - urls.py](README_docs/readme_images/testing/checkout/pep8_valid_checkout_urls.png)

    ![Python Validation - views.py](README_docs/readme_images/testing/checkout/pep8_valid_checkout_views.png)

    ![Python Validation - webhook_handler.py](README_docs/readme_images/testing/checkout/pep8_valid_checkout_webhook_handler.png)

    ![Python Validation - webhooks.py](README_docs/readme_images/testing/checkout/pep8_valid_checkout_webhooks.png)

    </details>

- Home
    <details>
    <summary>Home Files - Python Validation</summary>

    ![Python Validation - forms.py](README_docs/readme_images/testing/home/pep8_valid_home_forms.png)

    ![Python Validation - models.py](README_docs/readme_images/testing/home/pep8_valid_home_models.png)

    ![Python Validation - urls.py](README_docs/readme_images/testing/home/pep8_valid_home_urls.png)

    ![Python Validation - views.py](README_docs/readme_images/testing/home/pep8_valid_home_views.png)

    </details>


- Products
    <details>
    <summary>Product Files - Python Validation</summary>

    ![Python Validation - admin.py](README_docs/readme_images/testing/products/pep8_valid_products_admin.png)

    ![Python Validation - apps.py](README_docs/readme_images/testing/home/pep8_valid_products_apps.png)

    ![Python Validation - forms.py](README_docs/readme_images/testing/home/pep8_valid_products_forms.png)

    ![Python Validation - models.py](README_docs/readme_images/testing/home/pep8_valid_products_models.png)

    ![Python Validation - urls.py](README_docs/readme_images/testing/home/pep8_valid_products_urls.png)

    ![Python Validation - views.py](README_docs/readme_images/testing/home/pep8_valid_products_views.png)

    ![Python Validation - widgets.py](README_docs/readme_images/testing/home/pep8_valid_products_widgets.png)

    </details>


- Profiles
    <details>
    <summary>Profiles Files - Python Validation</summary>

    ![Python Validation - forms.py](README_docs/readme_images/testing/profiles/pep8_valid_profiles_forms.png)

    ![Python Validation - models.py](README_docs/readme_images/testing/profiles/pep8_valid_profiles_models.png)

    ![Python Validation - urls.py](README_docs/readme_images/testing/profiles/pep8_valid_profiles_urls.png)

    ![Python Validation - views.py](README_docs/readme_images/testing/profiles/pep8_valid_profiles_views.png)

    </details>


- Watch You Want

    <details>
    <summary>Watch You Want Files - Python Validation</summary>

    ![Python Validation - urls.py](README_docs/readme_images/testing/profiles/pep8_valid_wyw_urls.png)

    ![Python Validation - views.py](README_docs/readme_images/testing/profiles/pep8_valid_wyw_views.png)

    ![Python Validation - wsgi.py](README_docs/readme_images/testing/profiles/pep8_valid_wyw_wsgi.png)

    </details>

## **Project Bugs and Solutions**

### **Bag Quantity**
During testing I discovered a bug whereby the quantity of an item was being added to the basket, but it wasn't showing up as a number in the quantity increment/decrement box and the Qty on the toast was showing up as True.  I spent a lot of time looking at my contexts.py file after a conversation with Alan from Tutor Support.  However, in the end in turned out to be a problem in my add_to_bag function in views.py.  I had re-written this function several times already to incorporate my primitive stock system.  When I compared it with the Boutique Ado code, I could see that I was missing an if-else statement in my final else statement.

### **Input Field**
During HTML code validation I realised that I had set an input tag as type="disabled". See image below.
![HTML Validation Input Type](README_docs/readme_images/testing/html/readme_bug_input_disabled.png)

I had forgotten that I could not do this, but a quick Google search and [this](https://stackoverflow.com/questions/16109358/what-is-the-correct-readonly-attribute-syntax-for-input-text-elements) Stack Overflow post helped me solve the issue.

This is what the code looks like now using "disabled" correctly.

![HTML Validation Input Type Fixed](README_docs/readme_images/testing/html/bug_input_fixed.png)

## User testing 
My husband and the lovely people of Slack were asked to review the site and documentation to point out any bugs and/or user experience issues. Their helpful advice throughout the process led to a few small UX changes in order to create a better experience.

[Back to top ⇧](#)

***
