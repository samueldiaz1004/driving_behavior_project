# Driving Behavior Project

<p align="center">
  <img src="https://user-images.githubusercontent.com/71342016/191650531-26374da8-0bb9-421f-9ae1-60580d94908b.jpg" width="400px" />
</p>

## Context
Aggressive driving behavior is the leading factor of road traffic accidents. As reported by the AAA Foundation for Traffic Safety, 
106,727 fatal crashes – 55.7 percent of the total – during a recent four-year period involved drivers who committed one or more 
aggressive driving actions. Therefore, how to predict dangerous driving behavior quickly and accurately?

## Dataset Content

* Sampling Rate: 2 samples (rows) per second.
* Gravitational acceleration: removed.
* Sensors: Accelerometer and Gyroscope.
* Data:
  * Acceleration (X,Y,Z axis in meters per second squared (m/s<sup>2</sup>))
  * Rotation (X,Y, Z axis in degrees per second (°/s))
  * Classification label (SLOW, NORMAL, AGGRESSIVE)
  * Timestamp (time in seconds)
* Driving Behaviors:
  * Slow
  * Normal
  * Aggressive
* Device: Samsung Galaxy S21

## Requirements
* A recent version of Python3
* Jupyter server environment
* Pip to install all the libraries listed in `requirements.txt`

## Solution Approach
Aggressive driving includes speeding, sudden breaks and sudden left or right turns. All these events are reflected on accelerometer and gyroscope data.
Analyse the data variables and select the relevant variables and even handcraft extra features. Train and test clasification algorithms such as 
[KNN](https://en.wikipedia.org/wiki/K-nearest_neighbors_algorithm), [Random Forest](https://en.wikipedia.org/wiki/Random_forest) and 
[Logistic Regression](https://en.wikipedia.org/wiki/Logistic_regression). Determine the best model for this dataset and suggest what actions could have been taken
to improve the results.

## Development
Detailed information of the project can be found in the `Results.pdf` and implementation of the algorithms in the `models` directory.

## Credits
The original problem and dataset can be found on [Kaggle](https://www.kaggle.com/datasets/outofskills/driving-behavior).
