# Molekule API project

## Problem Description

This project makes use of the freely available RESTful API provided by http://football-data.org to retrieve data relate to football (soccer) in JSON format. This data is then processed using Python to retrieve the names of the top 5 goalscorers in 3 different competitions/leagues - English Premier League, Spanish League and UEFA Champions League. 


## Authentication

To enable the retrieval of data, a free account needs to be created. Once that is done, the API authentication token is provided over email. 

![image](https://user-images.githubusercontent.com/18036391/82612771-aa6c2a00-9b91-11ea-8078-b8156500a7b6.png)


## High level overview of the code

The code file is named **CallAPI.py**.

The main functionality of the code has been implemented in the helper function - **get_top_scorers()**. This function accepts JSON data as an input parameter and returns the top 5 scorers in each competition in a tabular format. 

### Sample outputs

Premier League (2019-2020 season) top 5 goalscorers

![image](https://user-images.githubusercontent.com/18036391/82613196-b7d5e400-9b92-11ea-8de0-725a7faafc4b.png)

Champions League (2019-2020 season) top 5 goalscorers





