from flask import Flask
from apps.home import app_home
from apps.user import app_user
from apps.auth import app_auth
from apps.gif import app_gif
from apps.transaction import app_transaction

app = Flask(__name__)
app.register_blueprint(app_home)
app.register_blueprint(app_user)
app.register_blueprint(app_auth)
app.register_blueprint(app_gif)
app.register_blueprint(app_transaction)


if __name__ == "__main__":
    app.run(debug=True, port=3000)
