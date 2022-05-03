# eCommerce Data Analysis - Profit Improvement Suggestion

# Introduction

## Background

- This data analysis project was introduced during the coding bootcamp. 
- It was a half-guided module and the problem and the preconditions are presented. 
- The insights, the visualizations and the suggestions are my original.

## Dataset

- Brazilian E-Commerce Public Dataset by Olist  

- kaggle.com/olistbr/brazilian-ecommerce

- Olist offers Logistic and Inventory Management Service to sellers

- Information about ~100k orders made between 2016 and 2018

- 8 csv files (orders, cutomers, reviews, sellers, products...etc)

## Problem statement

**How should Olist improve it's profit margin**, given that the revenue and the cost are calculated as the following condition:

**Revenue**

1. Olist takes a 10% cut on the product price (excl. freight) of each order delivered.
2. Olist charges 80 BRL by month per seller.

**Cost**

1. Estimated cost occured by bad review per order

|review_score|	cost (BRL)|
|:---:|:---:|
|1 star|100|
|2 stars|50|
|3 stars|40|
|4 stars|0|
|5 stars|0|

2. IT costss

Olist's IT costs are estimated to be proportional to *the square-root of the total cumlated number of orders approved*.

The IT department also told you that since the birth of the marketplace, cumulated IT costs have amounted to 500,000 BRL.

## Suggestion

After the data analysis on seller data, I would give the following 2 suggestions to improve the profits by at least 10 %.

**1. By removing the worst 15 sellers (0.5 % of the sellers) who make negative profits, Olist improves the profits by 10 %**

**2. By charging 10 % of the review cost directly to the sellers, Olist improves the profits by 13.9 %**
