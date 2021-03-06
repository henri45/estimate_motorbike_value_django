# Side_project_motorbike_price_estimator

In South Africa, there is no website to help you to estimate the price of your Motorbike. In April 2020, I built a tool to estimate the value of a bike. I used the data from 2 websites which are market-places for brand-new and second-hand motorbikes. I used Scrapy to collect the data and I deployed my spider with a Django app on Heroku. Then I used a Jupyter notebook to treat the data and apply machine learning to estimate the price of a motorbike. This documentation explains the different steps I followed and how to implement such a tool in your country. Everything has been coded in Python.

## Scraping the data
### Scrapy

I collected a 5000 motorbikes database using the framework Scrapy. I chose it as it was providing many features such as a pipeline, a middleware for rotating IP address and convenient tools for cleaning the data.
Many tutorial are available online. @Harry Wang helps me a lot with an easy-to-follow medium tutorial https://towardsdatascience.com/a-minimalist-end-to-end-scrapy-tutorial-part-i-11e350bcdec0. 
The infographic bellow sums up well how Scrapy is working. 

![alt text](https://github.com/henri45/estimate_motorbike_value_django/blob/master/Screen/scrapy_logic.png)


The Scrapy project can be run locally. The folder to fork is: scraper_django/estimate_motorbike_value_django/scrapy_project. 

### DataBase
I tried 3 databases for storing the ads scraped.
#### SQLite
When I was running the spider locally, SQLite appears as the best option. This relational database is easy to implement with Scrapy. Nevertheless one can't use SQLite in a production environment. Heroku suggests using PostgreSQL instead.

#### PostgreSQL
Postgres is a relational database which can be used on Heroku. One has to install the Heroku add-on. The free plans are limited to 10 000 rows though.

#### DynamoDB
DynamoDB is a NoSQL offered by Amazon. I used it as the free Tier includes 25GB.

## Scheduling the crawlers
Once my spider was working, I looked for scheduling it. I used scrapyd, Django and Heroku to deploy it. Then I realised that scheduling the spider locally with CronTab was just easier.
### Scrapyd
Scrapyd is an application for deploying Scrapy spiders. It's handy as one can run multiple spiders through a webservice. 

### Django-Scrapyd
Django is a famous Web App framework in python. I used it to wrap my Scrpayd application in order to add features (such as the possibility to schedule the spider run). The alternative would be using the scrapy commercial service https://scrapinghub.com or deploying scrapyd with a client such as Scrapyd-client (https://github.com/scrapy/scrapyd-client). I tried the second option with Heroku but at some point, it required an SSL certificate that one has to pay for.
The Django app (in this repo) is very simple. It contains the Scrapyd app and a scheduler which run the spider every x minutes.

### Using CronTab locally
Using the Heroku free plans involves having the app shutdown if no request were done. For this reason, I decided to use to collect the data from my own computer. I scheduled the crawlers with CronTab. I saved the results in an SQLite database. 

## Data utilisation
I treated the data in the Global_analyse.ipynb file.

### Data Cleaning
The most challenging part was to match the data between the 2 websites I used. The same bike has often 2 different names. It required a lot of manual correction. Also, I had to deal with many missing values. For instance, the engine displacement was missing in 25% of the ads. I created a function which collects the engine power in the title of the ads when it appears. 

### Data Visualisation

#### Explanatory Data Analysis
Here is the most important visualisation from my Explanatory Data Analysis part.

![alt text](https://github.com/henri45/estimate_motorbike_value_django/blob/master/Screen/Ads_type.png)

![alt text](https://github.com/henri45/estimate_motorbike_value_django/blob/master/Screen/Brands.png)

![alt text](https://github.com/henri45/estimate_motorbike_value_django/blob/master/Screen/Km_hist.png)

![alt text](https://github.com/henri45/estimate_motorbike_value_django/blob/master/Screen/Year_old_hist.png)

![alt text](https://github.com/henri45/estimate_motorbike_value_django/blob/master/Screen/Price_hist.png)

![alt text](https://github.com/henri45/estimate_motorbike_value_django/blob/master/Screen/BMW800GS.png)

## Predicting models
### Feature engineering

I decided to keep in the database only the bike with at least 25 ads scrapped.  I end up with 22 different bikes. I tried to use a different set of variables:

- Year
- Kilometres
- Year & Kilometers
- Brand & Model & Kilometers & Year

### Predictors 

I used the following methods:

- Linear Regression
- Polynomial Linear Regression
- Random Forest
- XGboost

### Evaluating the models

For each model, the data has been split into a training and a testing set. The Mean Absolute Error (MAE) has been used to compare them. Here are the results: 

![alt text](https://github.com/henri45/estimate_motorbike_value_django/blob/master/Screen/results_model.png)

NB: Except for the "xgb_full_data" and "random_forest_full_data", this table is actually the mean of the MAE for the 22 predictors (one per bike). For each bike, 8 different predictors have been tried. Each predictor has been trained 5 times, changing the training and testing set each time. At the end, the Mean of the 5 MAE is done to determine how effective is the predictor for this bike.

![alt text](https://github.com/henri45/estimate_motorbike_value_django/blob/master/Screen/result_model_bmw800Fgs.png)

### Going further

In order to improve the accuracy of the models, one could work on:
- removing the outliers
- collecting more data (by scrapping a new website)
- create new features using NLP in the bike description (Does the bike have ABS? Does it have any damage? Is it a first hand?)

Conclusion: I learnt a lot from this project. I improve my scrapping skills (Scrapy + Scrapyd), my knowledge in DataBase (SQLite, Postgres, Dynamo DB), my knowledge with Django and how to deploy apps on Heroku. I will keep collecting data as my next project could be building a website to help South African people to estimate the value of their motorbike. Feel free to contact me if you have any question about this project.

LinkedIn: https://www.linkedin.com/in/henri-terrasse-672850101/
