from flask import Flask
import configparser
application=Flask(__name__)

from . import views

c = configparser.ConfigParser()
c.read('src/config.ini')
application.secret_key=c['SECRETKEY']['secretKey']
