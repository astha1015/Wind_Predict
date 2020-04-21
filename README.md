This is a high altitude wind prediction application using airplane data. 

Enclosed Components:
* classifiers (folder) -> includes splitted zipped files that sums up to a single classifier file - classifier_red.pkl 
* do_predict (script) -> takes arguments from the command line and passes them through the classifiers for the prediction

Prerequisites:
* Python 3
* Numpy
* Pandas
* scikit-learn
* pickle
* sys

Setup:
* Extract all the zipped files and concatenate them together using following:
          On windows: copy /B *.zip output.zip
          On Linux/: cat *.zip > output.zip

* Run the python script for prediction using:
          python do_predict.py
