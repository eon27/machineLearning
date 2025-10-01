# Machine Learning

*Machine Learning from Google course:*
https://developers.google.com/machine-learning

## Linear regression

Linear regression is the concept of modelling a mathematical relation between the parameters (features) and the values (labels).
*Value = bias + weight * parameter_1*
or
*lable = bias + weight * feature_1*

###For example: 
**how size of apartment correlates to the rent.**
*rent = base_rent + correlation_value * size_m^2*

## Loss
The regression model tries to make a mathematical relation between features and lables.
To evaluate how correct this mathematical relation is, we calculate the loss of the model against a dataset.

The loss for each point is how far the value of the datapoint is from the value that the mathematical relation gets for those features
loss = |*datapoint - math_value*|

We do this for all points in the dataset to evaluate the accuracy of the formula, with some caviates.
There are 5 ways to calculate the loss of the dataset:
  Loss                          type	Definition	                                                                      Equation
  L1 loss                       The sum of the absolute values of the difference                                        Sum(|actual_value - predicted_value|)
                                between the predicted values and the actual values.
                                
Mean absolute error (MAE)	      The average of L1 losses across a set of N examples.                                    Sum(|actual_value - predicted_value|) / N

L2 loss	                        The sum of the squared difference between the predicted values and the actual values.	  Sum( (actual_value - predicted_value)^2 )

Mean squared error (MSE)	      The average of L2 losses across a set of N examples.	                                  Sum( (actual_value - predicted_value)^2 ) / N

Root mean squared error (RMSE)	The square root of the mean squared error (MSE).	                                      Sqrt( Sum( (actual_value - predicted_value)^2 ) / N )

## Gradient decent

The method for finding the minimum loss of the linear regression model against a dataset.

