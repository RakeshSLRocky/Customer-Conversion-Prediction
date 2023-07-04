<h1 align="center"> Customer-Conversion-Prediction</h1>

**Problem Statement**

You are working for a new-age insurance company and employ mutiple outreach plans to sell term insurance to your customers. Telephonic marketing campaigns still remain one of the most effective way to reach out to people however they incur a lot of cost. Hence, it is important to identify the customers that are most likely to convert beforehand so that they can be specifically targeted via call. We are given the historical marketing data of the insurance company and are required to build a ML model that will predict if a client will subscribe to the insurance. 

**Data**

The historical sales data is available in below link

https://drive.google.com/file/d/1BJ_Q8Q-kDRisAQyLltBQggeb0QmdWGZy/view?usp=sharing

**Features:** 

age (numeric)

job : type of job (Object)

marital : marital status (Object)

educational_qual : education status (Object)

call_type : contact communication type (Object)

day: last contact day of the month (numeric)

mon: last contact month of year (Object)

dur: last contact duration, in seconds (numeric)

num_calls: number of contacts performed during this campaign and for this client (Object) 

prev_outcome: outcome of the previous marketing campaign (categorical: "unknown","other","failure","success")

**Output variable (desired target):**

y - has the client subscribed to the insurance?


**Minimum Requirements**

It is not sufficient to just fit a model - the model must be analysed to find the important factors that contribute towards the conversion rate. F1-Score must be used as a metric to evaluate the performance of the models. 
