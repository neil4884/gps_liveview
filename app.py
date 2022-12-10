import views
from flask import Flask
from flask_cors import CORS
from flask import request

app = Flask(__name__)
CORS(app)


app.add_url_rule('/', view_func=views.index, methods=['GET'])
app.add_url_rule('/api/update', view_func=views.update, methods=['POST'])
app.add_url_rule('/api/update', view_func=views.view_update, methods=['GET'])
app.add_url_rule('/api/reset', view_func=views.reset, methods=['POST'])


if __name__ == '__main__':
    app.run()
