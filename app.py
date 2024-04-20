from flask import Flask,render_template, request
from gevent.pywsgi import WSGIServer

from view import auth_bp

app= Flask(__name__)
app.register_blueprint(auth_bp)





if __name__ == '__main__':
    app.run()
    # http_server = WSGIServer(('', 5000), app)
    # http_server.serve_forever()
