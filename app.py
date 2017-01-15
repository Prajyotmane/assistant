from flask import Flask ,render_template, request
from werkzeug import secure_filename
import numpy as np
from sklearn.svm import NuSVC
app = Flask(__name__)

@app.route('/')
def hello_world():
    f= open("log.txt")
    f.readline()
    data = np.loadtxt(f)
    X = data[:,1:]
    y = data[:,0]
    clf = NuSVC(nu=0.1)
    clf.fit(X, y) 
    NuSVC(cache_size=200, class_weight=None, coef0=0.0,decision_function_shape=None, degree=3, gamma='auto', kernel='rbf',max_iter=-1, nu=0.5, probability=False, random_state=None,shrinking=True, tol=0.001, verbose=False)
    num = clf.predict([[14.25,2]])
    return render_template('hello.html', val = num)

@app.route('/upload')
def upload_file():
   return render_template('hello.html')
   
 
@app.route('/uploader', methods = ['GET', 'POST'])
def uploader_file():
   if request.method == 'POST':
      f = request.files['file']
      f.save(secure_filename(f.filename))
      return 'success'

@app.route('/hello')
def hello():
      return "Hello"

if __name__ == '__main__':
   app.run()