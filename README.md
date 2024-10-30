<img src="logo.png" width="100" height="100"><br>
# FlaskDecisionTree
<br>This is project used for study Decision Tree machine learning model and Flask API from python.

We are using *tennis.csv* to training our model and using the following parameters to decide to play tennis or no:
- outlook
- temperature
- humidity
- wind

## Requirements
- python 3.9+
- flask

## PIP Install
Install the following packages from PIP:

`$ pip install Flask` <br>
`$ pip install pandas` <br>
`$ pip install scikit-learn matplotlib` <br>

# How to use:

1. First the all execute de script bellow for generate model:

`$ python DecisionTree.py` 

2. Run the flask api server

`$ python app.py`

3. Execute cURL with the desired parameters:

`$ curl -X POST http://127.0.0.1:5000/JogarTenis -d  "o=sunny&t=72&h=95&w=FALSE"`

Other example:

`$ curl -X POST http://127.0.0.1:5000/JogarTenis -d  "o=sunny&t=85&h=85&w=FALSE"`

