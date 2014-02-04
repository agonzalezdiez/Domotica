from bottle import route, run, template, static_file
import os
import sys
import json

@route('/hello/<name>')
def index(name):
    return template('<b>Hello {{name}}</b>!', name=name)

@route('/')
def index():
    #return template('<b>AAAAA</b>')
    return static_file('hola.html', root='./static/')

@route('/light')
def index():
    #sys.stdout.write("ENCIENDO")
    print "ENCIENDO"
    print os.system("python /home/pi/codigo/Domotica/raspberry/GPIO/bin/led_controller.py 1")
    #sys.stdout.write(ret)
    #return static_file('lighted.html', root='./static/')
    return json.dumps({"status":"OK"})

@route('/off')
def index():
    #sys.stdout.write("APAGO")
    print "APAGO"
    print os.system("python /home/pi/codigo/Domotica/raspberry/GPIO/bin/led_controller.py 0")    
    #sys.stdout.write(ret)
    #return static_file('hola.html', root='./static/')
    return json.dumps({"status":"OK"})

@route('/led_control')
def index():
    return static_file('led_control.html', root='./static/')

run(host='192.168.1.133', port=8080)
