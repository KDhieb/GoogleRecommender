# HackCamp2020
Our 2020 NwPlus HackCamp submission.

# How to use:
1. Clone Repo
2. Create a directory titled "data" inside the root folder
3. Inside the "data" directory, create a file titled "apikey.txt" with your Google Places API key on the first line
4. Run the Gui class
5. Enter a keyword (such as "coffee shop", "restaurant", "grocery store" etc.)
6. Enter the maximum distance you are willing to travel in km
7. Click "Search"
8. Enjoy!

# Purpose:
During the Covid-19 pandemic, social distancing is essential to maintaining public health. As laws
surrounding public health change and become more restrictive, it's difficult to find safe public
outlets. This app is designed for users to find safe reccomendations where they can minimize contact
with others. In non-pandemic times, it's also useful for finding non-crowded places to study, or
restaurants that are not too busy if you're looking to eat as soon as possible.

# App Features:
* Search for currently open nearby business (such as coffee shops, restaurants, grocery stores, etc.) by keyword 

* Get recommended businesses based on busyness level, distance, and Google rating

* View each recommendation's business information (address, telephone number, distance, rating etc.)

* Be able to select the maximum distance you are willing to travel

# How it Works:

The app used Python for the backend and Tkinter for the graphical user interface. For the backend, the app uses Google Places API for to query for local business data based various parameteres. The local results are found using the latitude and longitude retrieved from the user's ip address. The busyness level is retreived using the popularplaces python library which scrapes Google (using the queried data) for displayed busyness data (since these metrics are not currently availlable directly from the Google Places API). The results are ranked on busyness level (from low to high) and then from distance if busyness data is not availlable. 



