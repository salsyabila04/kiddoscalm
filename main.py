from django.shortcuts import render 
# from flask import Flask, render_template, request, jsonify, session, render_template, url_for, escape, redirect
from flask import Flask, render_template, request, jsonify, session, render_template, url_for, redirect
from markupsafe import escape
from data import YouTubeData
import joblib
import numpy as np
from PIL import Image
import os , io , sys
import numpy as np 
import cv2 
import base64
from yolo_detection_images import runModel
import re
import pandas as pd



app = Flask(__name__)
app.secret_key = '\x1c\x8bP\x17\x06n\xd1\x1fCA\x10\x8d'
app.static_folder = 'static'
app.config ['SECRET-KEY'] = 'randomstring'
''# app.config['MAIL_SERVER']='smtp.gmail.com'
# app.config['MAIL_PORT'] = 465
# app.config['MAIL_USERNAME'] = "salsyabila80@gmail.com"
# app.config['MAIL_PASSWORD'] = "Salsyabilavidia.04"p
# app.config['MAIL_USE_TLS'] = False
# app.config['MAIL_USE_SSL'] = True

# mail = Mail(app)
# @app.route('/', methods = ['POST', 'GET'])
# def index():
#     return render_template('index.html')


# # tantrum kategori
# daftarPenyakit = ['Kategori Tantrum Rendah, silahkan mengunjungi fitur rekomendasi', 'Kategori Tantrum Tinggi, silhkan mengunjungi fitur rekomendasi dan segera konsultasikan ke Psikolog terdekat']

# # gejala
# daftarGejala = ['Anak Anda menangis dengan berteriak / menjerit dengan intensitas menangis 5-10 menit dalam sehari',
# 'Anak Anda Menangis dengan mengentakkan kaki dengan intensitas menangis 5-10 menit dalam sehari',
# 'Anak Anda Menangis dengan menjatuhkan diri ke lantai dengan intensitas meangis 5-10 menit dalam sehari',
# 'Anak Anda Menangis dengan menggapai lengan tangan atau lengan kaki orang tua dengan intensitas menangis 5-10 menit dalam sehari',
# 'Anak Anda Menangis dengan mendorong-dorong orang tua dengan intensitas menangis 5-10 menit dalam sehari',
# 'Anak Anda Menangis dengan menarik badan orang tua dengan intensitas menangis 5-10 menit dalam sehari',
# 'Anak Anda Menangis dengan berteriak / menjerit terjadi < 5x dalam seminggu',
# 'Anak Anda Menangis dengan menghentakkan kaki terjadi < 5x dalam seminggu',
# 'Anak Anda Menangis dengan menjatuhkan diri ke lantai terjadi < 5x dalam seminggu',
# 'Anak Anda Menangis dengan menggapai lengan kaki / lengan tangan terjadi < 5x dalam seminggu',
# 'Anak Anda Menangis dengan mendorong-dorong orang tua terjadi < 5x dalam seminggu',
# 'Anak Anda Menangis dengan menarik badan orang tua terjadi < 5x dalam seminggu',
# 'Anak Anda Menangis dengan melukai diri sendiri atau orang lain dengan intensitas menangis > 15 menit dalam sehari',
# 'Anak Anda Menangis dengan melempar barang dengan intensitas menangis > 15 menit dalam sehari',
# 'Anak Anda Menangis dengan megumpat atau berkata kasar dengan intensitas menangis > 15 menit dalam sehari',
# 'Anak Anda Menangis dengan tatapan marah dengan intensitas menangis > 15 menit dalam sehari',
# 'Anak Anda Menangis dengan melukai diri sendiri atau orang lain terjadi > 5x dalam seminggu',
# 'Anak Anda Menangis dengan melempar barang terjadi > 5x dalam seminggu',
# 'Anak Anda Menangis dengan mengumpat atau berkata kasar terjadi > 5x dalam seminggu',
# 'Anak Anda Menangis dengan tatapan marah terjadi > 5x dalam seminggu']

# @app.route('/', methods=['GET', 'POST'])
# def index():
#     return render_template('index.html', daftarGejala=daftarGejala)

# @app.route('/tantrum', methods=['POST', 'GET'])
# def tantrum():
#     gejala = request.form.getlist('gejala[]')
#     gejala = list(map(int, gejala)) # convert strings to integers
# #rules di forward chaining
#     if all(x in gejala for x in [1,2,3,4,5,6,7,8,9,10,11,12]):
#         penyakit = 0 # Kategori Tantrum Rendah
#     elif all(x in gejala for x in [13,14,15,16,17,18,19,20]):
#         penyakit = 1 # Kategori Tantrum Tinggi
#     else:
#         penyakit = None # Tidak dapat menentukan kategori
#     if penyakit is None:
#         result = "Tidak dapat menentukan kategori tantrum"
#     else:
#         result = daftarPenyakit[penyakit]
#     return render_template('results.html', gejala=gejala, daftarGejala=daftarGejala, result=result)''
@app.route('/tantrum', methods=['POST'])

def tantrum():
    # read the input from the HTML form
    gejala = request.form.getlist('gejala[]')

    # define the rules for forward chaining
    if '1' in gejala:
        kategori = 'Tantrum Rendah'
        solusi = 'Solusi untuk kategori tantrum rendah, silahkan mengunjungi fitur rekomendasi'
    elif '2' in gejala:
        kategori = 'Kategori Tantrum Tinggi'
        solusi = 'Solusi untuk kategori tantrum tinggi, silahkan mengunjungi fitur rekomendasi dan segera konsultasikan ke Psikolog Anak terdekat'
    else:
        kategori = 'Tidak bisa menentukan kategori'
        solusi = ''

    # return the result to the HTML template
    return render_template('results.html', kategori=kategori, solusi=solusi)

# mail = Mail(app)
# @app.route('/send_message', methods=['GET', 'POST'])
# def send_message():
#     if request.method == "POST":
#         email = request.form['email']
#         msg = request.form['message']
#         subject = request.form['subject']
        
#         message = Message(subject,sender="salsyabila80@gmail.com", recipients = [email])

#         message.body = msg

#         mail.send(message)

#         success = "Pesan Terkirim"
#         return render_template("result.html", success=success)


# @app.route('/index/recommend', methods=['POST'])
# def search1():
#     if request.method == 'POST':
#         # getting the video details like images and channelid
#         search = request.form['search']
#         data = YouTubeData(search)
#         snippet = data.get_channel_details(search)
#         return render_template('search_page.html', message=snippet, search=search)
#     else:
#         return render_template('base.html')

@app.route("/index", methods=['GET', 'POST'])  
def weight_prediction():
    if request.method == 'GET':
        return render_template('index.html')

@app.route('/search', methods=['POST'])
def search():
    if request.method == 'POST':
        # getting the video details like images and channelid
        search = request.form['search']
        data = YouTubeData(search)
        snippet = data.get_channel_details(search)
        return render_template('search_page.html', message=snippet, search=search)
    else:
        return render_template('base.html')

@app.route('/get_more/<channelId>/<search>/<videoid>', methods=['GET', 'POST'])
def get_more(channelId, search, videoid):
    if request.method == 'GET':
        data = YouTubeData(search)
        content = data.get_channel_stats(channelId)

        snippet = data.get_videoDetails(videoid)

        stats = data.get_statistics(videoid)

        return render_template("moredata.html", subCount=content, statistics=stats, snippet=snippet)
    else:
        return render_template("index.html")  

@app.route('/detectObject' , methods=['POST'])
def mask_image():
	# print(request.files , file=sys.stderr)
	file = request.files['image'].read() ## byte file
	npimg = np.fromstring(file, np.uint8)
	img = cv2.imdecode(npimg,cv2.IMREAD_COLOR)

	img = runModel(img)

	img = Image.fromarray(img.astype("uint8"))
	rawBytes = io.BytesIO()
	img.save(rawBytes, "JPEG")
	rawBytes.seek(0)
	img_base64 = base64.b64encode(rawBytes.read())
	return jsonify({'status':str(img_base64)})



@app.route('/test' , methods=['GET','POST'])
def test():
	print("log: got at test" , file=sys.stderr)
	return jsonify({'status':'succces'})

@app.route('/')
def home():
	return render_template('./index.html')

@app.after_request
def after_request(response):
    print("log: setting cors" , file = sys.stderr)
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
    response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE')
    return response

 

    
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
