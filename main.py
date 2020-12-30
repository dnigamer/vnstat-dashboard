__author__ = "Dni Gamer"
__copyright__ = "Copyright 2020, DniGamerOfficial"
__license__ = "GNU"
__version__ = "1.0"
__maintainer__ = "Dni Gamer"
__email__ = "dnigamerofficial@gmail.com"

import subprocess
import os
from flask import Flask, render_template, redirect, url_for, request, make_response
import time
from datetime import datetime
import multiprocessing

app = Flask(__name__)

# CONFIGURATION!!
# Write here the interface to keep tracking of
iface_name = "em0"

# Write here if you want looping or not
looping = True

# If you put looping as True, write here the update interval (in seconds)
update_interval = 5

##############
# DO NOT CHANGE ANYTHING BELOW HERE
##############

@app.route('/')
def index():
    if 'forcereload' in request.form:
        vnstati()
    else:
        pass
    r = make_response(render_template('index.html'))
    r.headers.set('Cache-Control', "no-cache, no-store, must-revalidate")
    r.headers.set('Pragma', "no-cache")
    r.headers.set('Expires', "0")
    return r

@app.route('/handler', methods=['POST'])
def handler():
    method = request.form["method"]
    if method == "forcereload":
        verification = vnstati()
        if verification == "OK":
            return redirect(url_for('wait'))
        else:
            return error(verification, "Check if you ran all the installation scripts correctly on your machine because there was a error with vnStati or vnStat")
    else:
        return redirect(url_for('error'))

@app.route('/wait', methods=['GET'])
def wait():
    return render_template('wait.html')

@app.route('/error', methods=['GET'])
def error(error, add):
    return render_template('error.html', erro=error, time=timee(), additional=add)

@app.route('/about', methods=['GET'])
def about():
    return render_template('about.html')

@app.route('/contact', methods=['GET'])
def contact():
    return render_template('contact.html')

# Processing functions

def vnstati():
    try:
        subprocess.check_output(f"vnstati -s -i {iface_name} -o static/images/sum.png", shell=True)
        subprocess.check_output(f"vnstati -5 -i {iface_name} -o static/images/minutes.png", shell=True)
        subprocess.check_output(f"vnstati -h -i {iface_name} -o static/images/hourly.png", shell=True)
        subprocess.check_output(f"vnstati -d -i {iface_name} -o static/images/daily.png", shell=True)
        subprocess.check_output(f"vnstati -m -i {iface_name} -o static/images/monthly.png", shell=True)
        return "OK"
    except Exception as err:
        return err

def timee():
    now = datetime.now()
    return now.strftime("%d/%m/%Y %H:%M:%S")

def updater(interval):
    if looping == True:
        while True:
            vnstati()
            time.sleep(interval)

def start_app():
    app.run(host='0.0.0.0', debug=True, port='8000')

if __name__ == "__main__":
    p1 = multiprocessing.Process(target=updater, args=(update_interval,))
    p2 = multiprocessing.Process(target=start_app)
    
    p1.start()
    p2.start()
    try:
        os.mkdir('images')
    except Exception as err:
        print(err)
        exit()
        