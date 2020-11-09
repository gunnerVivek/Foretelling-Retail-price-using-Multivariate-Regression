# Foretelling-Retail-price-using-Multivariate-Regression
The clients wanted to find if the prices they were being charged / produced invoice for, were reasonable or were they 
being taken advantage of.

# DATA
Data provided is divided into TRAIN SET and TEST SET. Training data has $284780$ observations and $8$ variables (including target), and Test data has $122049$ observations and $7$ variables.
### Attribute Description:
Attribute | Description
----------|-------------
Invoice No | Invoice ID, encoded as Label
StockCode | Unique code per stock, encoded as Label
Description | The Description, encoded as Label
Quantity | Quantity purchased
InvoiceDate | Date of purchase
UnitPrice | The target value, price of every product
CustomerID | Unique Identifier for every country
Country | Country of sales, encoded as Label

# Machine Learning Formulation
The use case lends itself as a Multivariate Regression problem.
### Performance Metric
RMSE (Root Mean Square Error)