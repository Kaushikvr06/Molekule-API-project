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

**Premier League (2019-2020 season) top 5 goalscorers**

![image](https://user-images.githubusercontent.com/18036391/82613196-b7d5e400-9b92-11ea-8de0-725a7faafc4b.png)

**Champions League (2019-2020 season) top 5 goalscorers**

![image](https://user-images.githubusercontent.com/18036391/82613334-0be0c880-9b93-11ea-9400-67c935926ef0.png)

## Next steps / improvement areas

This project is an extremely basic implementation of an API call to obtain data in JSON format and an attempt to do some exploratory data analysis on it. These are some ways in which the implementation can be improved in the future:

1. Current code obtains data only for the 2019-20 season. Historical data can be obtained for various years as an improvement to identify trends in top goalscorers across various leagues - data can be broken down by various dimensions like nationality of the player, playing position of the player etc. 
2. Matplotlib can be utilized to visualize the data that has been obtained and spot various trends.
3. Since this API token is for the free version and brings in a relatively small amount of data, it has been configured in the Python code itself. Ideally, we would be setting up the API token in a config file or a database and retrieve its value.
4. To enable data analysis and exploration on a recurring basis, a basic data pipeline can be generated so that the JSON data that is obtained is processed and stored in a database in an incremental fashion. 
5. Once the data is visualized and some trends are identified, it would be interesting to see if any machine learning algorithms can be applied on top of this data to solve some basic prediction problems. 






