import os
from zipfile import ZipFile

import os
os.environ ['KAGGLE_USERNAME'] = 'davidpeaperalta'
os.environ ['KAGGLE_KEY'] = '13dff3d69dbe9752ee8de1b951f8a99c'


with ZipFile('weather-prediction.zip', 'r') as f:
    f.extractall()
