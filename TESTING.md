# Testing

> [!NOTE]  
> Return back to the [README.md](README.md) file.

🛑🛑🛑🛑🛑🛑🛑🛑🛑🛑-START OF NOTES (to be deleted)

In this section, you need to convince the assessors that you have conducted enough testing to legitimately believe that the site works well.
Essentially, in this part, you should go over all of your project's features, and ensure that they all work as intended,
with the project providing an easy and straightforward way for the users to achieve their goals.

Feature-by-Feature Testing:

Go through each feature of your portfolio site and detail the testing process for each.

Explain the functionality and demonstrate how it aligns with the intended purpose. This could include:

- Navigation: Ensuring smooth transitions between pages, links directing to the correct destinations.
- Responsive Design: Checking for compatibility across various devices and screen sizes.
- Portfolio Display: Verifying that projects are properly showcased with accurate descriptions, images, and links.
- Contact Form: Testing the form submission process, ensuring the user receives a confirmation, and you receive the message.

User Experience Testing:

- Usability Testing: Have users (or simulated users) interact with the site and provide feedback. Document any issues encountered and the resolutions implemented.
- Accessibility Testing: Confirm compliance with accessibility standards (e.g., screen reader compatibility, proper alt text for images, keyboard navigation).

Compatibility Testing:

- Browser Compatibility: Testing on different browsers (Chrome, Firefox, Safari, Edge, etc.) to ensure consistent performance.
- Device Compatibility: Ensuring functionality across various devices (desktops, laptops, tablets, and mobile phones).
- Performance Testing (optional):
	- Speed and Load Testing: Tools like PageSpeed Insights or GTmetrix to check page load times and optimize where necessary.
	- Scalability Testing: Assess how the site handles increased traffic or usage.

Regression Testing:

After implementing fixes or updates, ensure that previous features and functionalities still work as intended. This prevents new changes from breaking existing features.

Documentation and Logs:

Maintain records of testing procedures, results, and any bugs encountered along with their resolutions. This helps demonstrate a systematic approach to testing and problem-solving.
User Feedback Incorporation:

If applicable, mention how user feedback has been taken into account and implemented to enhance the user experience.

🛑🛑🛑🛑🛑🛑🛑🛑🛑🛑-END OF NOTES (to be deleted)

## Code Validation

🛑🛑🛑🛑🛑🛑🛑🛑🛑🛑-START OF NOTES (to be deleted)

Use the space to discuss code validation for any of your own code files (where applicable).
You are not required to validate external libraries/frameworks, such as imported Bootstrap, Materialize, Font Awesome, etc.

**IMPORTANT**: You must provide a screenshot for each file you validate.

**PRO TIP**: Always validate the live site pages, not your local code. There could be subtle/hidden differences.

🛑🛑🛑🛑🛑🛑🛑🛑🛑🛑-END OF NOTES (to be deleted)

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

🛑🛑🛑🛑🛑🛑🛑🛑🛑🛑-START OF NOTES (to be deleted)

Use this space to discuss testing the live/deployed site on various browsers.

Consider testing AT LEAST 3 different browsers, if available on your system.

You DO NOT need to use all of the browsers below, just pick any 3 (minimum).

Recommended browsers to consider:
- [Chrome](https://www.google.com/chrome)
- [Firefox (Developer Edition)](https://www.mozilla.org/firefox/developer)
- [Edge](https://www.microsoft.com/edge)
- [Safari](https://support.apple.com/downloads/safari)
- [Brave](https://brave.com/download)
- [Opera](https://www.opera.com/download)

**IMPORTANT**: You must provide screenshots of the tested browsers, to "prove" that you've actually tested them.

Please note, there are services out there that can test multiple browser compatibilities at the same time.
Some of these are paid services, but some are free.
If you use these, you must provide a link to the source used for attribution, and multiple screenshots of the results.

Sample browser testing documentation:

🛑🛑🛑🛑🛑🛑🛑🛑🛑🛑-END OF NOTES (to be deleted)

I've tested my deployed project on multiple browsers to check for compatibility issues.

| Browser | Home | About | Contact | etc | Notes |
| --- | --- | --- | --- | --- | --- |
| Chrome | ![screenshot](documentation/browsers/browser-chrome-home.png) | ![screenshot](documentation/browsers/browser-chrome-about.png) | ![screenshot](documentation/browsers/browser-chrome-contact.png) | ![screenshot](documentation/browsers/browser-chrome-etc.png) | Works as expected |
| Firefox | ![screenshot](documentation/browsers/browser-firefox-home.png) | ![screenshot](documentation/browsers/browser-firefox-about.png) | ![screenshot](documentation/browsers/browser-firefox-contact.png) | ![screenshot](documentation/browsers/browser-firefox-etc.png) | Works as expected |
| Edge | ![screenshot](documentation/browsers/browser-edge-home.png) | ![screenshot](documentation/browsers/browser-edge-about.png) | ![screenshot](documentation/browsers/browser-chrome-edge.png) | ![screenshot](documentation/browsers/browser-edge-etc.png) | Works as expected |
| Safari | ![screenshot](documentation/browsers/browser-safari-home.png) | ![screenshot](documentation/browsers/browser-safari-about.png) | ![screenshot](documentation/browsers/browser-safari-contact.png) | ![screenshot](documentation/browsers/browser-safari-etc.png) | Minor CSS differences |
| Brave | ![screenshot](documentation/browsers/browser-brave-home.png) | ![screenshot](documentation/browsers/browser-brave-about.png) | ![screenshot](documentation/browsers/browser-brave-contact.png) | ![screenshot](documentation/browsers/browser-brave-etc.png) | Works as expected |
| Opera | ![screenshot](documentation/browsers/browser-opera-home.png) | ![screenshot](documentation/browsers/browser-opera-about.png) | ![screenshot](documentation/browsers/browser-opera-contact.png) | ![screenshot](documentation/browsers/browser-opera-etc.png) | Minor differences |
| repeat for any other tested browsers | x | x | x | x | x |

## Responsiveness

🛑🛑🛑🛑🛑🛑🛑🛑🛑🛑-START OF NOTES (to be deleted)

Use this space to discuss testing the live/deployed site on various device sizes.

The minimum requirement is for the following 3 tests:
- Mobile
- Tablet
- Desktop

**IMPORTANT**: You must provide screenshots of the tested responsiveness, to "prove" that you've actually tested them.

Using the "amiresponsive" mockup image (or similar) does not suffice the requirements.
Consider using some of the built-in device sizes in the Developer Tools.

If you have tested the project on your actual mobile phone or tablet, consider also including screenshots of these as well.
It showcases a higher level of manual tests, and can be seen as a positive inclusion!

Sample responsiveness testing documentation:

🛑🛑🛑🛑🛑🛑🛑🛑🛑🛑-END OF NOTES (to be deleted)

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
  - ![screenshot](documentation/responsiveness/Dekstop_allreviews.png)

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

Edit Review
  - ![screenshot](documentation/responsiveness/Desktop_editreview.png)

Delete Review (Modal)
  - ![screenshot](documentation/responsiveness/Desktop_deletereview_modal.png)

404 page
  - ![screenshot](documentation/responsiveness/Desktop_404.png)

Unauthorised Page
  - ![screenshot](documentation/responsiveness/Desktop_unauthorised.png)

[jump to the top](###Desktop-Dev-Tools)

</details>

### Tablet Dev Tools 
All working as expected

<details>
<summary> Click here to see the Tablet Pages </summary>

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

Edit Review
  - ![screenshot](documentation/responsiveness/Tablet_editreview.png)

Delete Review (Modal)
  - ![screenshot](documentation/responsiveness/Tablet_deletereview_modal.png)

404 page
  - ![screenshot](documentation/responsiveness/Tablet_404.png)

Unauthorised Page
  - ![screenshot](documentation/responsiveness/Tablet_unauthorised.png)

[jump to the top](###Tablet-Dev-Tools)

</details>

### Mobile Dev Tools 
All working as expected

<details>
<summary> Click here to see the Tablet Pages </summary>

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

Edit Review
  - ![screenshot](documentation/responsiveness/Mobile_editreview.png)

Delete Review (Modal)
  - ![screenshot](documentation/responsiveness/Mobile_deletereview_modal.png)

404 page
  - ![screenshot](documentation/responsiveness/Mobile_404.png)

Unauthorised Page
  - ![screenshot](documentation/responsiveness/Mobile_unauthorised.png)

[jump to the top](###Mobile-Dev-Tools)

</details>

[jump to the top](###Mobile-Dev-Tools)



## Lighthouse Audit

🛑🛑🛑🛑🛑🛑🛑🛑🛑🛑-START OF NOTES (to be deleted)

Use this space to discuss testing the live/deployed site's Lighthouse Audit reports.
Avoid testing the local version (especially if developing in Gitpod), as this can have knock-on effects of performance.

If you don't have Lighthouse in your Developer Tools,
it can be added as an [extension](https://chrome.google.com/webstore/detail/lighthouse/blipmdconlkpinefehnmjammfjpmpbjk).

Don't just test the home page (unless it's a single-page application).
Make sure to test the Lighthouse Audit results for all of your pages.

**IMPORTANT**: You must provide screenshots of the results, to "prove" that you've actually tested them.

Sample Lighthouse testing documentation:

🛑🛑🛑🛑🛑🛑🛑🛑🛑🛑-END OF NOTES (to be deleted)

I've tested my deployed project using the Lighthouse Audit tool to check for any major issues. It has issues with pages that require login, so 
I will only provide the pages that have successful lighthouse reports, the all_reviews pages has identical functionality and design to the approved,
unapproved and pending reviews pages so will have almost identical performance. 

| Page | Mobile | Desktop | Notes |
| --- | --- | --- | --- |
| Home | ![screenshot](documentation/lighthouse/Lighthouse_mobile_home.png) | ![screenshot](documentation/lighthouse/Lighthouse_desktop_home.png) | Some minor warnings |
| About | ![screenshot](documentation/lighthouse/Lighthouse_mobile_about.png) | ![screenshot](documentation/lighthouse/Lighthouse_desktop_about.png) | Some minor warnings |
| all_reviews | ![screenshot](documentation/lighthouse/Lighthouse_mobile_allreviews.png) | ![screenshot](documentation/lighthouse/Lighthouse_desktop_allreviews.png) | Slow response time due to large images |
| review_detail | ![screenshot](documentation/lighthouse/Lighthouse_mobile_reviewdetail.png) | ![screenshot](documentation/lighthouse/Lighthouse_desktop_reviewdetail.png) | Slow response time due to large images |

## Defensive Programming

🛑🛑🛑🛑🛑🛑🛑🛑🛑🛑-START OF NOTES (to be deleted)

Defensive programming (defensive design) is extremely important!

When building projects that accept user inputs or forms, you should always test the level of security for each.
Examples of this could include (not limited to):

Forms:
- Users cannot submit an empty form
- Users must enter valid email addresses

PP3 (Python-only):
- Users must enter a valid letter/word/string when prompted
- Users must choose from a specific list only

MS3 (Flask) | MS4/PP4/PP5 (Django):
- Users cannot brute-force a URL to navigate to a restricted page
- Users cannot perform CRUD functionality while logged-out
- User-A should not be able to manipulate data belonging to User-B, or vice versa
- Non-Authenticated users should not be able to access pages that require authentication
- Standard users should not be able to access pages intended for superusers

You'll want to test all functionality on your application, whether it's a standard form,
or uses CRUD functionality for data manipulation on a database.
Make sure to include the `required` attribute on any form-fields that should be mandatory.
Try to access various pages on your site as different user types (User-A, User-B, guest user, admin, superuser).

You should include any manual tests performed, and the expected results/outcome.

Testing should be replicable.
Ideally, tests cases should focus on each individual section of every page on the website.
Each test case should be specific, objective, and step-wise replicable.

Instead of adding a general overview saying that everything works fine,
consider documenting tests on each element of the page
(ie. button clicks, input box validation, navigation links, etc.) by testing them in their happy flow,
and also the bad/exception flow, mentioning the expected and observed results,
and drawing a parallel between them where applicable.

Consider using the following format for manual test cases:

Expected Outcome / Test Performed / Result Received / Fixes Implemented

- **Expected**: "Feature is expected to do X when the user does Y."
- **Testing**: "Tested the feature by doing Y."
- (either) **Result**: "The feature behaved as expected, and it did Y."
- (or) **Result**: "The feature did not respond to A, B, or C."
- **Fix**: "I did Z to the code because something was missing."

Use the table below as a basic start, and expand on it using the logic above.

🛑🛑🛑🛑🛑🛑🛑🛑🛑🛑-END OF NOTES (to be deleted)

Defensive programming was manually tested with the below user acceptance testing:

| Page | Expectation | Test | Result | Fix | Screenshot |
| --- | --- | --- | --- | --- | --- |
| Home | | | | | |
| | Feature is expected to do X when the user does Y | Tested the feature by doing Y | The feature behaved as expected, and it did Y | Test concluded and passed | ![screenshot](documentation/features/feature01.png) |
| | Feature is expected to do X when the user does Y | Tested the feature by doing Y | The feature did not respond to A, B, or C. | I did Z to the code because something was missing | ![screenshot](documentation/features/feature02.png) |
| About | | | | | |
| | Feature is expected to do X when the user does Y | Tested the feature by doing Y | The feature behaved as expected, and it did Y | Test concluded and passed | ![screenshot](documentation/features/feature03.png) |
| | Feature is expected to do X when the user does Y | Tested the feature by doing Y | The feature did not respond to A, B, or C. | I did Z to the code because something was missing | ![screenshot](documentation/features/feature04.png) |
| Profile | | | | | |
| | Feature is expected to do X when the user does Y | Tested the feature by doing Y | The feature behaved as expected, and it did Y | Test concluded and passed | ![screenshot](documentation/features/feature05.png) |
| | Feature is expected to do X when the user does Y | Tested the feature by doing Y | The feature did not respond to A, B, or C. | I did Z to the code because something was missing | ![screenshot](documentation/features/feature06.png) |
| Create Review | | | | | |
| | Feature is expected to do X when the user does Y | Tested the feature by doing Y | The feature behaved as expected, and it did Y | Test concluded and passed | ![screenshot](documentation/features/feature07.png) |
| | Feature is expected to do X when the user does Y | Tested the feature by doing Y | The feature did not respond to A, B, or C. | I did Z to the code because something was missing | ![screenshot](documentation/features/feature08.png) |
| repeat for all remaining pages | x | x | x | x | x |

🛑🛑🛑🛑🛑🛑🛑🛑🛑🛑-START OF NOTES (to be deleted)

Another way of performing defensive testing is a simple Pass/Fail for each test.
The assessors prefer the above method, with the full test explained, but this is also acceptable in most cases.

When in doubt, use the above method instead, and delete the table below.

🛑🛑🛑🛑🛑🛑🛑🛑🛑🛑-END OF NOTES (to be deleted)

| Page | User Action | Expected Result | Pass/Fail | Comments |
| --- | --- | --- | --- | --- |
| Home | | | | |
| | Click on Logo | Redirection to Home page | Pass | |
| | Click on Home link in navbar | Redirection to Home page | Pass | |
| Gallery | | | | |
| | Click on Gallery link in navbar | Redirection to Gallery page | Pass | |
| | Load gallery images | All images load as expected | Pass | |
| Contact | | | | |
| | Click on Contact link in navbar | Redirection to Contact page | Pass | |
| | Enter first/last name | Field will accept freeform text | Pass | |
| | Enter valid email address | Field will only accept email address format | Pass | |
| | Enter message in textarea | Field will accept freeform text | Pass | |
| | Click the Submit button | Redirects user to form-dump | Pass | User must click 'Back' button to return |
| Sign Up | | | | |
| | Click on Sign Up button | Redirection to Sign Up page | Pass | |
| | Enter valid email address | Field will only accept email address format | Pass | |
| | Enter valid password (twice) | Field will only accept password format | Pass | |
| | Click on Sign Up button | Asks user to confirm email page | Pass | Email sent to user |
| | Confirm email | Redirects user to blank Sign In page | Pass | |
| Log In | | | | |
| | Click on the Login link | Redirection to Login page | Pass | |
| | Enter valid email address | Field will only accept email address format | Pass | |
| | Enter valid password | Field will only accept password format | Pass | |
| | Click Login button | Redirects user to home page | Pass | |
| Log Out | | | | |
| | Click Logout button | Redirects user to logout page | Pass | Confirms logout first |
| | Click Confirm Logout button | Redirects user to home page | Pass | |
| Profile | | | | |
| | Click on Profile button | User will be redirected to the Profile page | Pass | |
| | Click on the Edit button | User will be redirected to the edit profile page | Pass | |
| | Click on the My Orders link | User will be redirected to the My Orders page | Pass | |
| | Brute forcing the URL to get to another user's profile | User should be given an error | Pass | Redirects user back to own profile |
| repeat for all remaining pages | x | x | x | x |

🛑🛑🛑🛑🛑🛑🛑🛑🛑🛑-START OF NOTES (to be deleted)

Repeat for all other tests, as applicable to your own site.
The aforementioned tests are just an example of a few different project scenarios.

🛑🛑🛑🛑🛑🛑🛑🛑🛑🛑-END OF NOTES (to be deleted)

## User Story Testing

🛑🛑🛑🛑🛑🛑🛑🛑🛑🛑-START OF NOTES (to be deleted)

Testing user stories is actually quite simple, once you've already got the stories defined on your README.

Most of your project's **features** should already align with the **user stories**,
so this should as simple as creating a table with the user story, matching with the re-used screenshot
from the respective feature.

🛑🛑🛑🛑🛑🛑🛑🛑🛑🛑-END OF NOTES (to be deleted)

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

🛑🛑🛑🛑🛑🛑🛑🛑🛑🛑-START OF NOTES (to be deleted)

This section is primarily used for JavaScript and Python applications,
but feel free to use this section to document any HTML/CSS bugs you might run into.

It's very important to document any bugs you've discovered while developing the project.
Make sure to include any necessary steps you've implemented to fix the bug(s) as well.

**PRO TIP**: screenshots of bugs are extremely helpful, and go a long way!

🛑🛑🛑🛑🛑🛑🛑🛑🛑🛑-END OF NOTES (to be deleted)

- JS Uncaught ReferenceError: `foobar` is undefined/not defined

    ![screenshot](documentation/bugs/bug01.png)

    - To fix this, I _____________________.

- JS `'let'` or `'const'` or `'template literal syntax'` or `'arrow function syntax (=>)'` is available in ES6 (use `'esversion: 11'`) or Mozilla JS extensions (use moz).

    ![screenshot](documentation/bugs/bug02.png)

    - To fix this, I _____________________.

- Python `'ModuleNotFoundError'` when trying to import module from imported package

    ![screenshot](documentation/bugs/bug03.png)

    - To fix this, I _____________________.

- Django `TemplateDoesNotExist` at /appname/path appname/template_name.html

    ![screenshot](documentation/bugs/bug04.png)

    - To fix this, I _____________________.

- Python `E501 line too long` (93 > 79 characters)

    ![screenshot](documentation/bugs/bug04.png)

    - To fix this, I _____________________.

### GitHub **Issues**

🛑🛑🛑🛑🛑🛑🛑🛑🛑🛑-START OF NOTES (to be deleted)

An improved way to manage bugs is to use the built-in **Issues** tracker on your GitHub repository.
To access your Issues, click on the "Issues" tab at the top of your repository.
Alternatively, use this link: https://github.com/Quaim/Capstone_Django_Project/issues

If using the Issues tracker for your bug management, you can simplify the documentation process.
Issues allow you to directly paste screenshots into the issue without having to first save the screenshot locally,
then uploading into your project.

You can add labels to your issues (`bug`), assign yourself as the owner, and add comments/updates as you progress with fixing the issue(s).

Once you've sorted the issue, you should then "Close" it.

When showcasing your bug tracking for assessment, you can use the following format:

🛑🛑🛑🛑🛑🛑🛑🛑🛑🛑-END OF NOTES (to be deleted)

**Fixed Bugs**

[![GitHub issue custom search](https://img.shields.io/github/issues-search?query=repo%3AQuaim%2FCapstone_Django_Project%20label%3Abug&label=bugs)](https://github.com/Quaim/Capstone_Django_Project/issues?q=is%3Aissue+is%3Aclosed+label%3Abug)

All previously closed/fixed bugs can be tracked [here](https://github.com/Quaim/Capstone_Django_Project/issues?q=is%3Aissue+is%3Aclosed).

| Bug | Status |
| --- | --- |
| [JS Uncaught ReferenceError: `foobar` is undefined/not defined](https://github.com/Quaim/Capstone_Django_Project/issues/1) | Closed |
| [Python `'ModuleNotFoundError'` when trying to import module from imported package](https://github.com/Quaim/Capstone_Django_Project/issues/2) | Closed |
| [Django `TemplateDoesNotExist` at /appname/path appname/template_name.html](https://github.com/Quaim/Capstone_Django_Project/issues/3) | Closed |

**Open Issues**

[![GitHub issues](https://img.shields.io/github/issues/Quaim/Capstone_Django_Project)](https://github.com/Quaim/Capstone_Django_Project/issues)
[![GitHub closed issues](https://img.shields.io/github/issues-closed/Quaim/Capstone_Django_Project)](https://github.com/Quaim/Capstone_Django_Project/issues?q=is%3Aissue+is%3Aclosed)

Any remaining open issues can be tracked [here](https://github.com/Quaim/Capstone_Django_Project/issues).

| Bug | Status |
| --- | --- |
| [JS `'let'` or `'const'` or `'template literal syntax'` or `'arrow function syntax (=>)'` is available in ES6 (use `'esversion: 11'`) or Mozilla JS extensions (use moz).](https://github.com/Quaim/Capstone_Django_Project/issues/4) | Open |
| [Python `E501 line too long` (93 > 79 characters)](https://github.com/Quaim/Capstone_Django_Project/issues/5) | Open |

## Unfixed Bugs

🛑🛑🛑🛑🛑🛑🛑🛑🛑🛑-START OF NOTES (to be deleted)

You will need to mention unfixed bugs and why they were not fixed.
This section should include shortcomings of the frameworks or technologies used.
Although time can be a big variable to consider, paucity of time and difficulty understanding
implementation is not a valid reason to leave bugs unfixed.

If you've identified any unfixed bugs, no matter how small, be sure to list them here.
It's better to be honest and list them, because if it's not documented and an assessor finds the issue,
they need to know whether or not you're aware of them as well, and why you've not corrected/fixed them.

Some examples:

🛑🛑🛑🛑🛑🛑🛑🛑🛑🛑-END OF NOTES (to be deleted)

- On devices smaller than 375px, the page starts to have `overflow-x` scrolling.

    ![screenshot](documentation/bugs/unfixed-bug01.png)

    - Attempted fix: I tried to add additional media queries to handle this, but things started becoming too small to read.

- For PP3, when using a helper `clear()` function, any text above the height of the terminal does not clear, and remains when you scroll up.

    ![screenshot](documentation/bugs/unfixed-bug02.png)

    - Attempted fix: I tried to adjust the terminal size, but it only resizes the actual terminal, not the allowable area for text.

- When validating HTML with a semantic `section` element, the validator warns about lacking a header `h2-h6`. This is acceptable.

    ![screenshot](documentation/bugs/unfixed-bug03.png)

    - Attempted fix: this is a known warning and acceptable, and my section doesn't require a header since it's dynamically added via JS.

🛑🛑🛑🛑🛑🛑🛑🛑🛑🛑-START OF NOTES (to be deleted)

If you legitimately cannot find any unfixed bugs or warnings, then use the following sentence:

🛑🛑🛑🛑🛑🛑🛑🛑🛑🛑-END OF NOTES (to be deleted)

> [!NOTE]  
> There are no remaining bugs that I am aware of.
