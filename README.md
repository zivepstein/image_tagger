# image_tagger
This is a simple open-source flask app to view lots of images efficiently. Currently, it supports clicking on the images and saving out a json containing all the images you clicked on (for large image labelling tasks)

##installation
simply clone the repo, install and install the dependencies. the tagger only requires flask and pandas, with python3

##running the app
To run the app, `cd` to the directory and run ```python app.py --folder folder_name``` where `folder_name` is a folder of images located at `static/data/folder_name`. Then you can navigate to the url e.g http://127.0.0.1:5000/

The image tagger will soon support reading images from csv with the argument `--datasheet` but its not working now.

##usage

You can scroll through the images and click the next page button to continue. You can also click the proceed and save button to download a json containing the ID of all the images you clicked on in the session.
![alt text](https://github.com/zivepstein/image_tagger/blob/main/example.png?raw=true)
