# Challenge-Mole

## Project Summary 
This tool takes the image of a mole as an input and calculates the probability of that mole being malign (Cancerous).
Skin Cancer is a common disease these days.
* A total of 18.1 million new cases and 9.6 million deaths from skin cancer were estimated globally in 2018.
* A recent study on the epidemiology of skin cancer stated that in Europe, the incidence would increase to 40–50/100,000 inhabitants per year in the next decade. 
* Studies from India report clinicopathological evaluation and also focus on the current scenarios of NMSCs
* The estimated 5-year survival rate for patients whose melanoma is detected early is about 98 percent in the U.S. The survival rate falls to 62 percent when the disease reaches the lymph nodes and 18 percent when the disease metastasizes to distant organs.
* Early detection is critical.


## Project mission:
- The main mission of this project was to create an app using CNN and Keras to diagnose the mole images. The app could predict whether the image detected/loaded is cancerous or benign

## Model Creation 
Built the CNN model from scratch, the key features implemented in the model are:
* **Conv2d** - All the convolutional layers have the same parameters except the input channel and output channel size.
* **MaxPool2d** - Downsamples the input along its spatial dimensions (height and width) by taking the maximum value over an input window (of size defined by pool_size) for each channel of the input.
* **BatchNormalization** - Used it to nullify the effect of an undesirable output from any specific layer by normalizing the values coming from the previous layer.
* **Dropout** - It is used for a better generalization of a model as it turns off a percentage of neurons randomly during training, which results in a more generalized model.
* **Flatten** - Used to turn the multi-dimensional output from the convolutional and max-pooling layers into one-dimensional tensor, to perform predictions.



## Deployment 
Used the Flask framework in python for creating the backend of the website, and used HTML, CSS, and Bootstrap for the structure and designing of each page. The input is taken in as a file and is checked whether it is an image or not using the extension of the file. The image is firstly stored in the static folder which, after each refresh, empties itself, so any image uploaded will be lost after a refresh. After the image has been uploaded and stored, it will be processed so that it is compatible with our model, and then passed to the model for classification. The result from the model is then displayed on the same page using jinja2. As for any type of error, we have used Flask framework's Flash messages module for displaying that error to the user in a readable format.

![Snapshot of the App](https://raw.githubusercontent.com/saifalbaghdadi/saifalbaghdadi/development/img/sc.png)


## Dataset 
This is a job we received from the company "skinCare".
The job entailed that we would develop a website that would be able to classify pictures of moles.

The dataset provided by the client is here https://www.kaggle.com/kmader/skin-cancer-mnist-ham10000
   

## Future work
The model was overfitting by a lot.  
To improve accuracy there has to be looked at more data augmentation techniques .

## Visuals: 

<p>  Model accuracy :(  0.7214  )  </p>
<p>  Model loss :    (  1.8070  ) </p>

![Snapshot of the App](https://raw.githubusercontent.com/saifalbaghdadi/saifalbaghdadi/development/img/output1.png)
![Snapshot of the App](https://raw.githubusercontent.com/saifalbaghdadi/saifalbaghdadi/development/img/output2.png)


## Installation on local machine

**On Windows*
$ virtualenv venv 
$ \venv\scripts\activate

**Or if using Linux/ MACOS**
$ python3 -m venv myvenv
$ source myvenv/bin/activate

**Install the requirements:**
$ pip install -r requirements.txt

**Run the app:**
$ python app.py

### Python version
* Python 3.9

### Packages used
* os
* Flask==2.1.2
* Pillow==9.1.1
* requests==2.27.1
* gunicorn==20.1.0
* Jinja2==3.1.2
* keras==2.9.0                        
* numpy==1.22.3 
* pandas==1.4.2
* seaborn==0.11.2
* matplotlib==3.5.2
* Werkzeug==2.1.2
* scikit-learn==1.1.1
* tensorflow.keras


## Timeline
16-05-2022 to 24/05/2022

## Author
Saif Malkshahi


