from flask import Flask,render_template,request,jsonify
import os
import base64
from final_api import prediction

UPLOAD_FOLDE='temp'
app=Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDE
@app.route('/')
def upload():
    return render_template("index.html")

@app.route('/success',methods=['POST'])
def success():
    if request.method=='POST':
        image=request.files['file']
        path = os.path.join(app.config['UPLOAD_FOLDER'], image.filename)
        image.save(path)
        image_string=base64.b64encode(image.read())
        print(image_string)
        s,name=prediction(path)
        list ={'score':str(s),
            'breed':name}
        return jsonify(list)


if __name__=="__main__":
    app.run(debug=False,threaded=False)
