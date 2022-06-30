# from datetime import datetime
from fileinput import filename
from flask import Flask, render_template, url_for
from flask_migrate import Migrate
from entity import db
from config import Config
from controller import blueprint
# from flask_cors import CORS
# from flask_jwt_extended import JWTManager
 
application = Flask(__name__, static_url_path='/static')
application.config.from_object(Config)
application.register_blueprint(blueprint)

db.init_app(application)
migrate = Migrate(application, db)
# jwt = JWTManager(application)
# CORS(application, resources={r"/*": {"origins": "*"}})

@application.route('/')
def Index():
  images = url_for('static', filename='images/')
  return render_template('index.html', images=images)

@application.route('/contact')
def Contact():
  return render_template('contact.html')

@application.route('/feature')
def Feature():
  return render_template('Feature.html')

@application.route('/page1')
def About():
  return render_template('Page1.html')

if __name__ == '__main__':
  application.run(host='0.0.0.0', debug=True)
