# Testing

> [!NOTE]  
> Return back to the [README.md](README.md) file.

## Code Validation

### HTML

I have used the recommended [HTML W3C Validator](https://validator.w3.org) to validate all of my HTML files, i used the source code as direct input to avoid issues that come with using certain technologies such as bootstrap and using python variables.

| Directory | File | Screenshot | Notes |
| --- | --- | --- | --- |
| reviews | about.html | ![screenshot](documentation/validation/About_validator.w3.org_nu_.png) | |
| reviews | all_reviews.html | ![screenshot](documentation/validation/All_Reviews_validator.w3.org_nu_.png) | |
| reviews | approved_reviews.html | ![screenshot](documentation/validation/Approved_Reviews_validator.w3.org_nu_.png) | |
| reviews | create_review.html | ![screenshot](documentation/validation/Create_Review_validator.w3.org_nu_.png) |The manytomany fields had same class so registered a duplicate attribute error, unavoidable  |
| reviews | edit_review.html | ![screenshot](documentation/validation/Editreview_validator.png) | same unavoidable errors as the create review due to manytomany fields |
| reviews | index.html | ![screenshot](documentation/validation/Home_validator.w3.org_nu_.png) | |
| reviews | pending_reviews.html | ![screenshot](documentation/validation/Pending_Reviews_validator.w3.org_nu_.png) | |
| reviews | profile.html | ![screenshot](documentation/validation/Profile_validator.w3.org_nu_.png) | |
| reviews | review_detail.html | ![screenshot](documentation/validation/Search_Results_validator.w3.org_nu_.png) | |
| reviews | search_result.html | ![screenshot](documentation/validation/path-to-screenshot.png) | |
| reviews | unapproved_reviews.html | ![screenshot](documentation/validation/Unapproved_Reviews_validator.w3.org_nu_.png) | |
| templates | 404.html | ![screenshot](documentation/validation/404_validator.w3.org_nu_.png) | |
| templates | unauthorised.html | ![screenshot](documentation/validation/Unauthorised_validator.w3.org_nu_.png) | |


### CSS

I have used the recommended [CSS Jigsaw Validator](https://jigsaw.w3.org/css-validator) to validate all of my CSS files.

| Directory | File | Screenshot | Notes |
| --- | --- | --- | --- |
| static | style.css | ![screenshot](documentation/validation/CSS_jigsaw.w3.org_css-validator_validator.png) | |

### JavaScript

I did not use any custom javascript for this project.

### Python

I have used the recommended [PEP8 CI Python Linter](https://pep8ci.herokuapp.com) to validate all of my Python files.

| Directory | File | CI URL | Screenshot | Notes |
| --- | --- | --- | --- | --- |
| gamersgambit | settings.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/Quaim/Capstone_Django_Project/main/gamersgambit/settings.py) | ![screenshot](documentation/validation/Python_validator_settings.png) | |
| gamersgambit | urls.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/Quaim/Capstone_Django_Project/main/gamersgambit/urls.py) | ![screenshot](documentation/validation/Python_validator_urls.png) | |
|  | manage.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/Quaim/Capstone_Django_Project/main/manage.py) | ![screenshot](documentation/validation/Python_validator_manage.png) | |
| reviews | admin.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/Quaim/Capstone_Django_Project/main/reviews/admin.py) | ![screenshot](documentation/validation/Python_validator_admin.png) | |
| reviews | forms.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/Quaim/Capstone_Django_Project/main/reviews/forms.py) | ![screenshot](documentation/validation/Python_validator_forms.png) | |
| reviews | models.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/Quaim/Capstone_Django_Project/main/reviews/models.py) | ![screenshot](documentation/validation/Python_validator_models.png) | |
| reviews | urls.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/Quaim/Capstone_Django_Project/main/reviews/urls.py) | ![screenshot](documentation/validation/Python_validator_reviews_urls.png) | |
| reviews | views.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/Quaim/Capstone_Django_Project/main/reviews/views.py) | ![screenshot](documentation/validation/Python_validator_views.png) | |

## Browser Compatibility

I've tested my deployed project on multiple browsers to check for compatibility issues. The resolution for each test was 1024x834.
I didnt test on every single page, I chose home, about, profile, all reviews and review detail(approve,unapproved,pending and search results have the same layout/functionality)

### Chrome
All working as expected

<details>
<summary> Click here to see the Chrome Pages </summary>

Home
  - ![screenshot](documentation/browsers/Chrome_home.png)

About
  - ![screenshot](documentation/browsers/Chrome_about.png)

All Reviews
  - ![screenshot](documentation/browsers/Chrome_allreviews.png)

Profile
  - ![screenshot](documentation/browsers/Chrome_profile.png)

Review Detail
  - ![screenshot](documentation/browsers/Chrome_reviewdetail.png)

</details>

### Firefox(developer)
All working as expected

<details>
<summary> Click here to see the Firefox(developer) Pages </summary>

Home
  - ![screenshot](documentation/browsers/Firefox_home.png)

About
  - ![screenshot](documentation/browsers/Firefox_about.png)

All Reviews
  - ![screenshot](documentation/browsers/Firefox_allreviews.png)

Profile
  - ![screenshot](documentation/browsers/Firefox_profile.png)

Review Detail
  - ![screenshot](documentation/browsers/Firefox_reviewdetail.png)

</details>

### Opera
All working as expected

<details>
<summary> Click here to see the Opera Pages </summary>

Home
  - ![screenshot](documentation/browsers/Opera_home.png)

About
  - ![screenshot](documentation/browsers/Opera_about.png)

All Reviews
  - ![screenshot](documentation/browsers/Opera_allreviews.png)

Profile
  - ![screenshot](documentation/browsers/Opera_profile.png)

Review Detail
  - ![screenshot](documentation/browsers/Opera_reviewdetail.png)

</details>

## Responsiveness

I've tested my deployed project on multiple devices in chrome dev tools to check for responsiveness issues.

### Desktop Dev Tools 
All working as expected

<details>
<summary> Click here to see the Desktop Pages </summary>

Home
  - ![screenshot](documentation/responsiveness/Desktop_home.png)

About
  - ![screenshot](documentation/responsiveness/Desktop_about.png)

All Reviews
  - ![screenshot](documentation/responsiveness/Desktop_allreviews.png)

Review Detail
  - ![screenshot](documentation/responsiveness/Desktop_reviewdetail_loggedout.png)

Search Result
  - ![screenshot](documentation/responsiveness/Desktop_searchresults.png)

Profile
  - ![screenshot](documentation/responsiveness/Desktop_profile.png)

Approved Review
  - ![screenshot](documentation/responsiveness/Desktop_approvedreviews.png)

Unapproved Review
  - ![screenshot](documentation/responsiveness/Desktop_unapprovedreviews.png)

Pending Reviews 
  - ![screenshot](documentation/responsiveness/Desktop_pendingreviews.png)

Sign In
  - ![screenshot](documentation/responsiveness/Desktop_signin.png)

Register
  - ![screenshot](documentation/responsiveness/Desktop_register.png)

Sign Out
  - ![screenshot](documentation/responsiveness/Desktop_signout.png)

Create Review
  - ![screenshot](documentation/responsiveness/Desktop_createreview.png)

Delete Review (Modal)
  - ![screenshot](documentation/responsiveness/Desktop_deletereview_modal.png)

404 page
  - ![screenshot](documentation/responsiveness/Desktop_404.png)

Unauthorised Page
  - ![screenshot](documentation/responsiveness/Desktop_unauthorised.png)


</details>

### Tablet Dev Tools - IPAD (768X1024)
All working as expected

<details>
<summary> Click here to see the Tablet/Ipad Pages </summary>

Home
  - ![screenshot](documentation/responsiveness/with_frames/Ipad_home.png)

About
  - ![screenshot](documentation/responsiveness/with_frames/Ipad_about.png)

All Reviews
  - ![screenshot](documentation/responsiveness/with_frames/Ipad_allreviews.png)

Review Detail
  - ![screenshot](documentation/responsiveness/with_frames/Ipad_reviewdetail.png)

Search Result
  - ![screenshot](documentation/responsiveness/with_frames/Ipad_searchresults.png)

Profile
  - ![screenshot](documentation/responsiveness/with_frames/Ipad_profile.png)

Approved Review
  - ![screenshot](documentation/responsiveness/with_frames/Ipad_approvedreviews.png)

Unapproved Review
  - ![screenshot](documentation/responsiveness/with_frames/Ipad_unapprovedreviews.png)

Pending Reviews 
  - ![screenshot](documentation/responsiveness/with_frames/Ipad_pendingreviews.png)

Sign In
  - ![screenshot](documentation/responsiveness/with_frames/Ipad_login.png)

Register
  - ![screenshot](documentation/responsiveness/with_frames/Ipad_register.png)

Sign Out
  - ![screenshot](documentation/responsiveness/with_frames/Ipad_signout.png)

Create Review
  - ![screenshot](documentation/responsiveness/with_frames/Ipad_createreview.png)

404 page
  - ![screenshot](documentation/responsiveness/with_frames/Ipad_404.png)

Unauthorised Page
  - ![screenshot](documentation/responsiveness/with_frames/Ipad_unauthorised.png)


</details>


### Tablet Dev Tools Full View Port 
All working as expected

<details>
<summary> Click here to see the Tablet full view port Pages </summary>

Home
  - ![screenshot](documentation/responsiveness/Tablet_home.png)

About
  - ![screenshot](documentation/responsiveness/Tablet_about.png)

All Reviews
  - ![screenshot](documentation/responsiveness/Tablet_allreviews.png)

Review Detail
  - ![screenshot](documentation/responsiveness/Tablet_reviewdetail_loggedout.png)

Search Result
  - ![screenshot](documentation/responsiveness/Tablet_searchresults.png)

Profile
  - ![screenshot](documentation/responsiveness/Tablet_profile.png)

Approved Review
  - ![screenshot](documentation/responsiveness/Tablet_approvedreviews.png)

Unapproved Review
  - ![screenshot](documentation/responsiveness/Tablet_unapprovedreviews.png)

Pending Reviews 
  - ![screenshot](documentation/responsiveness/Tablet_pendingreviews.png)

Sign In
  - ![screenshot](documentation/responsiveness/Tablet_signin.png)

Register
  - ![screenshot](documentation/responsiveness/Tablet_register.png)

Sign Out
  - ![screenshot](documentation/responsiveness/Tablet_signout.png)

Create Review
  - ![screenshot](documentation/responsiveness/Tablet_createreview.png)

404 page
  - ![screenshot](documentation/responsiveness/Tablet_404.png)

Unauthorised Page
  - ![screenshot](documentation/responsiveness/Tablet_unauthorised.png)


</details>

### Mobile Dev Tools IPhone 6/7/8 Plus (414x736)
All working as expected

<details>
<summary> Click here to see the Mobile/Iphone pages </summary>

Home
  - ![screenshot](documentation/responsiveness/with_frames/Iphone_home.png)

About
  - ![screenshot](documentation/responsiveness/with_frames/Iphone_about.png)

All Reviews
  - ![screenshot](documentation/responsiveness/with_frames/Iphone_allreviews.png)

Review Detail
  - ![screenshot](documentation/responsiveness/with_frames/Iphone_reviewdetail.png)

Search Result
  - ![screenshot](documentation/responsiveness/with_frames/Iphone_searchresults.png)

Profile
  - ![screenshot](documentation/responsiveness/with_frames/Iphone_profile.png)

Approved Review
  - ![screenshot](documentation/responsiveness/with_frames/Iphone_approvedreviews.png)

Unapproved Review
  - ![screenshot](documentation/responsiveness/with_frames/Iphone_unapprovedreviews.png)

Pending Reviews 
  - ![screenshot](documentation/responsiveness/with_frames/Iphone_pendingreviews.png)

Sign In
  - ![screenshot](documentation/responsiveness/with_frames/Iphone_login.png)

Register
  - ![screenshot](documentation/responsiveness/with_frames/Iphone_register.png)

Sign Out
  - ![screenshot](documentation/responsiveness/with_frames/Iphone_signout.png)

Create Review
  - ![screenshot](documentation/responsiveness/with_frames/Iphone_createreview.png)

404 page
  - ![screenshot](documentation/responsiveness/with_frames/Ipad_404.png)

Unauthorised Page
  - ![screenshot](documentation/responsiveness/with_frames/Ipad_unauthorised.png)

</details>


### Mobile Dev Tools Full View Port 
All working as expected

<details>
<summary> Click here to see the Mobile full view port pages </summary>

Home
  - ![screenshot](documentation/responsiveness/Mobile_home.png)

About
  - ![screenshot](documentation/responsiveness/Mobile_about.png)

All Reviews
  - ![screenshot](documentation/responsiveness/Mobile_allreviews.png)

Review Detail
  - ![screenshot](documentation/responsiveness/Mobile_reviewdetail_loggedout.png)

Search Result
  - ![screenshot](documentation/responsiveness/Mobile_searchresults.png)

Profile
  - ![screenshot](documentation/responsiveness/Mobile_profile.png)

Approved Review
  - ![screenshot](documentation/responsiveness/Mobile_approvedreviews.png)

Unapproved Review
  - ![screenshot](documentation/responsiveness/Mobile_unapprovedreviews.png)

Pending Reviews 
  - ![screenshot](documentation/responsiveness/Mobile_pendingreviews.png)

Sign In
  - ![screenshot](documentation/responsiveness/Mobile_signin.png)

Register
  - ![screenshot](documentation/responsiveness/Mobile_register.png)

Sign Out
  - ![screenshot](documentation/responsiveness/Mobile_signout.png)

Create Review
  - ![screenshot](documentation/responsiveness/Mobile_createreview.png)

404 page
  - ![screenshot](documentation/responsiveness/Mobile_404.png)

Unauthorised Page
  - ![screenshot](documentation/responsiveness/Mobile_unauthorised.png)

</details>


## Lighthouse Audit

I've tested my deployed project using the Lighthouse Audit tool to check for any major issues. It has issues with pages that require login, so 
I will only provide the pages that have successful lighthouse reports, the all_reviews pages has identical functionality and design to the approved,
unapproved and pending reviews pages so will have almost identical performance. 

| Page | Mobile | Desktop | Notes |
| --- | --- | --- | --- |
| Home | ![screenshot](documentation/lighthouse/Lighthouse_mobile_home.png) | ![screenshot](documentation/lighthouse/Lighthouse_desktop_home.png) | Some minor warnings |
| About | ![screenshot](documentation/lighthouse/Lighthouse_mobile_about.png) | ![screenshot](documentation/lighthouse/Lighthouse_desktop_about.png) | Some minor warnings |
| all_reviews | ![screenshot](documentation/lighthouse/Lighthouse_mobile_allreviews.png) | ![screenshot](documentation/lighthouse/Lighthouse_desktop_allreviews.png) | Slow response time due to large images |
| review_detail | ![screenshot](documentation/lighthouse/Lighthouse_mobile_reviewdetail.png) | ![screenshot](documentation/lighthouse/Lighthouse_desktop_reviewdetail.png) | Some minor warnings |

## Defensive Programming / Feature checking

In the section below I have manually tested each relevant page feature to test they work and tested each form and url in terms of how they hold up in terms of security, i.e users not being able to access pages they shouldnt be able to, edit or delete data that isnt theres, and forms should only be submitted if they arent empty and have a value in all required fields.

| Page | User Action/ Feature | Expected Result | Pass/Fail | Comments |
| --- | --- | --- | --- | --- |
| Navigation Bar | | | | |
| | Click on Logo | Redirection to Home page | Pass | |
| | Click on link in navbar | Redirection to relevant page | Pass | All working |
| | Register/Login | Users who arent logged in will see register/login button in navbar | Pass | |
| | Logout | Users who are logged in will see log out button in navbar | Pass | |
| | Profile | Users who are logged in will see profile button in navbar | Pass | |
| | Admin | Users who are logged in and superusers will see admin button in navbar | Pass | |
| | Active Page | An underline will make it visible which page the user is currently on | Pass | |
| Profile | | | | |
| | Load logged in user profile page | All relevant buttons load successfully | Pass | |
| | Approved reviews | If user clicks on this button and has approved reviews in database they will be taken to a page where these are rendered | Pass | |
| | Unpproved reviews | If user clicks on this button and has unapproved reviews in database they will be taken to a page where these are rendered | Pass | |   
| | Pending reviews (Admin) | If a user is a superuser/admin a pending reviews button will be visble, and if they click on this button and there are reviews pending approval in the database they will be taken to a page where these are rendered, and below each review there will be buttons to either read the full review, approve it or delete it. The approval and deletion buttons also exist in the review details page of unapproved/pending reviews. If approved the reviews approved status will change to approved and they will be added to the approved reviews(user)/all reviews pages(public). The user will be displayed a message that tells them that their approval or deletion was succesful | Pass | |  
| | No bruteforce | Only logged in users can access page, asked to log in if not | Pass | |
| | No bruteforce pending reviews | Only super users can access page, someone trying to access this url who isnt will be taken to the custom unauthorised page | Pass | |
| Create Review | | | | |
| | User must enter value in all required fields | Can't submit if a field doesnt have value | Pass | |
| | Enter title | Field will accept freeform text | Pass | |
| | Enter description | Field will accept freeform text | Pass | |
| | Pick genre | Field will accept a choice from dropdown menu | Pass | |
| | Select tags | Field will accept 1 or multiple checkboxes | Pass | |
| | Select platforms | Field will accept 1 or multiple checkboxes | Pass | |
| | Enter review in textarea | Field will accept freeform text | Pass | |
| | Select rating | Field will choice of 1 - 5 in dropdown menu | Pass | |
| | Select image | Field will accept image file, or use placeholder if left blank | Pass | |
| | Click the Submit button | Redirects to home page, message of success | Pass | |
| | Cant brute force using url | Users who arent logged in will be taken to the login page before accessing this page | Pass | |
| Edit Review | | | | |
| | User must enter value in all required fields | Can't submit if a field doesnt have value | Pass | |
| | Click on edit button in review detail | If user if author, taken to prefilled form with the relevant information rendered into each field | Pass | |
| | Edit any of the fields | User can update any of the fields in the form | Pass | |
| | Cant brute force using url | Users who arent author will receive message saying they dont have access | Pass | |
| | Click the Submit button | Redirects to home page, message of success and remove from approved reviews into pending reviews | Pass | |
| Delete Review | | | | |
| | User must be author or super user for delete button to appear | Button doesnt show/url won't work if this check is failed, successful deletion message appears once it has been confirmed by user | Pass | |
| | Try to brute force | There is no way to brute force this with the use of a URL and there are restrictions in the backend preventing any way to do this | Pass | |
| Sign Up | | | | |
| | Enter valid password that meets laid out critera | Submit wont work and will notify you of which criteria failed | Pass | |
| Log In | | | | |
| | Enter valid username/password | Field will only accept existing user, notify you if the combination are incorrect | Pass | |
| | Click Login button | Redirects user to home page | Pass | |
| Log Out | | | | |
| | Click Logout button | Redirects user to logout page | Pass | Confirms logout first |
| | Click Confirm Logout button | Redirects user to home page | Pass | |
| Review Detail | | | | |
| | Click full review button | User taken to full review page of that particular entry | Pass | |
| | Click on the Edit button | If user is author an edit button will be visible and when clicked will take them to the edit form for that review  | Pass | |
| | Click on the Delete button | If user is author or a super user a delete button will be visible and when clicked will provide a confirmation modal, and a message that it was successful or they can cancel the deletion | Pass | |
| Search Result | | | | |
| | Enter nothing in search bar | User taken to page rendering all approved reviews as the search query has nothing in it so added no additional filter to the view that renders the objects on the page | Pass | |
| | Enter query into search bar | User taken to page rendering search results with only approved reviews containing that query in the title, tag, platform or genre. If no reivews have that query in the title the page will simply have a message saying no reviews containg that query exist in the database and tell them to check their spelling just in case | Pass | |

## Feedback Messages
There are various feedback messages related so some of the features above, such as signing in, creating a rewiew, editing a review etc. 

* Logged In Message
  - ![screenshot](documentation/feedback/Loggedin_message.png)

* Logged Out Message
  - ![screenshot](documentation/feedback/Signout_message.png)

* Edit Successful Message
  - ![screenshot](documentation/feedback/Review_updated_message.png)

* Edit Access denied Message
  - ![screenshot](documentation/feedback/Edit_access_denied_message.png)

* Review Submitted Message
  - ![screenshot](documentation/feedback/Review_submitted_message.png)

* Review Approved Message
  - ![screenshot](documentation/feedback/Review_approved_message.png)

* Review Deleted Message
  - ![screenshot](documentation/feedback/Desktop_deletereview_message.png)

* Example of invalid password on register, failed criteria
  - ![screenshot](documentation/feedback/Invalidpassword_signup_message.png)


## User Story Testing

| User Story | Screenshot |
| --- | --- |
| As a user I want to be able to easily navigate between the various pages on the website so that I can access the content I am looking for efficiently. | ![screenshot](documentation/features/Desktop_navbar_loggedin.png) |
| As a user I want to be welcomed to the website by a page that gives me an idea of what the website is about and has links to other necessary pages. | ![screenshot](documentation/features/Desktop_home.png) |
| As a user I want to be able to view an about page that gives a detailed view of what the website is about so that I know what to expect from it. | ![screenshot](documentation/features/Desktop_about.png) |
| As a user I want to be able to easily access the public reviews so that I can explore the various reviews and their contents. | ![screenshot](documentation/features/Desktop_allreviews.png) |
| As a user I want to be able to view a more detailed view of a particular review, so that I can read the full length review. | ![screenshot](documentation/features/Desktop_reviewdetail_loggedout.png) |
| As a user I want to be able to search reviews so that I can easily retrieve only a certain type of review, by title, tag or platform. | ![screenshot](documentation/features/Desktop_searchresults.png) |
| As a user I want to be able to easily sign up and login to the website to access the options and content only registered users have access to. | ![screenshot](documentation/features/Desktop_register.png) |
| As a user I want visual feedback when I perform an action to let me know if my action was successful/unsuccessful. (one example) | ![screenshot](documentation/features/messages/Review_submitted_message.png) |
| As a returning user I want access to a list of my unapproved reviews so that I can easily access them for edit or deletion. | ![screenshot](documentation/features/Desktop_unapprovedreviews.png) |
| As a returning user I want to have access to a list of my approved reviews so that I can easily access them for edit or deletion. | ![screenshot](documentation/features/Desktop_approvedreviews.png) |
| As a returning user I want to be able to create, read update and delete my own reviews on the website so that others can access these reviews if they are approved. | ![screenshot](documentation/features/Desktop_reviewdetail_userowned.png) |
| As a returning user I want access to a profile page that allows me to easily access my approved and unapproved reviews. | ![screenshot](documentation/features/Desktop_profile.png) |
| As an Admin I want a profile page that allows me to easily access my approved and unapproved reviews and additonally access reviews pending approval. | ![screenshot](documentation/features/Desktop_profile_admin.png) |
| As an Admin I should be able to create, read, update and delete reviews to keep the site in order. | ![screenshot](documentation/features/Desktop_reviewdetail_notowned_admin.png) |
| As an Admin I want access to a list of reviews that are pending approval so that I can easily access them for approval or deletion. | ![screenshot](documentation/features/Desktop_pendingreviews.png) |
| As an Admin I want a link to the admin page on the front end so I can easily access the admin page for database /site management.. | ![screenshot](documentation/features/Desktop_navbar_admin.png) |
| As an Admin I can create, read, update and delete users. No screenshot available, all working.

## Bugs

**Fixed Bugs**

[![GitHub issue custom search](https://img.shields.io/github/issues-search?query=repo%3AQuaim%2FCapstone_Django_Project%20label%3Abug&label=bugs)](https://github.com/Quaim/Capstone_Django_Project/issues?q=is%3Aissue+is%3Aclosed+label%3Abug)

All previously closed/fixed bugs can be tracked [here](https://github.com/Quaim/Capstone_Django_Project/issues?q=is%3Aissue+is%3Aclosed).

| Bug | Status |
| --- | --- |
| [Delete doesnt work on front end as superuser](https://github.com/Quaim/Capstone_Django_Project/issues/16) | Closed |
| [Edit form doesnt pick up existing image](https://github.com/Quaim/Capstone_Django_Project/issues/15) | Closed |
| [Form won't upload images, however Editform will...](https://github.com/Quaim/Capstone_Django_Project/issues/14) | Closed |

**Open Issues**

[![GitHub issues](https://img.shields.io/github/issues/Quaim/Capstone_Django_Project)](https://github.com/Quaim/Capstone_Django_Project/issues)
[![GitHub closed issues](https://img.shields.io/github/issues-closed/Quaim/Capstone_Django_Project)](https://github.com/Quaim/Capstone_Django_Project/issues?q=is%3Aissue+is%3Aclosed)

Any remaining open issues can be tracked [here](https://github.com/Quaim/Capstone_Django_Project/issues).

| Bug | Status |
| --- | --- |
| [Issue on the review_detail pages where the items image gets zoomed in rather than scaling with the resolution](https://github.com/Quaim/Capstone_Django_Project/issues/33) | Open |


## Unfixed Bugs

- On all devices, the associated review image in the container zooms in on the image, more so at differnet resolutions instead of scaling the image to fit each resolution

- Full image on all_reviews(and other pages where multiple reviews are rendered) 

![screenshot](documentation/bugs/Bug_Full_Image.png)
 
- Broken image on review_detail page

![screenshot](documentation/bugs/Bug_Broken_Image.png)

    - Attempted fix: I tried to add additional media queries to handle this, but as I found out about it quite late into devlopment I ran out of time and it isnt a site breaking issue so will have to fix it in the next iteration of the site.
