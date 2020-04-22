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
* Archiver (https://archiverapp.com)

Setup:
* Clone the project or download in a local directory

* Open all the .split files using archiver app and combine to a single zipped file. Finally, extract the decompressed file within the same location.

* Run the python script for prediction using:
          python do_predict.py
