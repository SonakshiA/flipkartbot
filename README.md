# flipkartbot
A simple project that integrates Selenium and Scrapy frameworks

This project is written in Python. 

# Extracted Data
This project extracts the title, price and ratings of Agatha Christie Books from Flipkart. The structure of extracted data is:
```
{ 'title' : ['Murder On The Orient Express'],
'price' : [184],
'rating' : [4.6]
}
```
# Storing Data

After extracting the data using Scrapy, it is stored in an sqlite3 database.
The title of the book with the highest rating is found out.

# Automation Using Selenium

The user is logged into Flipkart using automation.
The book title is sent to the search bar. 
The user is given option to add item to cart or buy it.

