# -*- coding: utf-8 -*-

__author__ = "Carlos Esparza Medel"
__copyright__ = "Totalplay 2021, Total Play Delivery Project"
__version__ = "0.0.1"
__maintainer__ = "Carlos Esparza Medel"
__email__ = "carlos.esparzam@totalplay.com.mx"
__status__ = "Develop"

#Flask library
from flask import Flask

#Blueprint library
from Services.routes import v1

#Flask app
app = Flask(__name__)

#Register blueprint
app.register_blueprint(v1, url_prefix="/v1")
app.register_blueprint(v1, url_prefix="/")

#Conexión al localhost
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002, debug=False)