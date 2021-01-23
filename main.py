from flask import Flask, render_template, redirect, request, send_file
from process import *
from flask_cors import CORS, cross_origin
from flask_apscheduler import APScheduler
import sys, os
app = Flask(__name__)
cors = CORS(app)

UPLOAD_FOLDER= './static/process/'
app.config['UPLOAD_FOLDER']=UPLOAD_FOLDER
scheduler= APScheduler()


@app.route('/')
def index():
    return render_template('index.html')
@app.route('/process/togrey',methods=['POST'])
def toGrey():
    if len(request.files) ==  0:
        return 'bad request', 400
    f=request.files['image1']

    #save to precessing folder
    f.save(os.path.join(app.config['UPLOAD_FOLDER'],f.filename))
    filePath = './static/process/'+ f.filename

    #process image
    img = readImage(filePath)
    greyImg = rgb_to_grey(img)

    #write to image
    save(filePath, greyImg)

    #sendback image
    return send_file(filePath,as_attachment=True)


@app.route('/process/detectface',methods=['POST'])
def detectFace():
    if len(request.files) ==  0:
        return 'bad request', 400
    f=request.files['image1']


    #save to precessing folder
    f.save(os.path.join(app.config['UPLOAD_FOLDER'],f.filename))

    filePath = './static/process/'+ f.filename

    #process image
    img = readImage(filePath)
    faceImg = drawRecOnface(img)

    #write to image
    save(filePath, faceImg)

    #sendback image
    return send_file(filePath,as_attachment=True)



@app.route('/process/replaceface',methods=['POST'])
def replaceFace():
    if len(request.files) ==  0:
        return 'bad request', 400
    f1=request.files['image1']
    f2=request.files['image2']


    #save to precessing folder
    f1.save(os.path.join(app.config['UPLOAD_FOLDER'],f1.filename))
    f2.save(os.path.join(app.config['UPLOAD_FOLDER'],f2.filename))

    filePath1 = './static/process/'+ f1.filename
    filePath2 = './static/process/'+ f2.filename
    filePath_combined = './static/process/'+ f1.filename.split('.')[0]+f2.filename

    #process image
    img1 = readImage(filePath1)
    img2 = readImage(filePath2)
    newImg = replace(img1, img2)

    #write to image
    save(filePath_combined, newImg)

    #sendback image
    return send_file(filePath_combined,as_attachment=True)


@app.route('/process/swapface',methods=['POST'])
def swapface():
    if len(request.files) ==  0:
        return 'bad request', 400
    f1=request.files['image1']
    f2=request.files['image2']


    #save to precessing folder
    f1.save(os.path.join(app.config['UPLOAD_FOLDER'],f1.filename))
    f2.save(os.path.join(app.config['UPLOAD_FOLDER'],f2.filename))

    filePath1 = './static/process/'+ f1.filename
    filePath2 = './static/process/'+ f2.filename
    filePath_combined = './static/process/'+ f1.filename.split('.')[0]+f2.filename

    #process image
    img1 = readImage(filePath1)
    img2 = readImage(filePath2)
    newImg = replaceByFace(img1, img2)

    #write to image
    save(filePath_combined, newImg)

    #sendback image
    return send_file(filePath_combined,as_attachment=True)


#clear memory
def emptyfolder():
    filelist=[f for f in os.listdir('./static/process/')]
    for f in filelist:
        os.remove(os.path.join('./static/process/',f))
    print('files cleared')
if __name__ == '__main__':
    scheduler.add_job(id='empty folder', func=emptyfolder,trigger='interval',seconds=180)
    scheduler.start()
    app.run(debug=True)
