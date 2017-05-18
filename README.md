# Code Institute Stream 3 project

## About Tradeable

Tradeable is a website for those people who do not want to sell their items but they would rather trade it with somebody.
There are more and more people out there who can not sell their item because no one wants to buy it.
Trading is much powerfull these days because people can pass on items what values are lower.
For example a guy named Kyle MacDonald started with a paperclip and after 14 trades he got a house.

## About the website generally

The website uses Bootstrap for full responsiveness so it is available on all devices.
On the home page user can find instructions how the site works and also they can read the story of Kyle Macdonald.
If the user clicks on the items in the Kyle Macdonald section it will pop up a gallery. This galleries functionality comes from a Bootstrap template and the pictures are from Kyle`s blog (www.oneredpaperclip.blogspot.ie)

## Functionalities

### Login and Register

If there are no user logged in some pages (Products, Profile, Forums) are not available. In order to use the website fully the user needs to be registered and logged in.
The registration process is 2 step: first the users needs to fill in their login details, then on a another form their profile details. Without completing this form the user will not be able to upload items.
After the user logged in Django Gravatar will load their profile pictures from their email accounts. If there are no profile pictures set up then Gravatar just loads a simple account icon.

### Add Product and Trading

User can upload products on their Profile page by fill in a form. Also they are able to delete their products and check other user`s product and the details.
To make a trade a user needs to select a product what the user is intrested in, and offer one of his/her own product. Only then a offer request will be send to the other user.
The trade will only happen if the other user accepts the trade request.
Every product has a owner_id. This owner_id is the same as the unique user_id. When a trade happens the wanted product and the offered product`s owner_id will be swapped.
If the request is declined then the trade will be deleted from the database.

### Forum

It would be difficult to use the website if the users could not interact with eachother. On the forum page only admins are able to creat subjects.
Users can make creats threads in these subjects where can they make comments. Also emojies, "posted since", delete or edit post options are available.

## Technologies used

Python, Django, PostgeSQL, Amazon AWS (S3), HTML, CSS3, Javascript, Bootstrap, Font awesome, Animate.css

## Host

Heroku is used to host this app. The app was deployed to Heroku over git.
