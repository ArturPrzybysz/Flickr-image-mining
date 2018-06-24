# Image mining application

## Setup
1.  Git clone this repository
2.  Create your virtual environment
3.  Download required modules: ```pip install -r requiremens.txt```
4.  Copy file `config_template.py`, give it a new name `config.py` and fill it following the hints inside
## How to run
The starting file is the `app.py`. You have two options: run it with, or without parameters:
#### _Without_ given parameters:
When run without supplied parameters, the application will download 100 most recently added to Flickr images.
###### Example:
```python app.py```
#### _With_ given parameters:
When run with parameters, the application will download given amount of images matching given keyword:
```python app.py keyword number_of_images```
The order of given parameters matters!

###### Example:
```python app.py dog 15```
```python app.py "longer example" 50```
